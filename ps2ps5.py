print("Users's last name")
lastName = input()
print("Enter the number of dependents")
nod = int(input())
print("Enter gross income")
gi = float(input())
gi = gi - nod * 12000
ag = int(input())
if gi >= 50000:
    gi = 0.2
else:
    gi = 0.1
print("Last Name:" + lastName + "number of dependents:" + str(nod) + "adjusted gross income:" + str(ag) + "Income tax:" + str(100))
