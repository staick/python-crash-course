filename = 'guest_book.txt'

while True:
    user_name = input("Enter your name: ")
    print(f"Welcome to here, {user_name}.")
    with open(filename, 'a') as file_object:
        file_object.write(f"{user_name}\n")
