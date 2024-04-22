from flask import Flask
from controllers import user_controllers
from database import db 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  

app.register_blueprint(user_controllers.user_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)