number_of_items = int(input("Number of items: "))
total_cost = 0
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items, 0, -1):
    price_of_item = float(input("Price of item: "))
    total_cost += price_of_item
if total_cost > 100:
    total_cost = round(total_cost * 0.9, 2)
print("Total price for", number_of_items, "items is $", total_cost)
