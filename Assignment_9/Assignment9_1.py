import threading
import time
def t1():
    for i in range(6):
        print(i)

def main():
    T1 = threading.Thread(target=t1)
    T1.start()
    T1.join()
    time.sleep(1)

    T2 = threading.Thread(target=t1)
    T2.start()
    T2.join()
    time.sleep(1)

    T3 = threading.Thread(target=t1)
    T3.start()
    T3.join()
    time.sleep(1)


if __name__ == "__main__":
    main()