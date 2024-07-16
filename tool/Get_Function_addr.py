import frida
rdev = frida.get_device("127.0.0.1:62001", timeout=4)

def on_message(message, data):
    print("[on_message] message:", message["payload"])
    #for f in message["payload"]:
    #    print(f.type)
    #    print(f.name)
    #    print(f.address)

session = rdev.attach("Demo_Fuzz_Native")
script = session.create_script("""
Java.perform(function () {
        console.log("%----Function address: ----%");
        //const hooks = Module.load('libdemo_fuzz_native.so');
        
        Module.getExportByName('libdemo_fuzz_native.so', 'div')
        console.log("Java_com_test_demo_1fuzz_1native_MainActivity_div address:",Module.findExportByName('libdemo_fuzz_native.so', 'Java_com_test_demo_1fuzz_1native_MainActivity_div'));
    });
""")
script.on("message", on_message)
script.load()

