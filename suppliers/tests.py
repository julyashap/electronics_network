from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from suppliers.models import Supplier, Product
from users.models import User


class SupplierAPITestCase(APITestCase):
    """Класс тестирования представлений модели Supplier"""

    def setUp(self):
        self.user = User.objects.create(email='user@test.com', password='test_password')

        self.supplier = Supplier.objects.create(
            name='test_supplier',
            email='supplier@example.com',
            country='test_country',
            city='test_city',
            street='test_street',
            house_number=35,
            created_at='2024-10-31 10:00:00'
        )

    def test_create_supplier(self):
        supplier_data_level_1 = {
            'name': 'test_supplier',
            'email': 'supplier_1@example.com',
            'country': 'test_country',
            'city': 'test_city',
            'street': 'test_street',
            'house_number': 35,
            'debt_to_supplier': 125.15,
            'supplier_link': self.supplier.pk,
            'products': [
                {
                    'name': 'product_1',
                    'model': 'model_a',
                    'realized_at': '2023-10-01 12:00'
                },
                {
                    'name': 'product_2',
                    'model': 'model_b',
                    'realized_at': '2023-10-02 23:54:00'
                }
            ]
        }

        supplier_data_level_2 = {
            'name': 'test_supplier_2',
            'email': 'supplier_2@example.com',
            'country': 'test_country_2',
            'city': 'test_city_2',
            'street': 'test_street_2',
            'house_number': 15,
            'debt_to_supplier': 11026.79,
            'supplier_link': self.supplier.pk + 1,
            'products': [
                {
                    'name': 'product_1',
                    'model': 'model_a',
                    'realized_at': '2023-10-01 12:00'
                },
                {
                    'name': 'product_2',
                    'model': 'model_b',
                    'realized_at': '2023-10-02 23:54:00'
                }
            ]
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.post(reverse('suppliers:supplier_create'), data=supplier_data_level_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 2)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(response.json().get('level'), 1)

        response = self.client.post(reverse('suppliers:supplier_create'), data=supplier_data_level_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 3)
        self.assertEqual(Product.objects.count(), 4)
        self.assertEqual(response.json().get('level'), 2)

    def test_retrieve_supplier(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('suppliers:supplier_retrieve', args=[self.supplier.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.supplier.name)

    def test_list_supplier(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('suppliers:supplier_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(len(response.data['results']), 1)

        response = self.client.get(reverse('suppliers:supplier_list'), query_params={'search': 'city'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.data['next'], None)
        self.assertEqual(response.data['previous'], None)
        self.assertEqual(len(response.data['results']), 0)

    def test_update_supplier(self):
        update_data = {
            'name': 'updated_supplier',
            'email': 'updated@example.com',
            'country': 'updated_country',
        }

        self.client.force_authenticate(user=self.user)

        response = self.client.patch(reverse('suppliers:supplier_update', args=[self.supplier.pk]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.supplier.refresh_from_db()
        self.assertEqual(self.supplier.name, 'updated_supplier')
        self.assertEqual(self.supplier.email, 'updated@example.com')

    def test_destroy_supplier(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse('suppliers:supplier_destroy', args=[self.supplier.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Supplier.objects.count(), 0)


class ProductAPITestCase(APITestCase):
    """Класс тестирования представлений модели Product"""

    def setUp(self):
        self.user = User.objects.create(email='user@test.com', password='test_password')

        self.supplier = Supplier.objects.create(
            name='test_supplier',
            email='supplier@example.com',
            country='test_country',
            city='test_city',
            street='test_street',
            house_number=35,
            created_at='2024-10-31 10:00:00'
        )

        self.product = Product.objects.create(
            name='test_product',
            model='model_a',
            realized_at='2024-10-31 10:05:00',
            supplier=self.supplier
        )

    def test_create_product(self):
        self.client.force_authenticate(user=self.user)

        product_data = {
            'name': 'new_product',
            'model': 'model_c',
            'realized_at': '2023-10-03',
            'supplier': self.supplier.pk
        }

        response = self.client.post(reverse('suppliers:product_create'), product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_update_product(self):
        self.client.force_authenticate(user=self.user)

        update_data = {
            'name': 'test_product_updated',
            'model': 'model_c',
            'realized_at': '2023-10-03',
            'supplier': self.supplier.pk
        }

        response = self.client.patch(reverse('suppliers:product_update', args=[self.product.pk]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'test_product_updated')

    def test_destroy_product(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(reverse('suppliers:product_destroy', args=[self.product.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
