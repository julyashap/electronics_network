from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User, CodePhrase


class UserAPITestCase(APITestCase):
    def setUp(self):
        self.codephrase = CodePhrase.objects.create(company_name='test_company', codephrase='testcph')
        self.user = User.objects.create(email='test_user@example.com', password='test_password')

    def test_create_user_with_correct_codephrase(self):
        create_data = {
            'email': 'new_user@example.com',
            'password': 'new_password',
            'company_name': 'test_company',
            'codephrase': 'testcph'
        }
        response = self.client.post(reverse('users:user_create'), data=create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_create_user_with_incorrect_codephrase(self):
        create_data = {
            'email': 'new_user@example.com',
            'password': 'new_password',
            'company_name': 'test_company',
            'codephrase': 'testcph_incorrect'
        }
        response = self.client.post(reverse('users:user_create'), data=create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.data, {
            "detail": "Кодовая фраза 'testcph_incorrect' для test_company неверна!"
        })

    def test_update_user(self):
        update_data = {
            'email': 'updated_user@example.com',
            'password': 'updated_password',
            'company_name': 'test_company',
            'codephrase': 'testcph'
        }
        response = self.client.patch(reverse('users:user_update', args=[self.user.pk]), data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'updated_user@example.com')

    def test_destroy_user(self):
        destroy_data = {
            'company_name': 'test_company',
            'codephrase': 'testcph'
        }

        response = self.client.delete(reverse('users:user_destroy', args=[self.user.pk]), data=destroy_data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
