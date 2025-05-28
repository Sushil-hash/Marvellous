
def main():
    cnt = int(input("please enter count of number of elements you want to enter : "))
    datalist = []
    for i in range(cnt):
        datalist.append(int(input(f"please enter {i} element")))
    print("0riginal data : ",datalist)

    fdata = list(filter(lambda no : no % 2 == 0,datalist))
    print("Data after filter : ",fdata)

    mdata = list(map(lambda no : no ** 2,fdata))
    print("Data after map : ",mdata)

    from functools import reduce
    rdata = reduce(lambda no1,no2 : no1 + no2,mdata)
    print(rdata)

if __name__ == "__main__":
    main()