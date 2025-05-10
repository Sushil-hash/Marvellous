def ChkNum(number):
    bool_val = True
    if number % 5 == 0:
        pass
    else:
        bool_val = False
    return bool_val

def main():
    print("please enter a number")
    number = int(input())
    ans = ChkNum(number)
    print("Number is divided by 5, answer is : ", ans)

if __name__ == "__main__":
    main()