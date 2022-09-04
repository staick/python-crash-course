filename = 'guest.txt'

user_name = input("Enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(f"{user_name}\n")
