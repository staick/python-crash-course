# 9-1. Restaurant
class Restaurant:
    """model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"The name of the restaurant is {self.restaurant_name}, and the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print("Welcome to the restaurant!")


restaurant = Restaurant("KFC", "quick food")
restaurant.describe_restaurant()
restaurant.open_restaurant()
