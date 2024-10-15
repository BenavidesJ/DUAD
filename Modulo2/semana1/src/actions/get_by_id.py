from src.data.actions.load_data import read_data

def get_by_id(task_id):
    tasks = read_data()
    for task in tasks:
        if task_id == task["id"]:
            requested_task = task
            break
        else:
            requested_task = None
            
    if not requested_task:
        return f"Task with id {task_id} not found"
    else:
        return requested_task