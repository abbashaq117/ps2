print("Enter the cost of an appliance")
cost = int(input())
print("Enter the name of the appliance")
appliance = input()
if cost >= 1000:
    warrantee = 0.1
else:
    warrantee = 0.05
print("Cost of application: " + str(cost) + ", Type of appliance: " + appliance + ", Warranty price: " + str(cost * warrantee) + ", Total cost: " + str(warrantee * cost + cost))
