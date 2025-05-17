print("enter number of elements")
ele  = int(input())
fl = []
for i in range(ele):
    print("please enter ",i+1,"th element")
    t = int(input())
    fl.append(t)

print("enter another number")
at = int(input())

def sn(fl,at):
    counter = 0
    for i in fl:
        if i == at:
            counter = counter + 1
    return counter

fans = sn(fl,at)

# fans = list(filter(lambda fl,at: cnt =0; ))

print("frequency of the given number is  : ", fans)