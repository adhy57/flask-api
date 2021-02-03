from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.dto import TaskDto
# from ..service.user_service import save_new_user, get_all_users, get_a_user
from ..service.task_service import get_all_tasks, save_new_task, delete_task, update_task

api = TaskDto.api
_task = TaskDto.task


@api.route('/')
class TaskList(Resource):
    @api.doc('list_of_task')
    @token_required
    @api.marshal_list_with(_task, envelope='data')
    def get(self):
        """List all task"""
        return get_all_tasks()

    @api.response(201, 'Task successfully created.')
    @token_required
    @api.doc('create a new task')
    @api.expect(_task, validate=True)
    def post(self):
        """Creates a new Task """
        data = request.json
        return save_new_task(data=data)

    @api.response(201, 'Task successfully removed.')
    @token_required
    @api.doc('delete a task')
    @api.expect(TaskDto.task_delete, validate=True)
    def delete(self):
        data = request.json
        return delete_task(data=data)

    


@api.route('/<task_id>/')
@api.param('task_id', 'The Task identifier')
@api.response(404, 'Task not found.')
class Task(Resource):
    @api.response(201, 'Task successfully updated.')
    @token_required
    @api.doc('update a task')
    @api.expect(_task, validate=True)
    def put(self, task_id):
        data = request.json
        return update_task(data, task_id)