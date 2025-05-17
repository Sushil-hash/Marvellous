print("enter number of elements")
ele  = int(input())
data = []
for i in range(ele):
    print("please enter ",i+1,"th element")
    t = int(input())
    data.append(t)

fdata = list(filter(lambda a: a >1 and all(a%i!=0 for i in range(2,a-1)) , data))
mdata = list(map(lambda a : a*2 , fdata))
from functools import reduce
rdata = reduce(lambda a,b:a if a>b else b,mdata)

print("final product is : ", rdata)
