import threading
def evenfactoradd(no):
    sum  = 0
    for i in range(1,no+1):
        if i % 2 == 0:
            sum = sum + i
    print("Addition of even factors is : ",sum )

def oddfactoradd(no):
    sum = 0
    for i in range(1, no + 1):
        if i % 2 != 0:
            sum = sum + i
    print("Addition of odd factors is : ", sum)

def main():
    print("please enter a number : ")
    no1 = int(input())
    T1 = threading.Thread(target=evenfactoradd,args=(no1,))
    T1.start()
    T1.join()

    print("please enter a number : ")
    no2 = int(input())
    T2 = threading.Thread(target=oddfactoradd,args=(no2,))
    T2.start()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()



