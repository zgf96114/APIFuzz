import frida
rdev = frida.get_device("127.0.0.1:62001", timeout=4)

def on_message(message, data):
    print("[on_message] message:", message["payload"])
    #for f in message["payload"]:
    #    print(f.type)
    #    print(f.name)
    #    print(f.address)

session = rdev.attach("API_Fuzz_Demo")
script = session.create_script("""
Java.perform(function () {
        console.log("%----Applications with following modules and functions----%");
        var process_Obj_Module_Arr = Process.enumerateModules();
        for(var i = 0; i < process_Obj_Module_Arr.length; i++) {
            console.log("*************************************************************");
            console.log("----->Module Name: ",process_Obj_Module_Arr[i].name);
            console.log("*************************************************************");
            //const hooks = Module.load('libRScpp.so');
            //var Exports = hooks.enumerateExports();
            //var Exports = process_Obj_Module_Arr[i].enumerateExports();
            let Exports = process_Obj_Module_Arr[i].enumerateExports();
            send(Exports);
            //for(var j = 0; j < Exports.length; j++) {
            //    send(Exports[j].type);
            //    send(Exports[j].name);
            //    send(Exports[j].address);
            //}
            //delete Exports;
            //Exports = null;
        }
    });
""")
script.on("message", on_message)
script.load()

