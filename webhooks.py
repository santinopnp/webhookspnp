from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("¡Pago recibido!", data)  # Aquí va la lógica de agregar al canal/grupo
    return 'OK', 200

@app.route('/', methods=['GET'])
def home():
    return '¡Servidor funcionando!', 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
