import sys

def main():
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]

    f1 = open(filename1,"r").read()
    f2 = open(filename2, "r").read()

    if f1 == f2:
        print("Content is same")
    else:
        print("content is not same")

if __name__ == "__main__":
    main()