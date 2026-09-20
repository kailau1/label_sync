from helpers import by_name
import json

def load_config(path):

    with open(path, "r") as f:
        return by_name(json.load(f))