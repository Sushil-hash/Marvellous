import multiprocessing

def factorial(no):
    tno = 1
    if no != 0 and no > 0:
        for i in range(no,1,-1):
            tno = i * tno
    else:
        print("please give the positive number")
    return tno

def main():
    print("please enter a number of elements : ")
    cnt = int(input())
    l = []
    print("please enter a values")
    for i in range(cnt):
        # print("please enter a ",i,"th number : ")
        # t = int(input())
        l.append(int(input()))
    result = multiprocessing.Pool().p1.map(factorial,l)
    print(result)

if __name__ == "__main__":
    main()