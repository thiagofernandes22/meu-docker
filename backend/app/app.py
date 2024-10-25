import os 

import mysql.connector

from flask import Flask, jsonify

app = Flask(__name__)

DATABASE_URL = os.getenv('DATABASE_URL')

def get_db_connection():
    config = {
        'user': 'root',
        'password': 'RootPassword',
        'host': 'mysql',  
        'database': 'Company',
        'port': '3306'
    }
    connection = mysql.connector.connect(**config)
    return connection

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/daniel')
def hello_daniel():
    return "Hello, Daniel!"


@app.route('/users')
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")  
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
