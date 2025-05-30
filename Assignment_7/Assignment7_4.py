no = int(input("please enter count of number of elements : "))
data = []
for i in range(1,no+1):
    data.append(int(input(f"please enter {i} element : ")))

from functools import reduce
res = reduce(lambda a,b : a*b,data)
print(res)