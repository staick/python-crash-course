number = input("Enter a number, and I'll tell you whether the number is a multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
    print("Yes, it's a multiple of 10.")
else:
    print("No, it's not a multiple of 10.")