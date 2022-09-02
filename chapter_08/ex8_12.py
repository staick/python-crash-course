# 8-12. Sandwiches
def make_pizza(*args):
    for arg in args:
        print(arg, end=' ')
    print()

make_pizza('mushroom')
make_pizza('mushroom', 'pineappble', 'apple')
make_pizza('apple', 'orange')
