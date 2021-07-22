print("enter and item to purchase (A or B)")
item = input()
print("now enter a quantity to order")
qty = int(input())
if item == "A":
    up = 10.0
else:
    up = 20.0
extprice = qty * up
print("Item ordered: " + item)
print("Extended Price is " + str(extprice))
