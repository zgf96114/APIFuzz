import frida
rdev = frida.get_device("127.0.0.1:62001", timeout=4)
processes = rdev.enumerate_processes()
print("Processes following:")
for process in processes:
    print (process)

applcations = rdev.enumerate_applications()
print("Applications following:")
for app in applcations:
    print (app)