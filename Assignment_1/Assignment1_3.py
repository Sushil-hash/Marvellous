
def Add(number1,number2):
    answer = number1 + number2
    return answer
def main():
    print("Please enter first number")
    number1 = int(input())

    print("Please enter second number")
    number2 = int(input())

    addition = Add(number1,number2)
    print("Addition is : ",addition)

if __name__ == "__main__":
    main()