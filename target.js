Java.perform(function () {
        var number_class = Java.use("java.lang.Integer");
        var tv_class = Java.use("com.example.api_fuzz_demo.MainActivity")
        tv_class.div.implementation = function (x, y) {
            var string_to_send = "Original para1: " + x.toString() + "-- Original para2: " + y.toString()
            send(string_to_send);
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
            return this.div(my_num1, my_num2);
        };
});