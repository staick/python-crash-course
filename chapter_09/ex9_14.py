from random import choice

test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
tickets=[]
for num in range(4):
    tickets.append(choice(test_list))

print(f"Any ticket matching the following four numbers or letters wins a prize:")
for ticket in tickets:
    print(ticket, end=' ')
