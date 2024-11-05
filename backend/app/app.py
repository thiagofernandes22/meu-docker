import os 

import mysql.connector

from flask import Flask, jsonify

app = Flask(__name__)


def get_db_connection():
    config = {
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'host': os.getenv('MYSQL_HOST'),
        'database': os.getenv('MYSQL_DATABASE'),
        'port': os.getenv('MYSQL_PORT')
    }

#validar as variaveis definidas
    for key, value in config.items():
        if value is None:
            raise EnvironmentError(f"A variável de ambiente {key} não está definida.")
    

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
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")  
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500  



@app.route('/users/<int:user_id>')
def greet_user(user_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        
        if user:
            return f"Olá, {user['name']}!"
        else:
            return jsonify({"error": "Usuário não encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
