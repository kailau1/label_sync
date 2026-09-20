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