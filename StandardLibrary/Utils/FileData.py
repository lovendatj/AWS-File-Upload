import json
import os


def read_json(path: str) -> dict:
    with open(path, 'r') as file:
        data = json.load(file)
    return data


def jsonify(data: dict) -> dict:
    return json.dumps(data)


def write_json(path: str, data: dict, force: bool = True, indent: int = 0) -> None:
    isExist = os.path.exists(path)
    if force and isExist:
        print("Making new directory")
        os.makedirs(path)
    elif not isExist and not force:
        raise Exception('Could not find directory for file output')
    with open(path, 'w') as file:
        json.dump(data, file, indent=indent)
