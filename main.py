import os
from dotenv import load_dotenv
from update_label import update_label
from get_labels import get_labels
from load_config import load_config
from create_label import create_label
from check_diff import checkDiff
from helpers import by_name

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
url = "https://api.github.com/repos/kailau1/label_sync/labels"



response_data = get_labels()
desired = load_config("config.json")
current = by_name(response_data)
final = checkDiff(current, desired)

for label in final["to_create"]:
    create_label(desired[label])

for label in final["to_update"]:
    update_label(desired[label])
