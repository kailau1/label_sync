import json

def load_config(path):

    with open(path, "r") as f:
        return by_name(json.load(f))

def by_name(labels):
    name_labels = {}
    for label in labels:
        name_labels[label['name']] = label

    return name_labels