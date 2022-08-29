# 7.5. Movie Tickets
message = 'Please enter your age:'

while True:
    age = input(message)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The ticket is free.")
    elif age < 12:
        print("The price is $10.")
    elif age > 12:
        print("The price is $15.")
