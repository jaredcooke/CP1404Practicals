name_file = open('name.txt', 'r')
name = name_file.readline()
print('Your name is {}'.format(name))
name_file.close()
