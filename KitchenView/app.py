from flask import Flask, request

kitchen_app = Flask(__name__)

@kitchen_app.route('/kitchen', methods=['POST'])
def receive_order():
    order = request.get_json()
    print("Ny beställning mottagen:", order)
    return "Beställning mottagen", 200

if __name__ == '__main__':
    kitchen_app.run(port=5001, debug=True)
