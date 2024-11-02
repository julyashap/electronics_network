from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User, CodePhrase


class UserAPITestCase(APITestCase):
    """Класс тестирования представлений модели User"""

    def setUp(self):
        self.codephrase = CodePhrase.objects.create(company_name='test_company', codephrase='testcph')
        self.user = User.objects.create(email='test_user@example.com', password='test_password')

        self.query_params = {
            'company_name': 'test_company',
            'codephrase': 'testcph'
        }

    def test_create_user_with_correct_codephrase(self):
        create_data = {
            'email': 'new_user@example.com',
            'password': 'new_password'
        }

        response = self.client.post(
            reverse('users:user_create'),
            query_params=self.query_params,
            data=create_data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_create_user_with_incorrect_codephrase(self):
        create_data = {
            'email': 'new_user@example.com',
            'password': 'new_password'
        }

        incorrect_query_params = {
            'company_name': 'test_company',
            'codephrase': 'testcphinc'
        }

        response = self.client.post(
            reverse('users:user_create'),
            query_params=incorrect_query_params,
            data=create_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.data, {
            "detail": "Кодовая фраза 'testcphinc' для test_company неверна!"
        })

    def test_update_user(self):
        update_data = {
            'email': 'updated_user@example.com',
            'password': 'updated_password'
        }

        response = self.client.patch(
            reverse('users:user_update', args=[self.user.pk]),
            query_params=self.query_params,
            data=update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated_user@example.com')

    def test_retrieve_user(self):
        response = self.client.get(
            reverse('users:user_retrieve', args=[self.user.pk]),
            query_params=self.query_params
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], self.user.email)

    def test_destroy_user(self):
        response = self.client.delete(
            reverse('users:user_destroy', args=[self.user.pk]),
            query_params=self.query_params
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
