def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C" or choice == "F":
            temp = convert_temp(choice)
            print('{:.2f} {}'.format(temp[0], temp[1]))
        else:
            print('Invalid Option!')
        print(MENU)
        choice = input(">>> ").upper()


def convert_temp(choice):
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        return [fahrenheit, 'F']
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        return [celsius, 'C']

main()