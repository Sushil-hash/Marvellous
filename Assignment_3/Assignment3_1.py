print("enter number of elements")
ele  = int(input())
fl = []
for i in range(ele):
    print("please enter ",i+1,"th element")
    t = int(input())
    fl.append(t)
from functools import reduce
add = lambda a,b:a+b
fadd = reduce(add,fl)
print("final addition : ",fadd)