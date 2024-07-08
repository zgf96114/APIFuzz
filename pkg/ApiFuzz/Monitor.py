"""This module created for APIFuzz
which implemetated the monitor fucntion to check if app/process exit or not.
Initial version 0.01 , created on Jun 26th, 2024 by Gaofeng Zhou from Harman China system team.
"""
import sys
import time
import frida
import tempfile
import subprocess
import os

# sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
# print(sys.path)
curr_folder = os.path.dirname(__file__)
#print(curr_folder)

def adb_monitor_process_live(pid: int, devid: str="127.0.0.1:62001") -> bool:
    monitor_bat = f"{curr_folder}\monitor_adb.bat {devid}"
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(monitor_bat, shell=True, stdout=tempf, stderr=tempf)
        proc.wait()
        tempf.seek(0)
        output = tempf.read().decode('utf-8')
        #print(output)
        # output = commandOutput.strip(CRLF)
    if not (str(pid) in output):
        #print("The App seems crashed and testing will be stoped.")
        #print(str(pid))
        return False
    else:
        return True

def remote_monitor_process_live(pid: int, host: str) -> bool:
    monitor_bat = f"{curr_folder}\monitor_host.bat {host}"
    with tempfile.TemporaryFile() as tempf:
        proc = subprocess.Popen(monitor_bat, shell=True, stdout=tempf, stderr=tempf)
        proc.wait()
        tempf.seek(0)
        output = tempf.read().decode('utf-8')
        # output = commandOutput.strip(CRLF)
    if not (str(pid) in output):
        print("The App seems crashed and testing will be stoped.")
        return False
    else:
        return True
