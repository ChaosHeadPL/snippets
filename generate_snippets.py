import os
import json


BASE_DIR = os.path.dirname(__file__)


def list_folders():
    return [x for x in os.listdir(BASE_DIR) if os.path.isdir(x) and x[0] != "."]


def list_json_files(dirname):
    location = os.path.join(BASE_DIR, dirname)
    output = []
    for dirpath, dirnames, filenames in os.walk(location):
        for filename in [f for f in filenames if f.endswith(".json")]:
            output.append(os.path.join(location, filename))
    
    return output

 
def read_json_file(file):
    print(f"Reading {file}")
    with open(file, "r") as json_file:
        data = json.load(json_file)
    return data


def save_json_file(file, data):
    print(f"Saving {file}.json")
    with open(f"{file}.json", "w") as json_file:
        json.dump(data, json_file, indent=2)


def main():
    files = []
    for folder in list_folders():
        snippets = {}
        for file in list_json_files(folder):
            snippets = dict(snippets, **read_json_file(file))

        save_json_file(folder, snippets)

    #TODO: copy and replace with existing snippets


if __name__ == "__main__":
    #TODO: parametize script using fire lib
    main()
