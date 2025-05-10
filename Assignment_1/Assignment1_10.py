def calculatelength(name):
    ans = len(name)
    return(ans)

def main():
    print("Please enter a name")
    name = str(input())
    ans = calculatelength(name)
    print("Length of the name is : ", ans)
if __name__ == "__main__" :
    main()