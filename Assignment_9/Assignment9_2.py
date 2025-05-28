import multiprocessing

def one(l1):
    fl1 = []
    print(l1)
    for i in l1:
        t = i**2
        print(t)
        fl1.append(t)
    print("Final list : ",fl1)


def main():
    print("please enter count of element of first list : ")
    c1 = int(input())
    l1 = []
    for i in range(c1):
        print("Please enter ",i,"th element")
        t = int(input())
        l1.append(t)

    p1 = multiprocessing.Process(target=one,args=(l1,))
    p1.start()
    p1.join()




if __name__ == "__main__":
    main()