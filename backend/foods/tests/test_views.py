from rest_framework import status
from rest_framework.test import APITestCase
from foods.models import Food
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


def client_api():
    username = 'testeuser'
    password = '12345'
    User.objects.create_superuser(
        username, f'{username}@example.com', password)
    user = User.objects.get(username=username)
    token = Token.objects.get_or_create(user=user)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token[0].key)
    return client


def createItem(client):
    endpoint = '/api/food/'
    data = dict(name='Kibe de forno',
                quantity=100,
                proteins=52,
                carbohydrates=2,
                fats=5,
                active=True)
    return client.post(endpoint, data, format='json')


def updateItem(client, id):
    endpoint = f'/api/food/{id}/'
    data = dict(name='Kibe de forno',
                quantity=100,
                proteins=52,
                carbohydrates=2,
                fats=5,
                active=False)
    return client.put(endpoint, data, format='json')


def patchItem(client, id):
    endpoint = f'/api/food/{id}/'
    data = dict(active=False)
    return client.patch(endpoint, data, format='json')


def deleteItem(client, id):
    endpoint = f'/api/food/{id}/'
    return client.delete(endpoint)


class TestCreateFoodItem(APITestCase):
    """
    Ensure we can create a new food
    """

    def setUp(self):
        self.client_api = client_api()
        self.response = createItem(self.client_api)

    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_item_was_created(self):
        self.assertEqual(Food.objects.count(), 1)

    def test_item_has_correct_name(self):
        self.assertEqual(Food.objects.get().name, 'Kibe de forno')


class TestUpdateFoodItem(APITestCase):
    """
    Ensure we can update an existing food item using PUT
    """

    def setUp(self):
        self.client_api = client_api()
        createItem(self.client_api)
        id = Food.objects.get().id
        self.assertEqual(Food.objects.get().active, True)
        self.response = updateItem(self.client_api, id)

    def test_received_200_updated_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        self.assertEqual(Food.objects.get().active, False)


class TestPatchFoodItem(APITestCase):
    """
    Ensure we can update an existing food item using PATCH
    """

    def setUp(self):
        self.client_api = client_api()
        createItem(self.client_api)
        id = Food.objects.get().id
        self.assertEqual(Food.objects.get().active, True)
        self.response = patchItem(self.client_api, id)

    def test_received_200_ok_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_updated(self):
        self.assertEqual(Food.objects.get().active, False)


class TestDeleteFoodItem(APITestCase):
    """
    Ensure we can delete a food item
    """

    def setUp(self):
        self.client_api = client_api()
        createItem(self.client_api)
        id = Food.objects.get().id
        self.response = deleteItem(self.client_api, id)

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_the_item_was_deleted(self):
        self.assertEqual(Food.objects.count(), 0)
