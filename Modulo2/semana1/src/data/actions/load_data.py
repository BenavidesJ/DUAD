import json

def read_data():
    try:
        with open("src/data/tasks_data.json", "r") as file:
            data = json.load(file)
    except Exception as e:
        print("Error while reading data on file", e)
            
    return data