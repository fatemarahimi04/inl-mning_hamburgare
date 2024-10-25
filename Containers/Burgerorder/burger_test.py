import unittest
import json
from app import app  # Importera burgerorder-appen

class BurgerOrderTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_order_post(self):
        order_data = {
            "name": "Hamburgare utan Lök",
            "price": 89,
            "ingredients": ["Kött", "Bröd", "Sallad"]
        }
        response = self.app.post('/order', data=json.dumps(order_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertEqual(response_data['message'], 'Order skickad!')

if __name__ == '__main__':
    unittest.main()
