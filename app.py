import os
from flask import Flask, render_template, request, jsonify
import mysql.connector


app = Flask(__name__)

# Configurações do banco de dados MySQL

db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME')
}

def connect_db():
    return mysql.connector.connect(**db_config)


# Configurações de rota

@app.route('/')
def index():
    return render_template('index.html')

# Adicionar item no carrinho
@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome_cliente= request.form['customerName']
    nome_produto = request.form['produto']
    endereco = request.form['endereco']

    conn = connect_db()
    cursor = conn.cursor()
    query = "INSERT INTO carrinho (nome_cliente, nome_produto, endereço) VALUES (%s, %s, %s)"

    cursor.execute(query, (nome_cliente, nome_produto, endereco))
    conn.commit()

    cursor.close() 
    conn.close()

    return jsonify({"message": "Pedido adicionado com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
