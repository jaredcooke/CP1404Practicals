"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    incomes = []
    got_months = False
    while not got_months:
        try:
            number_of_months = int(input("How many months? "))
            if number_of_months > 0:
                got_months = True
            else:
                print('Please enter a valid number of months')
        except ValueError:
            print('Please enter a valid number of months')

    for month in range(1, number_of_months + 1):
        got_income = False
        while not got_income:
            try:
                income = float(input("Enter income for month {}: ".format(month)))
                incomes.append(income)
                got_income = True
            except ValueError:
                print("Please enter a valid income")

    print_report(incomes, number_of_months)


def print_report(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()
