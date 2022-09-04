import json


filename = 'favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    favorite_num = input("Please enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(favorite_num, f)
    print("Ok, I remember it!")
else:
    print(f"Your favorite number is {number}.")
