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
        console.log("%----Modules Info following----%");
        var hooks = Module.load('libdemo_fuzz_native.so');
        console.log("模块名称:",hooks.name);
        console.log("模块地址:",hooks.base);
        console.log("大小:",hooks.size);
        console.log("文件系统路径",hooks.path)
    });
""")
script.on("message", on_message)
script.load()

