print("please enter number")
num = int(input())
for i in range(1,num+1):
    for j in range(i):
        print(j+1, end=" ")
    print()