while True: 
    try:
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))
        break
    except ValueError:
        print("Please enter a number.")

result = num_1 + num_2
print(f"The result is {result}.")
