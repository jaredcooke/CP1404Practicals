print("Electricity Bill Estimator \n")
cents_per_kwh = float(input("Enter cents per kWh: "))
while cents_per_kwh <=0:
    print("Invalid value")
    cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))
while daily_use_kWh <=0:
    print("Invalid value")
    daily_use_kWh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))
while billing_days <=0:
    print("Invalid value")
    billing_days = int(input("Enter number of billing days: "))
estimated_bill = round(cents_per_kwh / 100 * daily_use_kWh * billing_days, 2)
print("Estimated bill: ${:.2f}".format(estimated_bill))