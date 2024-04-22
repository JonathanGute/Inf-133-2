from database import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)  # Ajusta la longitud de la cadena según tu requerimiento
    contraseña = db.Column(db.String(100), nullable=False)  # Ajusta la longitud de la cadena según tu requerimiento
    FNacimiento = db.Column(db.String(50), nullable=False)

    def __init__(self, email, contraseña, FNacimiento):
        self.email = email
        self.contraseña = contraseña
        self.FNacimiento = FNacimiento

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()
        