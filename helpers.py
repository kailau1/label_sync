def by_name(labels):
    name_labels = {}
    for label in labels:
        name_labels[label['name']] = label

    return name_labels