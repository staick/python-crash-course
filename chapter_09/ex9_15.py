# 9-15. Lottery Analysis
from random import choice

test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
tickets=[]
for num in range(4):
    tickets.append(choice(test_list))

my_ticket = [1, 1, 1, 1]

count = 0
while my_ticket != tickets:
    tickets=[]
    for num in range(4):
        tickets.append(choice(test_list))
    count += 1

print(f"It has ran {count} times.")
