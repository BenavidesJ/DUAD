from src.data.actions.load_data import read_data
from src.data.actions.save_data import save_data

def modify_task(task_id, req):
    tasks = read_data()
    new_task_data = req.json
    updated = False
    for task in tasks:
        if task_id == task["id"]:
            task.update(new_task_data)
            updated = True
            break
    if updated:
        save_data(tasks)
        return "Task modified succesfully"
    else:
        return f"Task with id {task_id} not found"