no = 4
cnt = 1
# while(cnt <=  no):
#     jcnt = 0
#     while(jcnt < cnt):
#         print("*",end=" ")
#         jcnt = jcnt + 1
#     cnt = cnt + 1
#     print()

def pattern():
    global no
    global cnt
    if cnt <= no:
        jcnt = 0
        while (jcnt < cnt):
            print("*",end= " ")
            jcnt = jcnt + 1
        cnt = cnt +1
        print()
        pattern()

pattern()
