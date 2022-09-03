# 9-4. Number Serverd
class Restaurant:
    """model a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(
            f"The name of the restaurant is {self.restaurant_name}, and the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print("Welcome to the restaurant!")

    def set_number_served(self, number):
        """set the number of customers that have been served"""
        self.number_served = number

    def increment_number_served(self, increment):
        """increment the number of customers that have been served"""
        self.number_served += increment


restaurant = Restaurant("KFC", "quick food")
print(f"The restaurant has served {restaurant.number_served} people.")
restaurant.number_served = 10
print(f"Now, the restaurant has served {restaurant.number_served} people.")

restaurant.set_number_served(20)
print(f"After setting, the restaurant has served {restaurant.number_served} people.")

restaurant.increment_number_served(10)
print(f"After incrementing, the restaurant has served {restaurant.number_served} people.")
