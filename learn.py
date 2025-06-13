item = input("What item woukld you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity

print(f"You have purchased {quantity} {item}(s) at a price of ${price:.2f} each for a total of ${total:.2f}.")