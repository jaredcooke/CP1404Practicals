def main():
    name = get_name()
    string = get_string(name)
    print(string)


def get_name():
    name = input('What is your name? ')
    while not name.strip():
        name = input('Please enter your name: ')
    return name


def get_string(string):
    frequency = int(input('frequency: '))
    s = ''
    for i in range(0, len(string), frequency):
        if i % frequency == 0:
            s += string[i]
    return s


main()