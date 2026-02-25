from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class BookAPITest(APITestCase):

    def test_create_books(self):
        url = reverse('book-list', kwargs={'version': 'v1'})

        data = {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "published_date": "1925-04-10"
        }

        response = self.client.post(url, data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)