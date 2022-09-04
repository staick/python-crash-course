filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    num_the = contents.lower().count('the')
    print(f"The 'the' appears {num_the} times.")
