from src.common.tasks_statuses import tasks_statuses
from src.data.actions.save_data import save_data

def create_task(req, res, existing_data):

    new_task = req.json
            
    task_status = new_task.get("status")
            
    if "title" not in new_task:
        raise ValueError("title is a required field")
    if "description" not in new_task:
        raise ValueError("description is a required field")
    if "status" not in new_task:
        raise ValueError("status is a required field")
    if task_status not in tasks_statuses:
        raise ValueError(f"status must be valid: {tasks_statuses[0]} or {tasks_statuses[1]} or {tasks_statuses[2]}")
    
    task_id = len(existing_data) + 1
    task = {
        "id" : task_id,
        "title" : new_task["title"],
        "description" : new_task["description"],
        "status" : new_task["status"]
    }
    
    save_data(task, existing_data)
    
    return "Task created succesfuly"