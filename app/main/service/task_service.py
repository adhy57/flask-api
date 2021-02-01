import uuid
import datetime

from app.main import db
from app.main.model.task import Task

from flask import request

from app.main.service.auth_helper import Auth

def save_new_task(data):
    user, status = Auth.get_logged_in_user(request)
    token = user.get('data')
    
    new_task = Task(
        title=data['title'],
        detail=data['detail'],
        user_id=token['user_id'],
    )
    save_changes(new_task)
    response_object = {
        'status': 'success',
        'message': 'Task successfully created.'
    }
    return response_object, 201

def update_task(data, task_id):
    user, status = Auth.get_logged_in_user(request)
    token = user.get('data')

    task = Task.query.filter(Task.id==task_id, Task.user_id==token["user_id"]).first()
    if task :
        task.title = data['title']
        task.detail = data['detail']
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Task successfully updated.'
        }
    else :
        response_object = {
            'status': 'fail',
            'message': 'Unable to delete task.'
        }

    return response_object, 201



def get_all_tasks():
    data, status = Auth.get_logged_in_user(request)
    token = data.get('data')
    return Task.query.filter_by(user_id=token["user_id"]).all()

def delete_task(data):
    user, status = Auth.get_logged_in_user(request)
    token = user.get('data')

    task = Task.query.filter(Task.id==data['id'], Task.user_id==token["user_id"]).first()
    if task :
        db.session.delete(task)
        db.session.commit()
    response_object = {
        'status': 'success',
        'message': 'Task successfully removed.'
    }
    return response_object, 201
    


# def get_a_user(public_id):
#     return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

# def generate_token(user):
#     try:
#         # generate the auth token
#         auth_token = user.encode_auth_token(user.id)
#         response_object = {
#             'status': 'success',
#             'message': 'Successfully registered.',
#             'Authorization': auth_token
#         }
#         return response_object, 201
#     except Exception as e:
#         response_object = {
#             'status': 'fail',
#             'message': 'Some error occurred. Please try again.',
#             'e': print(e.message)
#         }
#         return response_object, 401