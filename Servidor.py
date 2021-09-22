from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/bienvenido', methods=['GET'])
def hello_world():
    return jsonify({"response":"Welcome to SmartClass"})

@app.route('/carga', methods=['POST'])
def insert_value():
    data = request.get_json(force=True)
    tipo = data['tipo']
    path = data['path']
    print("el tipo es: ",tipo)
    print("el path es: ",path)
    return jsonify({"response":"informacion recibida"})






#if __name__ == "__main__":
   # app.run("localhost", port=3000)
   # matriz_dispersa()


