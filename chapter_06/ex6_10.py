# 6-10. Favorite Numbers
favorite_numbers = {
    'Jack': ['1', '9'],
    'Mary': ['2', '8'],
    'Staick': ['3', '7'],
    'Json': ['4', 6],
    'Mike': ['0','5'],
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: ", end='')
    for number in numbers:
        print(number, end=' ')
    print()
