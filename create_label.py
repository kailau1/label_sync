import requests
import json

def create_label(url, label, ACCESS_TOKEN):
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }

    response = requests.post(url=url, headers=headers, json=label)
    print(label["name"])
    print(response.status_code)
