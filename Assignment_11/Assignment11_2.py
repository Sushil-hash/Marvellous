# mul = 1
# no = 5
# while(no >= 1):
#     mul =  mul * no
#     no = no -1
# print(mul)

mul = 1
no = 5
def factorial():
    global no
    global mul
    if no >= 1:
        mul = mul * no
        no = no - 1
        factorial()

factorial()
print(mul)