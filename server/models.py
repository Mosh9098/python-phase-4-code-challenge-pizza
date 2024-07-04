from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = "restaurants"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade="all, delete-orphan")

    def to_dict(self, full=False):
        if full:
            return {
                "id": self.id,
                "name": self.name,
                "address": self.address,
                "restaurant_pizzas": [rp.to_dict() for rp in self.restaurant_pizzas]
            }
        else:
            return {
                "id": self.id,
                "name": self.name,
                "address": self.address
            }

class Pizza(db.Model, SerializerMixin):
    __tablename__ = "pizzas"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ingredients": self.ingredients
        }

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = "restaurant_pizzas"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id', ondelete='CASCADE'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id', ondelete='CASCADE'))

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not (1 <= self.price <= 30):
            raise ValueError("Price must be between 1 and 30.")

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "restaurant_id": self.restaurant_id,
            "pizza_id": self.pizza_id,
            "pizza": self.pizza.to_dict(),
            "restaurant": self.restaurant.to_dict()
        }
