name = 'Staick'
print(f"Is the name Staick? {name == 'Staick'}.")
print(f"Is the name Harry? {name == 'Harry'}.")

print(f"Is it a new user name? {name.lower() != 'staick'}")

age = 20
print(f'Is he 20? {age == 20}.')
print(f"Is he 20? {age != 20}.")
print(f"Is he older than 18? {age > 18}.")
print(f'Is he younger than 18? {age < 18}.')
print(f"Is he older than 18(include 18)? {age >= 18}.")
print(f"Is he younger than 18(include 18)? {age <= 18}.")

score = 100
print(f"Does he get a 'A'? {score > 90 and score <= 100}.")
print(f"Is it a surprising score? {score == 100 or score == 0}.")

odd = list(range(1, 10, 2))
print(f'Is 1 an odd? {1 in odd}.')
print(f"Isn't 2 an odd? {2 not in odd}.")