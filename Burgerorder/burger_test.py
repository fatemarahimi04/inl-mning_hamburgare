import json
from app import app  

client = app.test_client()

def test_index_get():
    response = client.get('/')
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

def test_order_post():
    order_data = {
        "name": "HeroBurger",
        "price": 100,
        "exclusions": ["Lök"]
    }
    response = client.post('/', data=json.dumps(order_data), content_type='application/json')
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json['message'] == 'Order sent successfully!'

if __name__ == "__main__":
    test_index_get()
    test_order_post()
