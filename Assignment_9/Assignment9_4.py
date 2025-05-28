import multiprocessing
import threading
import time

def seq():
    fans = 0
    for i in range(1000000+1):
        fans = fans + i
    return fans

def madd(l):
    fans = 0
    for i in range(len(l)):
        fans = fans + i
    print("Addition is : ",fans)

def main():
    print("starting sequential execution")
    stime = time.time()
    ans = seq()
    print("Addition is : ", ans)
    etime = time.time()
    print("Total time taken for sequential execution : ",etime-stime)

    ldata = []
    for i in range(1000000+1):
        ldata.append(i)

    print("starting threading execution")
    t1 = threading.Thread(target=madd,args=(ldata,))
    sstime = time.time()
    t1.start()
    t1.join()
    eetime= time.time()
    print("Total time taken for threading execution : ", eetime - sstime)

    print("starting multiprocessing execution")
    p1 = multiprocessing.Process(target=madd,args=(ldata,))
    sstime = time.time()
    p1.start()
    p1.join()
    eetime = time.time()
    print("Total time taken for multiprocessing execution : ", eetime - sstime)

if __name__ == "__main__":
    main()
