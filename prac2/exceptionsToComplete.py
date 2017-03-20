finished = False
result = 0
while not finished:
    try:
        number = int(input('Please input an integer: '))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)