import frida
rdev = frida.get_device("127.0.0.1:62001", timeout=4)
front_app = rdev.get_frontmost_application()
print(front_app)
