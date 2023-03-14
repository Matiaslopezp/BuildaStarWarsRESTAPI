from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Fav_user(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    user_fav=db.Column(db.String(120),db.ForeignKey("user.email"))
    rel_user=db.relationship("User")
    def serialize(self):
        return {
            "id": self.id,
            "fav_users": self.fav_user,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<People %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            # do not serialize the password, its a security breach
        }

class Fav_people(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    people_name= db.Column(db.String(120), db.ForeignKey("people.name"))
    user_fav=db.Column(db.String(120),db.ForeignKey("user.email"))
    rel_people=db.relationship("People")
    rel_user=db.relationship("User")

class Planet(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    planet= db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<Planet%r>' % self.planet
    def serialize(self):
        return {
            "id": self.id,
            "planet": self.planet,
            # do not serialize the password, its a security breach
        }

class Fav_planet(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    planet_name= db.Column(db.String(120), db.ForeignKey("planet.planet"))
    user_fav=db.Column(db.String(120),db.ForeignKey("user.email"))
    rel_planet=db.relationship("Planet")
    rel_user=db.relationship("User")