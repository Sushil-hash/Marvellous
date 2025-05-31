digit = 1234
l_digit = list(str(digit))
sum = 0
digit_len = len(l_digit)
fd = digit_len - 1
# for i in l_digit:
#     sum = sum + int(i)
# print(sum)

# while(fd >= 0):
#     sum = sum + int(l_digit[fd])
#     fd = fd - 1
# print(sum)

def add_digit():
    global sum
    global fd
    if (fd >= 0):
        sum = sum + int(l_digit[fd])
        fd = fd -1
        add_digit()

add_digit()
print(sum)
