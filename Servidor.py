from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hola', methods=['GET'])
def hello_world():
    return jsonify({"response":"hello world"})

@app.route('/insert/value', methods=['POST'])
def insert_value():
    data = request.get_json(force=True)
    valor = data['character']
    valor2 = data['power']
    print("el valor 1 es: ",valor)
    print("el valor 2 es: ",valor2)
    return jsonify({"response":"informacion recibida"})

if __name__ == "__main__":
    app.run("localhost", port=3000)
