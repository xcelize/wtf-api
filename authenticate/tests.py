from django.test import TestCase
from rest_framework.test import APITestCase, force_authenticate
from .models import User


# Create your tests here.
class UserTestCase(TestCase):

    def test_create_user_low_password(self):
        data = {
            "password": 'test',
            "email": "alexis@alexis.fr"
        }
        reponse = self.client.post(path='http://127.0.0.1:8000/api/inscription', data=data, format='json')
        assert reponse.status_code == 400

    def test_create_user_valide(self):
        data = {
            "password": 'JesuisUnTest-12345',
            "email": "alexis@alexis.fr"
        }
        reponse = self.client.post(path='http://127.0.0.1:8000/api/inscription', data=data, format='json')
        assert reponse.status_code == 201

    def test_update_user_without_auth(self):
        data = {
            "telephone": "0618785485"
        }
        reponse = self.client.put(path='http://127.0.0.1:8000/api/profil/1', data=data, format='json')
        assert reponse.status_code == 401

