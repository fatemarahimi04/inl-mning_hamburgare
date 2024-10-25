
import sqlite3
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('C:/Users/fatem/Desktop/Inlämning Hamburgare/inl-mning_hamburgare/MenuStore/menu.db')
    conn.row_factory = sqlite3.Row
    return conn

def sendToKitchen(order):
    requrl = 'http://localhost:5001/order'  
    print('Using KitchenView URL: ' + requrl)

    response = requests.post(requrl, json=order)

    if response.status_code == 200:
        print('Order sent successfully!')
    else:
        print('Failed to send order')

    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        order = request.json  

        burger_name = order.get('name')
        price = order.get('price')
        exclusions = order.get('exclusions', [])

        order_details = f"{burger_name} utan {', '.join(exclusions)}" if exclusions else burger_name

        sendToKitchen({
            'name': order_details,
            'price': price
        })

        return jsonify({'message': 'Order sent successfully!'}), 200

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM menu_items')
    menu_items = cursor.fetchall()
    conn.close()

    return render_template('index.html', menu_items=menu_items)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
