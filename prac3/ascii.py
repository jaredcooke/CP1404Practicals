def main():
    UPPER_LIMIT = 127
    LOWER_LIMIT = 33
    number = get_number(UPPER_LIMIT, LOWER_LIMIT)
    print('The character for {} is {}'.format(number, chr(number)))


def get_number(upper, lower):
    finished = False
    while not finished:
        try:
            number = int(input('Enter a number ({} - {}): '.format(lower, upper)))
            if lower <= number <= upper:
                return number
            else:
                print('Please enter a valid number')
        except ValueError:
            print('Please enter a number')


main()
