
def prime(no):
    for i in range(2,no):
        if no % i == 0:
            return False
    return True

def main():
    cnt = int(input("please enter a count of number you want to enter : "))
    datalist = []
    for i in range(cnt):
        datalist.append(int(input(f"please enter a {i} element : ")))
    print("Original data : ",datalist)

    fdata = list(filter(prime,datalist))
    print("Data after filter : ",fdata)

    mdata = list(map(lambda no : no *2,fdata))
    print("data after map  : ",mdata )

    from functools import  reduce
    rdata = reduce(lambda a,b : a if a> b else b,mdata)
    print("final anser is  : ",rdata)

if __name__ == "__main__":
    main()