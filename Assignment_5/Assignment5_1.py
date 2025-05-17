add = lambda a,b : a + b
diff = lambda a,b : a - b
mul = lambda a,b : a*b
div = lambda a,b : a/b

def main():
    print("please enter first number : ")
    num1 = int(input())

    print("please enter second number : ")
    num2 = int(input())

    sans = add(num1,num2)
    print("Addition is : ",sans)

    sans = diff(num1, num2)
    print("Addition is : ", sans)

    sans = mul(num1, num2)
    print("Addition is : ", sans)

    sans = div(num1, num2)
    print("Addition is : ", sans)


if __name__ == "__main__":
    main()