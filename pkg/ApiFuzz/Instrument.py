"""This module created for APIFuzz
which implemetated the App instrumentation fucntion based on frida hook framework.
Initial version 0.01 , created on Jun 25th, 2024 by Gaofeng Zhou from Harman China system team.
"""

import sys
import frida
import chardet
from ApiFuzz import Monitor

def isgenerator(iterable):
    return hasattr(iterable,'__iter__') and not hasattr(iterable,'__len__')

class fuzzer(object):
    def __init__(self, devid, package_name, script_files):
        self.package_name = package_name
        self.script_files = script_files
        self.device = None
        self.session = None
        self.fuzzdata = None
        self.script = None
        self.pid = None
        self.device_id = str(devid).strip()
        self.fuzz_start_flag = 1

    def attach(self):
        # Create a device object
        # self.device = frida.get_usb_device()
        self.device = frida.get_device(self.device_id, timeout=4)
        # Start an app and connected to it
        self.pid = self.device.spawn([self.package_name])
        # print(self.pid)
        self.session = self.device.attach(self.pid)
        self.device.resume(self.pid)

    def detach(self):
        # detach session
        if self.session:
            self.session.detach()

    def load_script(self):
        # Inject Frida script
        for script_file in self.script_files:
            with open(script_file, 'rb') as f:
                file_content = f.read()
            encoding = chardet.detect(file_content)['encoding']
            with open(script_file, 'r', encoding=encoding) as f:
                script_content = f.read()
            self.script = self.session.create_script(script_content)
            self.script.on('message', self.on_message)
            self.script.load()

    def on_message(self, message, data):
        if message['type'] == 'send':
            payload = message['payload']
            # print("Payload is : ",payload)
            # if 'java.lang.Exception' in payload:
            #     with open("script_trace.txt", "a") as f:
            #         f.write(payload + "\n")
        #self.script.post({"my_data": "800:300"})
        if (self.fuzzdata and self.fuzz_start_flag ==2):
            print("Send fuzzing data to target-->:", self.fuzzdata)
            self.script.post({"my_data": self.fuzzdata})
        self.fuzz_start_flag = 1

    def start_fuzzing_test(self, *args):
        self.attach()
        self.load_script()
        # input('[+] Press <Enter> at any time to detach from instrumented program.\n\n')
        # self.detach()
        fuzz_block = []
        if len(args) == 0:
            print("No fuzzing data feed.")
            self.detach()
            sys.exit(1)
        elif len(args) == 1:
            fuzz_block= list(args)
            if isgenerator(fuzz_block[0]):
                fuzz_data_length = 1
            else:
                print("You feed the wrong fuzzing data, fuzzing data should be the generator object")
                self.detach()
                sys.exit(2)
        else:
            for data in args:
                if isgenerator(data):
                    fuzz_block.append(data)
                else:
                    print("You feed the wrong fuzzing data, fuzzing data should be the generator object")
                    self.detach()
                    sys.exit(3)
            fuzz_data_length = len(fuzz_block)
        print("Starting fuzzing test......")
        while True:
            if not (Monitor.adb_monitor_process_live(self.pid, self.device_id)):
                print("The App seems crashed and testing will be stoped.")
                self.detach()
                sys.exit(6)
            try:
                if self.fuzz_start_flag == 1:
                    newtmp = []
                    for fuzzerdata in fuzz_block:
                        tmpdata = next(fuzzerdata)
                        #print(tmpdata[0])
                        newtmp.append(str(tmpdata[0]))
                        #print(newtmp)
                    self.fuzzdata = '::'.join(newtmp)
                    #print(self.fuzzdata)
                    self.fuzz_start_flag = 2
            except StopIteration:
                print('Finished all fuzzer data.')
                self.detach()
                exit(0)
            except KeyboardInterrupt:
                print("Fuzzing test terminated with CTRL C by user.")
                self.detach()
                sys.exit(4)
            except Exception as e:
                print('Data generate failure:', e)
                self.detach()
                sys.exit(5)


#APP_PACKAGE_NAME = "com.example.demo"
# Frida script files
#SCRIPT_FILES = ["script.js", "request.js"]
#SCRIPT_FILES = ["script.js"]

# create App Instrumentation object and run
#instrumentation = AppInstrumentation(APP_PACKAGE_NAME, SCRIPT_FILES)
#instrumentation.run()

