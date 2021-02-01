import unittest
import json
from app.test.base import BaseTestCase


def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            email='example@gmail.com',
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            email='example@gmail.com',
            password='123456'
        )),
        content_type='application/json'
    )

def list_task(self):
    return self.client.get(
        '/task/',
        data=json.dumps(dict(
            email='example@gmail.com',
            password='123456'
        )),
        content_type='application/json'
    )

class TestAuthBlueprint(BaseTestCase):

    def test_user_create_task(self):
        with self.client:
            # user registration
            user_response = register_user(self)
            response_data = json.loads(user_response.data)
            self.assertTrue(response_data['Authorization'])
            self.assertEqual(user_response.status_code, 201)

            # registered user login
            login_response = login_user(self)
            data = json.loads(login_response.data)
            self.assertTrue(data['Authorization'])
            self.assertEqual(login_response.status_code, 200)

            create_response = self.client.post(
                '/task/',
                headers=dict(
                    Authorization='Bearer ' + data['Authorization']
                ),
                data=json.dumps(dict(
                    title='Title 1',
                    detail='Detail 1'
                )),
                content_type='application/json'
            )
            data_create = json.loads(create_response.data)
            self.assertEqual(data_create['message'], 'Task successfully created.')
            self.assertEqual(create_response.status_code, 201)




if __name__ == '__main__':
    unittest.main()