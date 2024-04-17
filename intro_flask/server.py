from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "¡Hola, mundo!"


@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

@app.route("/sumar", methods=["POST"])
def sumar():
    try:
        data = request.get_json()
        num1 = int(data["num1"])
        num2 = int(data["num2"])
        suma = num1 + num2
        return jsonify({"resultado": suma})
    except (KeyError, ValueError):
        return jsonify({"error": "Se requieren los parámetros 'num1' y 'num2' como números."}), 400

@app.route("/sumar", methods=["POST"])
def sumar():
    data = request.json
    numero1 = data.get("num1")
    numero2 = data.get("num2")
    
    if numero1 is None or numero2 is None:
        return jsonify({"error": "Se requieren dos números en el cuerpo de la solicitud."}), 400
    
    try:
        resultado = int(num1) + int(num2)
        return jsonify({"resultado": resultado}), 200
    except ValueError:
        return jsonify({"error": "Los valores proporcionados no son números válidos."}), 400

if __name__ == "__main__":
    app.run()