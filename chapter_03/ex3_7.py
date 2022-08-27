from sre_constants import GROUPREF


guests = ['Staick', 'Harry', 'Peter']
old_guest = 'Harry'
new_guest = 'Jack'

print(f'I will have a party, I invite {guests[0]}, {guests[1]}, {guests[2]}.')
print(f'But {old_guest} can not present.')
guests.remove(old_guest)
guests.append(new_guest)
print(f'So, I will invite {guests[0]}, {guests[1]}, {guests[2]}.')

print('I find a larger table.')

guests.insert(0, 'Mary')
guests.insert(2, 'Jason')
guests.append('Mike')
print(f'Now, I will invite {guests[0]}, {guests[1]}, {guests[2]}, {guests[3]}, {guests[4]}, {guests[5]}.')

print('I am sorry to say that the new table I bought can not reach in time.')

del_guest = guests.pop()
print(f'I am sorry, {del_guest}.')
del_guest = guests.pop()
print(f'I am sorry, {del_guest}.')
del_guest = guests.pop()
print(f'I am sorry, {del_guest}.')
del_guest = guests.pop()
print(f'I am sorry, {del_guest}.')

print(f'I will invite {guests[0]}, {guests[1]}.')
del guests[0]
del guests[0]
print(guests)