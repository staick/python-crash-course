filename = 'learning_python.txt'

print("-----The first Times-----")
with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)

print("\n-----The second Times-----")    
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print("\n-----The Third Times-----")
for line in lines:
    print(line.strip())
