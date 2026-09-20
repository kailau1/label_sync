import requests
import json

def get_labels(url, ACCESS_TOKEN):
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(url, headers=headers)
    response_data = json.loads(response.text)

    return(response_data)
