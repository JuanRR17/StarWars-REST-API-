from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __init__(self, email, username, password, is_active):
        self.email = email
        self.username = username
        self.password = password
        self.is_active =is_active

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))

    user = db.relationship('User', backref='users')
    character = db.relationship('Character', backref='users')
    planet = db.relationship('Planet', backref='users')

    def __repr__(self):
        return '<Favourite %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(120))
    birth_year = db.Column(db.String(120))
    eye_color = db.Column(db.String(120))
    skin_color = db.Column(db.String(120))
    height = db.Column(db.Integer)
    
    # def __init__(self, name, gender, birth_year, eye_color, skin_color, height):
    #     self.name = name
    #     self.gender = gender
    #     self.birth_year = birth_year
    #     self.eye_color = eye_color
    #     self.skin_color = skin_color
    #     self.height = height

    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "skin_color": self.skin_color,
            "height": self.height,
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(120))
    population = db.Column(db.String(120))
    orbital_period = db.Column(db.String(120))
    rotation_period = db.Column(db.String(120))
    diameter = db.Column(db.Integer)

    # def __init__(self, name, climate, population, orbital_period, rotation_period, diameter):
    #     self.name = name
    #     self.climate = climate
    #     self.population = population
    #     self.orbital_period = orbital_period
    #     self.rotation_period = rotation_period
    #     self.diameter = diameter

    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population,
            "orbital_period": self.orbital_period,
            "rotation_period": self.rotation_period,
            "diameter": self.diameter,
        }