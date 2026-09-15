import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
url = "https://api.github.com/repos/kailau1/label_sync/labels"

headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {ACCESS_TOKEN}",
}

response = requests.get(url, headers=headers)
pretty = json.loads(response.text)

print(response.status_code)
print(response.text)
print(json.dumps(pretty, indent=4))