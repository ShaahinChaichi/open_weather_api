import json


def write_to_file(text):
    with open('data.json', 'w') as f:
        json.dump(text, f)
