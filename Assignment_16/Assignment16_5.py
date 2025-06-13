def main():
    f = open("Student.txt","r")
    alllines =f.readlines()
    print(alllines)
    for line in alllines:
        if sum(len(i.split()) for i in line) >=5 :
            print(line)

main()