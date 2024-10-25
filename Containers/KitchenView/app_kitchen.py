from flask import Flask, request, render_template
from app_kitchen import app
app = Flask(__name__)

orders = []

@app.route('/order', methods=['POST'])
def place_order():
    order = request.get_json()
    print("Mottagen beställning:", order)  
    orders.append(order) 
    return "Order mottagen", 200


@app.route('/')
def kitchen_view():
    print("Aktuella beställningar:", orders) 
    return render_template('kitchen.html', orders=orders)

if __name__ == "__main__":
    app.run(debug=True, port=5001)