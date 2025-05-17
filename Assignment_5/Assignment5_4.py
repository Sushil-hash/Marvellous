print("print 1st number")
no1 = int(input())

print("print 2nd number")
no2 = int(input())

print("print 3rd number")
no3 = int(input())

if no1 > no2 and no1 > no3:
    print("largest number is : ", no1)
elif no2 > no1 and no2 > no3 :
    print("largest number is : ", no2)
else:
    print("largest number is : ", no3)