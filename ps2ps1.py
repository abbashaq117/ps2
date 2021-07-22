tax = 0.07
print("Hello user please enter the number of items: ")
qauntity = int(input())
if qauntity <= 1000:
    price = 5
    tax = qauntity * price * tax
else:
    price = 3
    tax = qauntity * price * tax
print("price= " + str(price) + ",tax= " + str(tax) + ", qauntity= " + str(qauntity) + ", and total= " + str(qauntity * price + tax))
