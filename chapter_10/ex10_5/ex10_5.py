filename = 'programming_poll.txt'

while True:
    reason = input("Enter the reason why you like programming: ")
    with open(filename, 'a') as file_object:
        file_object.write(f"{reason}\n")
