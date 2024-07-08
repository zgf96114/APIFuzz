from ApiFuzz.Instrument import fuzzer as fuzz
from ApiFuzz import Mutators
import uiautomator2 as u2
import time
import threading

APP_PACKAGE_NAME = "com.example.api_fuzz_demo" #Give the app package name you want to test
SCRIPT_FILES = ["target.js"] #Give the app package name you want to test

deviceid = '127.0.0.1:62001' #mutiple devices need to give the deviceid
ui_dev = u2.connect(deviceid) #initilize and connect to uiautomator
ui_dev.implicitly_wait(20)
print("Connected uiautomator2")

para1 = Mutators.mutator_int(1,-10,10) #create generator object for test Parameter 1
para2 = Mutators.mutator_int(1,-10,10) #create generator object for test Parameter 2

instrumentation = fuzz(deviceid, APP_PACKAGE_NAME, SCRIPT_FILES) #create App Fuzzer object

"""
device control function which simualte the click behavior just as user(in another thread)
"""
def device_control():
    time.sleep(0.5)
    while True:
            try:
                if instrumentation.fuzz_start_flag == 2:
                    ui_dev(resourceId="com.example.api_fuzz_demo:id/but2").click()
            except Exception as e:
                print("device control wrong: ", e)
            time.sleep(1)

control_thread = threading.Thread(target=device_control) #start a child threod to simulate the button click
control_thread.setDaemon(True) #set the child thread as Daemon thread
control_thread.start() #start running the child thread
instrumentation.start_fuzzing_test(para1,para2) # feed para1 and par2 and start the api fuzzing test.





