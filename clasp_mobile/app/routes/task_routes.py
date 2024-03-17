from flask import Blueprint, request, jsonify
from app.models.task_model import TaskModel
# from app.utils.auth import authenticate

task_bp = Blueprint('task', __name__)


@task_bp.route('/tasks', methods=['GET'])
# @authenticate
def get_tasks():
    args = request.args.to_dict()
    task_model = TaskModel()
    documents = task_model.find_all(args)
    return jsonify(documents), 200

# @task_bp.route('/tasks', methods=['POST'])
# @authenticate
# def create_task():
#     data = request.json
#     task_model = TaskModel()
#     task_id = task_model.insert(data)
#     return {'id': task_id}, 201
