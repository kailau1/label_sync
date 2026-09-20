import requests
import json
import urllib

def update_label(url, label, ACCESS_TOKEN):
    headers = {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {ACCESS_TOKEN}",
            }

    response = requests.patch(url=url+ "/" + urllib.parse.quote(label["name"]), headers=headers, json=label)
    print(label["name"])
    print(response.status_code)