import sqlite3
import os
from flask import Flask, render_template, request, redirect, jsonify
import requests
app = Flask(__name__)

# Koppla till databasen
def get_db_connection():
    conn = sqlite3.connect('C:/Users/fatem/Desktop/Inlämning Hamburgare/inl-mning_hamburgare/MenuStore/menu.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM menu_items')
    menu_items = cursor.fetchall()
    
    conn.close()
    return render_template('index.html', menu_items=menu_items)

baseURL = 'http://' + os.getenv('KITCHENVIEW_HOST', 'localhost:5001')

def makeURL(order_id): 
    return f"{baseURL}/order/{order_id}"

def addOptions(url, options):
    if options:
        url += '?'
        url += '&'.join(options) 
    return url

def sendToKitchen(order):
    requrl = 'http://localhost:5001/' 
    
    print('Using KitchenView URL: ' + requrl)
    
    response = requests.post(requrl, json=order)
    
    if response.status_code == 200:
        print('Order sent successfully!')
    else:
        print('Failed to send order')
    
    return response

@app.route('/order', methods=['POST'])
def place_order():
    order = request.json 
    
    response = sendToKitchen(order) 

    if response.status_code == 200:
        return jsonify({'message': 'Order sent successfully!'}), 200
    else:
        return jsonify({'message': 'Failed to send order'}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000) 

