from flask import Flask, request, jsonify

from src.actions.create_task import create_task
from src.actions.get_tasks import get_tasks
from src.actions.delete_by_id import delete_by_id
from src.actions.get_by_id import get_by_id
from src.actions.modify_task import modify_task

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Service healthy!</h1>"

@app.route("/tasks", methods=["GET", "POST"])
@app.route("/tasks/<int:task_id>", methods=["GET", "DELETE", "PATCH"])
def tasks_handler(task_id=None):
    try:
        tasks = get_tasks()
        method = request.method
        
        if method == "GET":
            
            if task_id is not None:
                response = get_by_id(task_id)
                return jsonify({"data": response}), 200
            else:
                return jsonify({"data": tasks}), 200
            
        elif method == "POST":
            
           response = create_task(request, jsonify, tasks)
           return jsonify({"message": response}), 201
       
        elif method == "DELETE":
            
            if task_id is None:
                return jsonify({"message": "Task ID is required for DELETE"}), 400
            
            response = delete_by_id(task_id)
            return jsonify({"message": response}), 200
        
        elif method == "PATCH":
            
            if task_id is None:
                return jsonify({"message": "Task ID is required for PATCH"}), 400
            
            response = modify_task(task_id, request)
            return jsonify({"message": response}), 200

    except ValueError as ex:
         return jsonify(message=str(ex)), 400
    except Exception as ex:
        return jsonify(message=str(ex)), 500
    
    

if __name__ == "__main__":
    app.run(host="localhost", debug=True)