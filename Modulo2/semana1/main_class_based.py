from flask import Flask, request, jsonify
from flask.views import MethodView

from src.actions.create_task import create_task
from src.actions.get_tasks import get_tasks
from src.actions.delete_by_id import delete_by_id
from src.actions.get_by_id import get_by_id
from src.actions.modify_task import modify_task

app = Flask(__name__)

class TaskItemApi(MethodView):
    """GET, POST"""
    
    def get(self):
        try:
            tasks = get_tasks()
            return jsonify({"data": tasks}), 200
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500

    def post(self):
        try:
            tasks = get_tasks() 
            response = create_task(request, jsonify, tasks) 
            return jsonify({"message": response}), 201
        except ValueError as ex:
            return jsonify({"message": str(ex)}), 400
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500

class TaskGroupApi(MethodView):
    """GET, DELETE, PATCH"""
    
    def get(self, task_id):
        try:
            response = get_by_id(task_id)
            
            return jsonify({"data": response}), 200

        except Exception as ex:
            return jsonify({"message": str(ex)}), 500

    def delete(self, task_id):
        try:
            response = delete_by_id(task_id)
            if "removed" in response.lower():
                return jsonify({"message": response}), 200
            else:
                return jsonify({"message": response}), 404 
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500

    def patch(self, task_id):
        try:
            response = modify_task(task_id, request)
            if "modified" in response.lower():
                return jsonify({"message": response}), 200
            else:
                return jsonify({"message": response}), 404  
        except Exception as ex:
            return jsonify({"message": str(ex)}), 500


task_item_view = TaskItemApi.as_view('task_item_api')
task_group_view = TaskGroupApi.as_view('task_group_api')

app.add_url_rule('/tasks', view_func=task_item_view, methods=['GET', 'POST'])
app.add_url_rule('/tasks/<int:task_id>', view_func=task_group_view, methods=['GET', 'DELETE', 'PATCH'])

if __name__ == "__main__":
    app.run(host="localhost", debug=True)
