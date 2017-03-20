sales = float(input("Enter Sales: $"))
while sales <= 0:
    print("Invalid number")
    sales = float(input("Enter Sales: $"))
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
    print("Bonus = ${:.2f}".format(bonus))
