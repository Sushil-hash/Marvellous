def main():
    filename = input("please enter a file name : ")
    f = open(filename,"r")
    fcontent = f.read()
    st = input("please enter the string you want to find : ")
    frequency = fcontent.count(st)
    print("Frequency of the given word is : ",frequency)
if __name__ == "__main__":
    main()