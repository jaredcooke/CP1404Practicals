valid_input = False
while not valid_input:
    try:
        age = int(input('Please input age: '))
        if age < 0:
            print('Please enter a valid number')
        else:
            valid_input = True
    except ValueError:
        print('Please enter a number')

if age % 2 == 0:
    print('{} is even'.format(age))
else:
    print('{} is odd'.format(age))
