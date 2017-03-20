character = input('Enter a characer: ')
print('The ASCII code for {} is {}'.format(character, ord(character)))
UPPER_LIMIT = 127
LOWER_LIMIT = 33
number = int(input('Enter a number between {} and {}: '.format(LOWER_LIMIT, UPPER_LIMIT)))
while number < LOWER_LIMIT or number > UPPER_LIMIT:
    print('Invalid number. Please enter a number between {} and {}'.format(LOWER_LIMIT, UPPER_LIMIT))
    number = int(input('Enter a number between {} and {}: '.format(LOWER_LIMIT, UPPER_LIMIT)))
print('The character for {} is {}'.format(number, chr(number)))



for i in range(33, 128, 1):
    print('{:3} {:>6}'.format(i, chr(i)))
