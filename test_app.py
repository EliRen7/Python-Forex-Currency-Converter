from app import app
from unittest import TestCase

class CurrencyConvertsRates(TestCase):
    def test_form(self):
     with app.test_client() as client:
        res = class.get('/')
        html = res.get_data(as_text=True)
        self.assertEqual(res.status_code, 200)


