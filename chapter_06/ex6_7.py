# 6-7. People
people_0 = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': '24',
    'city': 'Hogwarts',
}
people_1 = {
    'first_name': 'Linus',
    'last_name': 'Torvalds',
    'age': '30',
    'city': 'Linux',
}
people_2 = {
    'first_name': 'Michael',
    'last_name': 'Jackson',
    'age': '18',
    'city': 'New York',
}
peoples = [people_0, people_1, people_2]

for people in peoples:
    print(
        f"My name is {people['first_name']} {people['last_name']},I am {people['age']} and I am from {people['city']}.")
