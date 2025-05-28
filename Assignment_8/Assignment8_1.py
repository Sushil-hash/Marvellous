import threading
def even():
    print("in even")
    cnt = 0
    for i in range(100):
        if i % 2 == 0 and cnt <= 10:
            cnt = cnt + 1
            print(i)

def odd():
    cnt = 0
    for i in range(100):
        if i % 2 != 0 and cnt <= 10:
            cnt = cnt + 1
            print(i)

def main():
    T1 = threading.Thread(target=even)
    T1.start()
    T1.join()

    T2 = threading.Thread(target=odd)
    T2.start()
    T2.join()

if __name__ == "__main__":
    main()



