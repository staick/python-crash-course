# 7-6. Three Exits
active = True
message = 'Please enter your age: '

while active:
    age = input(message)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age < 12:
            print("The price is $10.")
        elif age > 12:
            print("The price is $15.")