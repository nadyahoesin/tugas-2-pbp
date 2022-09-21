from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class PageTest(TestCase):
    fixtures = ['initial_mywatchlist_data.json']

    def test_html_page(self):
        response = self.client.get('/html/')
        self.assertEqual(response.status_code, 200)

    def test_json_page(self):
        response = self.client.get('/json/')
        self.assertEqual(response.status_code, 200)

    def test_xml_page(self):
        response = self.client.get('/xml/')
        self.assertEqual(response.status_code, 200)