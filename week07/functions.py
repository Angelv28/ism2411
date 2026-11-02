#DISCOLSURE: I used Microsoft Copilot to help me write the code in this file. I did not use any other sources for this assignment.
# Self Assesment 
# 1. In exercise 5, I found the bug after running the code in terminal and after the error message of a missing colon, I added the colon to the for loop.
# 2. apply_discount(price, tier) is a function that calculates the discounted price of a sale after applying an tier discount or no discount at all if not eligible. Its inputs are the price and the tier of the customer. It returns a new price after looking at the tier and applying the corresponding discount. A colleague can probably use the code without reading the bodyas they just  input the price and tier of the customer to get the result of the function.
# 3. I used AI to build my understanding of debugging in exercise 5. It helped me understand the error messages and how to fix them.
# Exercise 1
def calculate_total(price, rate):
    return price + (price * rate)


print(f"Taxed price: ${calculate_total(100, 0.07):.2f}")
print(f"Taxed price: ${calculate_total(250, 0.08):.2f}")

# Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
print(f"Discount price: ${apply_discount(200, 'gold'):.2f}")
print(f"Discount price: ${apply_discount(200, 'silver'):.2f}")
print(f"Discount price: ${apply_discount(200, 'bronze'):.2f}")
print(f"Discount price: ${apply_discount(200, 'none'):.2f}")

# Exercise 3
def final_price(price, tier, rate):
    discounted_price = apply_discount(price, tier)
    return calculate_total(discounted_price, rate)

discounted_price = apply_discount(200, "gold")
print(f"After discount: ${discounted_price:.2f}")
print(f"After tax: ${calculate_total(discounted_price, 0.07):.2f}")
print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

#Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale  # total isnt adding the sales, it is just being overwritten each time. Gotta add a plus sign to add the sales.
print(f"Total: ${total}")

count = 0
for sale in sales: # must add a colon at the end of the for loop
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i]) # must use < instead of <= to avoid index out of bounds
    i += 1
# Exercise 6 
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here? -- 100 or x prints here
print(double_it()) # what prints here? -- 1998 prints here as x is now 999 for this function
print(x)           # has x changed? -- X stays the same as the first one, because 999 is only used in the function "double_it" 
# scope in coding is the context in which a variable is defined. A variable inside of a function is local to that function and can't be accesed outside of it. A variable outside of a function is global and can be accessed throuhgout the program.