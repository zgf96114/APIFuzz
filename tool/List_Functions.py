import frida
rdev = frida.get_device("127.0.0.1:62001", timeout=4)

def on_message(message, data):
    print("[on_message] message:", message, "data:", data)

session = rdev.attach("demo")
script = session.create_script("""
rpc.exports.enumerateModules = function () {
  return Process.enumerateModules();
};
//rpc.exports.enumerate_exports = function () {
//  return Process.enumerateModules().enumerateExports();
//};
""")
# script = session.create_script("""
# Java.perform(function () {
#         var process_Obj_Module_Arr = Process.enumerateModules();
#         for(var i = 0; i < process_Obj_Module_Arr.length; i++) {
#             if(process_Obj_Module_Arr[i].path.indexOf("debuggerd")!=-1)
#             {
#                 console.log("模块名称:",process_Obj_Module_Arr[i].name);
#                 send("模块名称:",process_Obj_Module_Arr[i].name)
#                 console.log("模块地址:",process_Obj_Module_Arr[i].base);
#                 send("模块地址:",process_Obj_Module_Arr[i].base)
#                 console.log("大小:",process_Obj_Module_Arr[i].size);
#                 send("大小:",process_Obj_Module_Arr[i].size);
#                 console.log("文件系统路径",process_Obj_Module_Arr[i].path);
#                 send("文件系统路径",process_Obj_Module_Arr[i].path);
#             }
#          }
#     });
# """)
script.on("message", on_message)
script.load()

for module in script.exports_sync.enumerate_modules():
    print (module)
