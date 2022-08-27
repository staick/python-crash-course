guests = ['Staick', 'Harry', 'Peter']
old_guest = 'Harry'
new_guest = 'Jack'

print(f'I will have a party, I invite {guests[0]}, {guests[1]}, {guests[2]}.')
print(f'But {old_guest} can not present.')
guests.remove(old_guest)
guests.append(new_guest)
print(f'So, I will invite {guests[0]}, {guests[1]}, {guests[2]}.')