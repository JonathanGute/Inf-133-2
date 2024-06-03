from flask import Blueprint, jsonify, request

from app.models.producto_model import Producto
from app.utils.decorators import jwt_required, roles_required
from app.views.producto_view import render_producto_detail, render_producto_list

# Crear un blueprint para el controlador de productos
producto_bp = Blueprint("producto", __name__)


# Ruta para obtener la lista de productos
@producto_bp.route("/productos", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_productos():
    productos = Producto.get_all()
    return jsonify(render_producto_list(productos))


# Ruta para obtener un producto específico por su ID
@producto_bp.route("/productos/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_producto(id):
    producto = Producto.get_by_id(id)
    if producto:
        return jsonify(render_producto_detail(producto))
    return jsonify({"error": "Producto no encontrado"}), 404


# Ruta para crear un nuevo producto
@producto_bp.route("/productos", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_producto():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Validación simple de datos de entrada
    if not name or not description or price is None or stock is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo producto y guardarlo en la base de datos
    producto = Producto(name=name, description=description, price=price, stock=stock)
    producto.save()

    return jsonify(render_producto_detail(producto)), 201


# Ruta para actualizar un producto existente
@producto_bp.route("/productos/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_producto(id):
    producto = Producto.get_by_id(id)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    stock = data.get("stock")

    # Actualizar los datos del producto
    producto.update(name=name, description=description, price=price, stock=stock)

    return jsonify(render_producto_detail(producto))


# Ruta para eliminar un producto existente
@producto_bp.route("/productos/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_producto(id):
    producto = Producto.get_by_id(id)

    if not producto:
        return jsonify({"error": "Producto no encontrado"}), 404

    # Eliminar el producto de la base de datos
    producto.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
