print("enter number of elements")
ele  = int(input())
fl = []
for i in range(ele):
    print("please enter ",i+1,"th element")
    t = int(input())
    fl.append(t)
# def maximum(a,b):
#     if a > b:
#         return a
#     else :
#         return b
#
# first_element = 0
# for i in fl:
#     fans = maximum(first_element,i)
#
# print("maximumn value is : ",fans)
from functools import reduce
fans = reduce(lambda a,b : a if a>b else b, fl)
print("maximumn value is : ",fans)