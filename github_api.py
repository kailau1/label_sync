import requests
import json
import urllib
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
url = "https://api.github.com/repos/kailau1/label_sync/labels"

def update_label(label):
    headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {ACCESS_TOKEN}",
            }

    response = requests.patch(url=url+ "/" + urllib.parse.quote(label["name"]), headers=headers, json=label)
    print(label["name"])
    print(response.status_code)

def create_label(label):
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }

    response = requests.post(url=url, headers=headers, json=label)
    print(label["name"])
    print(response.status_code)


def get_labels():
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(url, headers=headers)
    response_data = json.loads(response.text)

    return(response_data)
