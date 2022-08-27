pizzas = ['pepperoni', 'Chicago-Style', 'California-style']
friend_pizzas = pizzas[:]

pizzas.append('NewYork-Style')
friend_pizzas.append('others')

print('My favorite pizzas are: ', end='')
for pizza in pizzas:
    print(pizza, end=' ')

print("\nMy friend's favorite pizzas are: ", end='')
for pizza in friend_pizzas:
    print(pizza, end=' ')
print()
