print("enter number of elements")
ele  = int(input())
data = []
for i in range(ele):
    print("please enter ",i+1,"th element")
    t = int(input())
    data.append(t)

fdata = list(filter(lambda a: a % 2 ==0, data))
mdata = list(map(lambda a : a*a , fdata))
from functools import reduce
rdata = reduce(lambda a,b:a+b,mdata)

print("final product is : ", rdata)
