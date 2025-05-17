#prime - if number is divisible by only 1 and itself
print("Please enter a number")
num = int(input())
flag = bool
print(flag)
for i in range(2,int(num/2+1)):
    if num % i == 0 :
        flag = True
    else:
        flag= False

if flag:
    print("It is not prime number")
else:
    print("It is prime number")