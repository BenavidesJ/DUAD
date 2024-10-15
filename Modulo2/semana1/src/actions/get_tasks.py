from src.data.actions.load_data import read_data

def get_tasks():
    tasks = read_data()
    return tasks