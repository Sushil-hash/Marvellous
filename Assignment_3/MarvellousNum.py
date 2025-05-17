def chkprime(a):
    for i in range(2,a-1):
        flag = []
        if a % i != 0:
            flag.append(i)
        if len(flag) > 0:
            return True
        else:
            return False
