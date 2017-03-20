import random
got_number = False
while not got_number:
    try:
        number_of_quick_picks = int(input('How many quick picks? '))
        if number_of_quick_picks <= 0:
            print("Please enter a valid number")
        else:
            got_number = True
    except ValueError:
        print("Please enter a number")

for i in range (0, number_of_quick_picks):
    numbers = []
    for j in range(0, 6):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number)
    numbers.sort()
    print("{:3} {:3} {:3} {:3} {:3} {:3}".format(numbers[0], numbers[1], numbers[2], numbers[3], numbers[4], numbers[5]))
