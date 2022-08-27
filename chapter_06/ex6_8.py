# 6-8. Pets
pet_0 = {
    'animal': 'dog',
    'owner': 'Harry',
}
pet_1 = {
    'animal': 'cat',
    'owner': 'Jack',
}
pet_2 = {
    'animal': 'duck',
    'owner': 'Mary',
}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(f"It is a {pet['animal']}, it's owner is {'owner'}.")