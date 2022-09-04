import json


filename = 'favorite_number.json'

favorite_num = input("Please enter your favorite number: ")

with open(filename, 'w') as f:
    json.dump(favorite_num, f)
