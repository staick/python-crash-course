# 6-5 Rivers
from itertools import count


rivers = {'nile': 'egypt', 'yellow river': 'china', 'ganges river': 'india'}

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())