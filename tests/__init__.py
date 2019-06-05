import unittest
import json
from urllib.parse import urljoin
from flights import app, db
from config import app_config

from flights.models.user import User


class BaseTestSetUp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app
        self.app.config.from_object(app_config['testing'])
        self.app = app.test_client()
        self.testHelper = TestHelper()
        self.base_url = self.testHelper.base_url
        self.app = self.testHelper.app
        self.headers = self.testHelper.headers

        with app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()


class TestHelper():

    def __init__(self):
        self.base_url = 'http://127.0.0.1:5000'
        self.headers = {'content-type': 'application/json'}
        self.app = app.test_client()
    # Create a new user

    def add_user(self, user_data):
        url = self.base_url + '/api/user/register'
        result = self.app.post(url, data=json.dumps(
            user_data), headers=self.headers)
        return result