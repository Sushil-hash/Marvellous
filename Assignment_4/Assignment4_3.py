print("enter number of elements")
ele  = int(input())
data = []
for i in range(ele):
    print("please enter ",i+1,"th element")
    t = int(input())
    data.append(t)

fdata = list(filter(lambda a: a if a >= 70 and a <= 90 else False, data))
mdata = list(map(lambda a : a+10, fdata))
from functools import reduce
rdata = reduce(lambda a,b:a*b,mdata)

print("final product is : ", rdata)
