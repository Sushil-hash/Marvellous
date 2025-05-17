import MarvellousNum

print("enter number of elements")
ele  = int(input())
fl = []
for i in range(ele):
    print("please enter ",i+1,"th element")
    t = int(input())
    fl.append(t)


def listprime(fl):
    fadd = 0
    for i in fl:
        if MarvellousNum.chkprime(i):
            print("Prime number : ", i)
            fadd = fadd + i
    print("Addition of all prime numbers is :", fadd)

listprime(fl)