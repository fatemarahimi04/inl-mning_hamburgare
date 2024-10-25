import unittest
from app_kitchen import app 

class KitchenViewTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_receive_order(self):
        order_data = {
            "name": "Hamburgare utan Lök",
            "price": 89,
            "ingredients": ["Kött", "Bröd", "Sallad"]
        }
        response = self.app.post('/order', json=order_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_method(self):
        response = self.app.get('/order') 
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
