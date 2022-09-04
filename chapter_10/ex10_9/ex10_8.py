cat_file = 'cats.txt'
dog_file = 'dogs.txt'

try:
    with open(cat_file) as f:
        cats = f.readlines()
except FileNotFoundError:
    pass
else:
    print("There are cats: ")
    for cat in cats:
        print(f"\t{cat.strip()}")

try:
    with open(dog_file) as f:
        dogs = f.readlines()
except FileNotFoundError:
    pass
else:
    print("There are dogs: ")
    for dog in dogs:
        print(f"\t{dog.strip()}")
