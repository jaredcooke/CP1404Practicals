name_file = open('name.txt', 'w')
name = input('What is your name? ')
print(name, file=name_file)
name_file.close()
