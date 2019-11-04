import unittest
import json
from tests import BaseTestSetUp
from tests.test_users.data_source import *


class TestLoginCase(BaseTestSetUp):

    def test_new_user_login_works(self):
        """Test API can login new user successfully (POST request)"""

        self.testHelper.add_user(new_user)
        response = self.testHelper.login_user(new_user)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "You logged in successfully.")
        self.assertEqual(response.status_code, 200)
    
    def test_user_cannot_login_with_blank_email(self):
        """Test API cannot login user with blank email (POST request)"""

        self.testHelper.add_user(new_user)
        response = self.testHelper.login_user(user_missing_email)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "email is required field")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_login_with_blank_password(self):
        """Test API cannot login user with blank password (POST request)"""
        
        self.testHelper.add_user(new_user)
        response = self.testHelper.login_user(user_missing_password)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "password is required field")
        self.assertEqual(response.status_code, 409)


    def test_user_cannot_login_with_invalid_email(self):
        """Test API cannot login user with invalid email (POST request)"""

        self.testHelper.add_user(new_user)
        response = self.testHelper.login_user(invalid_email)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "Invalid email, Please try again")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_login_with_invalid_password(self):
        """Test API cannot register user with invalid password (POST request)"""

        self.testHelper.add_user(new_user)
        response = self.testHelper.login_user(invalid_password)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "wrong password")
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_login_with_blank_email_key(self):
        """Test API cannot login user with blank email key (POST request)"""

        self.testHelper.add_user(new_user)
        response = self.testHelper.login_user(missing_email_key)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "email key is missing")

    def test_user_cannot_login_with_blank_password_key(self):
        """Test API cannot login user with blank password key (POST request)"""

        self.testHelper.add_user(new_user)
        response = self.testHelper.login_user(missing_password_key)
        result = json.loads(response.data.decode())
        self.assertEqual(result[
            "message"], "password key is missing")


    def test_user_cannot_login_with_email_with_spaces(self):
         """Test API cannot login user with email with spaces (POST request)"""

         self.testHelper.add_user(new_user)
         response = self.testHelper.login_user(email_with_spaces)
         result = json.loads(response.data.decode())
         self.assertEqual(result[
            "message"], "Invalid email, Please try again")
         self.assertEqual(response.status_code, 409)

    def test_user_can_logout(self):
        """Test API cannot logout user (GET request)"""

        self.testHelper.add_user(new_user)
        self.result = self.testHelper.login_user(new_user)
        self.token = json.loads(self.result.data.decode())['AuthToken']
        response = self.testHelper.logout_user(token=self.token)
        result = json.loads(response.data.decode())
        self.assertIn(result[
            "message"], "Logout Successful")
        self.assertEqual(response.status_code, 200)
