favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# People who should take the poll
peoples = ['jen', 'sarah', 'staick', 'harry']

for people in peoples:
    if people in favorite_languages.keys():
        print(f'Thanks for your responding, {people.title()}.')
    else:
        print(f'{people.title()}, could you please take a poll?')
