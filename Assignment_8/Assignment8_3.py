import threading

def evenlistadd(l1):
    sum = 0
    for i in l1:
        if i % 2 == 0:
           sum = sum + i
    print("Addition of even element is : ", sum)

def oddlistadd(l2):
    sum = 0
    for i in l2:
        if i % 2 != 0:
            sum = sum + i
    print("Addition of odd element is : ", sum)

def main():
    print("Please enter a number of elements : ")
    lec = int(input())
    lecl = []
    for i in range(lec):
        print("please enter ",i,"th element : ")
        t = int(input())
        lecl.append(t)
    print(lecl)
    T1 = threading.Thread(target = evenlistadd, args=[(lecl)])
    T1.start()
    T1.join()

    print("Please enter a number of elements : ")
    lec2 = int(input())
    lecl2 = []
    for i in range(lec2):
        print("please enter ", i, "th element : ")
        t = int(input())
        lecl2.append(t)
    T1 = threading.Thread(target = oddlistadd, args=(lecl2,))
    T1.start()
    T1.join()

if __name__ == "__main__":
    main()