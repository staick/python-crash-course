foods = ('pizza', 'falafel', 'carrot cake', 'ice cream', 'hamburger')

print(f'We have {len(foods)} food for you: ', end='')
for food in foods:
    print(food, end=', ')

# foods[0] = 'rice'

foods = ('pizza', 'falafel', 'french fries', 'rice', 'hamburger')
print(
    f'\nWe update the food list, now we have {len(foods)} food for you: ', end='')
for food in foods:
    print(food, end=', ')
print()
