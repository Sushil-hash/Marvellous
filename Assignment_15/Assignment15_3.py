import sys
def main():
    file1 = sys.argv[1]
    fobj1 = open(file1,"r")
    file1_content = fobj1.read()
    fobj2 = open("Demo.txt","w")
    fobj2.write(file1_content)

if __name__ == "__main__":
    main()