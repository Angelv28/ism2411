# Reflection
# 1. What suprised me the most about how lists work is how easy it is to manipulate them. I was surprised that you can add, remove, and sort items in a list with just a few lines of code.
# 2. I haven't used excel yet to complete any assignments, although I am familiar with it from using it to play around with during high school. However I think a python list might be more useful for me because I can manipulate the data in a more efficient way and I can use it to do calculations and analysis that would be more difficult to do in excel.


# Exercise 1 
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print(inventory[0], inventory[-1], inventory[2])

# Exercise 3
print(inventory[0:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
cords = (40.7128, -74.0060)
try:
    cords[0] = 99
except TypeError:
    print("Tuples are unchangeable/inmutable. This is useful for storing data that should not be changed, like coordinates.")
print(cords)

# Exercise 6
sales = [100, 250, 75, 480, 200]
print(f"total : {sum(sales)}")
print(f"count : {len(sales)}")
print(f"average : {sum(sales) / len(sales)}")
print(f"best day : {max(sales)}")
print(f"worst day : {min(sales)}")

# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted_price = f"{price * 0.9:.2f}"
    discounted.append(discounted_price)
print(f"original : {prices}")
print(f"discounted : {discounted}")

# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for sale in sales:
    if sale > 300:
        high_sales.append(sale)
print(f"High sales: {high_sales}")
print(f"Count : {len(high_sales)}")
print(f"Avg : {sum(high_sales) / len(high_sales):.2f}")
