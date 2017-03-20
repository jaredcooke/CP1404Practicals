numbers_file = open('numbers.txt', 'r')
total = 0
for line in numbers_file:
    total += int(line)
print('The sum of numbers in the file is {}'.format(total))
