from flask import Blueprint, request, redirect, url_for
from views import user_view
from models.user_model import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route('/users', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        email = request.form['email']
        contraseña = request.form['contraseña']
        FNacimiento = request.form['FNacimiento']
        user = User(email, contraseña, FNacimiento)
        user.save()
        return redirect(url_for('user.usuarios'))
    return user_view.registro()