from importlib.resources import path
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse("create-user")
TOKEN_URL = reverse("api-token")
MANAGE_URL = reverse("manage-user")


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user_with_valid_data(self):
        payload = {
            "username": "Gandalf",
            "password": "abcabcabc",
            "email": "gandalf@gmail.com",
        }
        result = self.client.post(CREATE_USER_URL, payload)
        # 1. Test: Ist Status 201?
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        # 2. Test: Pruefe, ob Passwort korrekt
        user = get_user_model().objects.get(**result.data)
        self.assertTrue(user.check_password(payload['password']))
        # 3. Test: Ist das passwort richtigerweise nicht enthalten?
        self.assertNotIn("password", result.data)

    def test_create_user_token(self):
        """
            1. Test: HTTP Status Rsponse = 200?
            2. Test token in Antort dict
        """

        test_user_name = "Gandalf"
        test_password = "abcabcabc"
        payload = {
            "username": test_user_name,
            "password": test_password
        }
        create_user(**payload)
        result = self.client.post(TOKEN_URL, payload)
        # 1. Test
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        # 2. Test
        self.assertIn("token", result.data)
