print("Enter the number of books ordered.")
books = int(input())
print("What is the cost per book")
cost = int(input())
totalCost = books * cost
if cost >= 50.0:
    cost = 25
else:
    shipping = 0
print("Cost per book: " + str(cost) + " number of books: " + str(books) + " Shipping cost: " + str(shipping) + " Total cost:" + str(totalCost + shipping), end='', flush=True)
