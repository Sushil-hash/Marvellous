no = 2
power = 3
mul = 1
# while (power >=1):
#     mul = mul * no
#     power = power -1
# print(mul)

def powerx():
    global power
    global mul
    if power >=1:
        mul = mul * no
        power = power -1
        powerx()

powerx()
print(mul)