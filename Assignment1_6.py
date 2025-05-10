
def chknum(number):
    if number > 0 :
        print("Number is positive")
    elif number == 0:
        print("number is zero")
    else:
        print("Number is negative")

def main():
    print("please enter a number")
    number = int(input())
    chknum(number)

if __name__ == "__main__" :
    main()
