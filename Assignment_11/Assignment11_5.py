no = 1020300
no_list = list(str(no))
no_len = len(list(str(no))) - 1
zero_count = 0
# while(no_len >= 0):
#     if int(no_list[no_len]) == 0:
#         zero_count = zero_count + 1
#     no_len = no_len - 1
# print(zero_count)

def zero_count_fuc():
    global no_len
    global zero_count
    if no_len > 0:
        if int(no_list[no_len]) == 0:
            zero_count = zero_count + 1
        no_len = no_len - 1
        zero_count_fuc()

zero_count_fuc()
print(zero_count)