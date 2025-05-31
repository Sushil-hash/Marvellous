# cnt = 1
# while (cnt<=5):
#     print(cnt)
#     cnt = cnt + 1

cnt = 1
def printnumber():
    global cnt
    if (cnt<=5):
        print(cnt)
        cnt = cnt + 1
        printnumber()

printnumber()