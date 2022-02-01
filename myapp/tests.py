from django.test import TestCase
from django.test import Client

# Create your tests here.

class ViewsTestCase(TestCase):
    """ Test cases for views """

    url = 'http://127.0.0.1:8000/details/'
    client = Client()

    def test_get_no_data_no_query_param(self):
        """ Test case to check getting data """
        response = self.client.get(self.url, {"id": "1234"})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            response.content, b'{"errorMsg": "Invalid movie id: 1234", "id": "1234"}')

    def test_get_no_data_without_query_param(self):
        """ Test case to check getting data """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'{"data": [], "id": null}')
