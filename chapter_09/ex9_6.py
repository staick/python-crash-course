# 9-6. Ice Cream Stand
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

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 0

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand = IceCreamStand('KFC', 'ice cream')
ice_cream_stand.flavors = ['chocolate', 'cream', 'strawberry']
ice_cream_stand.display_flavors()
