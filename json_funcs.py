import json


def change_data(key, value):
    data = get_data()
    data[key] = value
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)


def get_data():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        return data
