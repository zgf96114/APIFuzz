function hookTest7() {
    Java.perform(function() {
        Java.enumerateLoadedClasses({
                onMatch:function(name, handler){
                    if(name.indexOf("com.example.demo")!=-1){
                        console.log(name);
                        var clazz=Java.use(name);
                        console.log(clazz);
                        var methods=clazz.class.getDeclaredMethods();
                        for(var i=0;i<methods.length;i++){
                            console.log(methods[i]);
                        }
                    }
                },
                onComplete:function(){

                }
        });
    });
};

setImmediate(hookTest7)