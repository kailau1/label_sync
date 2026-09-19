import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
url = "https://api.github.com/repos/kailau1/label_sync/labels"

def load_config(path):

    with open(path, "r") as f:
        return by_name(json.load(f))

def getLabels():
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    response = requests.get(url, headers=headers)
    response_data = json.loads(response.text)

    return(response_data)

def by_name(labels):
    name_labels = {}
    for label in labels:
        name_labels[label['name']] = label

    return name_labels

def checkDiff(current, desired):
    desired_set = set(desired)
    current_set = set(current)

    in_both = current_set.intersection(desired_set)
    to_create = desired_set.difference(current_set)
    extras = current_set.difference(desired_set)
    to_update = set()
    unchanged = set()

    for label in in_both:
        if current[label]['color'] == desired[label]['color'] and current[label]['description'] == desired[label]['description']:
            unchanged.add(label)
        else:
            to_update.add(label)

    final = {}
    final["to_create"] = to_create
    final["to_update"] = to_update
    final["extras"] = extras
    final["unchanged"] = unchanged

    return final


def create_label(label):
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {ACCESS_TOKEN}",
        }

    response = requests.post(url=url, headers=headers, json=label)
    print(label["name"])
    print(response.status_code)


response_data = getLabels()
desired = load_config("config.json")
current = by_name(response_data)
final = checkDiff(current, desired)

for label in final["to_create"]:
    create_label(desired[label])
