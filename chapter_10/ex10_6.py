try:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
except ValueError:
    print("Please enter a number.")
else:
    result = num_1 + num_2
    print(f"The result is {result}.")
