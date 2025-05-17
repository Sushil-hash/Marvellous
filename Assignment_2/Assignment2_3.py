#factorial - multiplication of all the values till the value
print("Please enter the number")
a = int(input())
r = 1
for i in range(a, 0, -1):
    r = r * i
print(r)