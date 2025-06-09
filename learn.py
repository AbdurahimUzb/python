item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many would you like?"))

total = price * quantity
print(f"The total cost for {quantity} {item}(s) is ${total:.2f}.")
