from src.data.actions.save_data import save_data
from src.data.actions.load_data import read_data

def delete_by_id(task_id):
    tasks = read_data()
    for task in tasks:
        if task_id == task["id"]:
            task_to_remove = task
            break
    if task_to_remove:
        tasks.remove(task_to_remove)
        save_data(tasks)
        return "Task removed succesfully"
    else:
        return f"Task with id {task_id} not found"