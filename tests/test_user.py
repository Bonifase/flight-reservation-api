import unittest
import json
from tests import BaseTestSetUp
from tests.data_source import *


class TestUserCase(BaseTestSetUp):

    def test_new_user_registration_works(self):
        """Test API can register new user successfully (POST request)"""

        response = self.testHelper.add_user(new_user)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "Registration successfull. Please log in")
        self.assertEqual(response.status_code, 201)