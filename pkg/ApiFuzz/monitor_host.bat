@echo on
call C:\Users\test\anaconda3\Scripts\activate.bat C:\Users\test\anaconda3\envs\pythonfuzz
frida-ps -H %1 -a
