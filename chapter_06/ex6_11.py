# 6-11. Cities
cities = {
    'Beijing': {
        'country': 'China',
        'population': '20',
        'fact': 'big',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '10',
        'fact': 'beautiful',
    },
    'New York': {
        'country': 'American',
        'population': '15',
        'fact': 'busy',
    },
}

for city, info in cities.items():
    print(
        f"The {city} is in {info['country']}, There are {info['population']} people, It's very {info['fact']}.")
