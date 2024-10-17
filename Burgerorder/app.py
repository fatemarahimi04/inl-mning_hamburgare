# import sqlite3
# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# # Connect to the database
# def get_db_connection():
#     conn = sqlite3.connect('C:/Users/mrahi/Desktop/Fati/MenuStore/menu.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# # URL for the kitchen service
# def sendToKitchen(order):
#     requrl = 'http://localhost:5001/order' 
#     print('Using KitchenView URL: ' + requrl)
#     response = requests.post(requrl, json=order)
    
#     if response.status_code == 200:
#         print('Order sent successfully!')
#     else:
#         print('Failed to send order')

#     return response

# # Handle both GET (menu) and POST (order) requests on the same route
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Process the order
#         order = request.form  # Retrieve order data from form submission
        
#         burger_name = order.get('burger_name')
#         price = order.get('price')
#         exclusions = request.form.getlist('exclusions')
        
#         # Format the order to show exclusions if any
#         order_details = f"{burger_name} without {', '.join(exclusions)}" if exclusions else burger_name
        
#         # Send order to kitchen
#         sendToKitchen({
#             'name': order_details,
#             'price': price
#         })
        
#         return jsonify({'message': 'Order sent successfully!'}), 200

#     # GET request: render the menu
#     conn = get_db_connection()
#     cursor = conn.cursor()
    
#     cursor.execute('SELECT * FROM menu_items')
#     menu_items = cursor.fetchall()
    
#     conn.close()
#     return render_template('index.html', menu_items=menu_items)

# if __name__ == "__main__":
#     app.run(debug=True, port=5000)


import sqlite3
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Koppla till databasen
def get_db_connection():
    conn = sqlite3.connect('C:/Users/fatem/Desktop/Inlämning Hamburgare/inl-mning_hamburgare/MenuStore/menu.db')
    conn.row_factory = sqlite3.Row
    return conn

# Skicka beställning till köket
def sendToKitchen(order):
    requrl = 'http://localhost:5001/order'  # Uppdatera URL om du vill ha den utan /order
    print('Using KitchenView URL: ' + requrl)

    response = requests.post(requrl, json=order)

    if response.status_code == 200:
        print('Order sent successfully!')
    else:
        print('Failed to send order')

    return response

# Hantera GET (meny) och POST (beställning) på samma route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        order = request.json  # Ta emot beställningsdata som skickas via JSON

        burger_name = order.get('name')
        price = order.get('price')
        exclusions = order.get('exclusions', [])

        order_details = f"{burger_name} utan {', '.join(exclusions)}" if exclusions else burger_name

        # Skicka beställningen till köket
        sendToKitchen({
            'name': order_details,
            'price': price
        })

        return jsonify({'message': 'Order sent successfully!'}), 200

    # Hämta menyposter från databasen
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM menu_items')
    menu_items = cursor.fetchall()
    conn.close()

    return render_template('index.html', menu_items=menu_items)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
