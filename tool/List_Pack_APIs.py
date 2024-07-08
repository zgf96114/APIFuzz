import frida
rdev = frida.get_device("127.0.0.1:62001", timeout=4)

def on_message(message, data):
    print("[on_message] message:", message["payload"])
    #for f in message["payload"]:
    #    print(f.type)
    #    print(f.name)
    #    print(f.address)

session = rdev.attach("demo")
script = session.create_script("""
Java.perform(function() {
        Java.enumerateLoadedClasses({
                onMatch:function(name, handler){
                    if(name.indexOf("com.example.demo")!=-1){
                        console.log("Class name:--->", name);
                        var clazz=Java.use(name);
                        console.log(clazz);
                        var methods=clazz.class.getDeclaredMethods();
                        for(var i=0;i<methods.length;i++){
                            console.log("Method Name: ", methods[i]);
                        }
                        console.log("|****************************************************************|");
                    }
                },
                onComplete:function(){

                }
        });
    });
""")
script.on("message", on_message)
script.load()

