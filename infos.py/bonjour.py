import requests
import json

webhook_url = ""

data = {
    "content": "Bonjour!"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Message envoyé avec succès!")
else:
    print("Échec de l'envoi du message. Code de statut:", response.status_code)
