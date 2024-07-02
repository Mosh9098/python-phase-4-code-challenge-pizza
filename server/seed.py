# seed.py

from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Create restaurants
        restaurant1 = Restaurant(name="Karen's Pizza Shack", address='address1')
        restaurant2 = Restaurant(name="Sanjay's Pizza", address='address2')
        restaurant3 = Restaurant(name="Kiki's Pizza", address='address3')

        # Create pizzas
        pizza1 = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
        pizza2 = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        pizza3 = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")

        # Create RestaurantPizzas
        rp1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=1)
        rp2 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=4)
        rp3 = RestaurantPizza(restaurant=restaurant3, pizza=pizza3, price=5)

        db.session.add_all([restaurant1, restaurant2, restaurant3, pizza1, pizza2, pizza3, rp1, rp2, rp3])
        db.session.commit()

        print("Database seeded!")

if __name__ == "__main__":
    seed_database()
