"""
i have created three variables for inputs and three for formatted lines 
with the variables and printed out them.
"""
product = 'Laptop'
price = 75000.5
discount = 10

f_string = f"Product: {product} | Price: {price:.2f} | Discount: {discount}%"
print("f-string style:", f_string)

format = "Product: {} | Price: {:.2f} | Discount: {}%".format(product, price, discount)
print(".format() style:", format)

percent = "Product: %s | Price: %.2f | Discount: %d%%" % (product, price, discount)
print("% operator style:", percent)