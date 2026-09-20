from github_api import update_label, get_labels, create_label
from config import load_config, by_name
from diff import check_diff





if __name__ == "__main__":

    response_data = get_labels()
    desired = load_config("config.json")
    current = by_name(response_data)
    final = check_diff(current, desired)

    for label in final["to_create"]:
        create_label(desired[label])

    for label in final["to_update"]:
        update_label(desired[label])
