total = 0
number = int(input("Number of Items"))
while number < 0:
    print("Invalid number of Items!")
    number = int(input("Number of Items"))
for i in range(number):
    price = float(input("Price of Item:"))
    total += price
if total > 100:
    total *= 0.9
print("Total Price for {} items is ${:.2f}".format(number, total))

