import json

def read_json(filepath):
    try:
        with open(filepath) as file_json:
            return json.load(file_json)
    except FileNotFoundError:
        return []
