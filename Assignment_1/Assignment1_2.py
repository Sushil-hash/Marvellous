def ChkNum(number):
    if number % 2 == 0:
        print("This is even number")
    else:
        print("This is odd number")

def main():
    print("Please enter a number")
    number = int(input())
    ChkNum(number)

if __name__ == "__main__":
    main()