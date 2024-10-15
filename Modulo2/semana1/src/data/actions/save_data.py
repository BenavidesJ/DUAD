import json

def save_data(data, existing_data=None):
    try:
        with open("src/data/tasks_data.json", "w") as file:
            if existing_data is not None:
                existing_data.append(data)
            
                json.dump(existing_data, file, indent=2)
            else: 
                json.dump(data, file, indent=2)
    except Exception as e:
        print("Error while writting data on file", e)