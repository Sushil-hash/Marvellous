no = int(input("please enter a number : "))
flag =  True
for i in range(2,round(no/2)):
    if no % i == 0:
        flag = False
if flag :
    print("Prime Number")
else:
    print("Not a prime number")
