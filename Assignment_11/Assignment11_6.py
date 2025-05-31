no = 5
sum =  0
# while (no >= 1):
#     sum = sum + no
#     no =  no -1
# print(sum)

def natural_num_addition():
    global sum
    global no
    if no >= 1:
        sum = sum + no
        no = no-1
        natural_num_addition()

natural_num_addition()
print(sum)