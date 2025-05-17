#factors - adition of all the divisible values
print("Please enter the number")
a = int(input())
ad = 0
fans = []
for i in range(a):
    if i != 0 and a % i == 0:
        ad = ad + i
        fans.append(i)
print(fans)
print(ad)


