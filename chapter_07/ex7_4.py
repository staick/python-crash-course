# 7-4. Pizza Toppings
active = True
message = '\nEnter the topping you want to add on the pizza: '

while active:
    topping = input(message)
    if topping == 'quit':
        active = False
    else:
        print("Add topping to the pizza.")