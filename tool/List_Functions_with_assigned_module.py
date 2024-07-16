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
        console.log("%----Module with following functions----%");
        const hooks = Module.load('libdemo_fuzz_native.so');
        console.log("Imported Functions:");
        console.log("=============================================================");
        var Imports = hooks.enumerateImports();
        for(var i = 0; i < Imports.length; i++) {
            //函数类型
            console.log("type:",Imports[i].type);
            //函数名称
            console.log("name:",Imports[i].name);
            //属于的模块
            console.log("module:",Imports[i].module);
            //函数地址
            console.log("address:",Imports[i].address);
        }
        
        console.log("Exported Functions:");
        console.log("***************************************************************");
        var Exports = hooks.enumerateExports();
        for(var i = 0; i < Exports.length; i++) {
            //函数类型
            console.log("type:",Exports[i].type);
            //函数名称
            console.log("name:",Exports[i].name);
            //函数地址
            console.log("address:",Exports[i].address);
         }
    });
""")
script.on("message", on_message)
script.load()

