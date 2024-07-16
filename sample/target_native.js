Java.perform(function () {
        var number_class = Java.use("java.lang.Integer");
        var div_addr = Module.findExportByName("libdemo_fuzz_native.so","Java_com_test_demo_1fuzz_1native_MainActivity_div");
        //console.log("Function address: " + div_addr);
        if(div_addr != null){
	        //Interceptor.attach-->是Frida里的一个拦截器
            Interceptor.attach(div_addr,{
	            //onEnter里-->可以打印和修改参数
                onEnter: function(args){  //-->args传入参数
                    //console.log("Args is ->" + args[0], args[1], args[2],args[3]);
                    var oldpara1 = parseInt(args[2]);
                    var oldpara2 = parseInt(args[3]);
                    //console.log("Old args is ->" + oldpara1 + " , " + oldpara2);
                    send("test");
                    //args[2] = ptr(100);
                    //args[3] = ptr(10);
                    //console.log("OK ->");
                    //console.log(args[0].readInt());  //打印第1个参数的值
                    //console.log("gap");
                    //console.log(ptr(args[1].readInt()));  //打印第2个参数的值
                    //console.log(parseInt(args[2]), parseInt(args[3]));
                    //console.log(args[1].readInt());
                    //console.log(args[3].readInt());
                    //send(args[3].readInt());
                    //send((args[1])
                    //console.log(this.context.x1);  // 打印寄存器内容
                    //console.log(args[1].toInt32()); //toInt32()转十进制
					//console.log(args[2].readCString()); //读取字符串 char类型
					//console.log(hexdump(args[2])); //内存dump
					var string_to_recv;
                    recv(function (received_json_object) {
                    string_to_recv = received_json_object.my_data
                    }).wait(); //block execution till the message is received
                    var numbers= string_to_recv.split('::');
                    //console.log("Para1:", numbers[0], ", Para2:", numbers[1]);
                    //var my_string = string_class_r.$new(string_to_recv); //covert to java string
                    var my_num1 = number_class.valueOf(numbers[0]).intValue();
                    var my_num2 = number_class.valueOf(numbers[1]).intValue();
                    console.log("Converted Para1-->:", my_num1, ", Para2-->:", my_num2);
                    args[2] = ptr(my_num1);
                    args[3] = ptr(my_num2);
                },
                //onLeave里-->可以打印和修改返回值
                onLeave: function(retval){  //retval-->返回值
                    //console.log(retval);
                    console.log("retval:",retval.toInt32());
                    //console.log("retval:",parseInt(retval));
                    //console.log("retval:",ptr(retval));
                }
            })
        }
});