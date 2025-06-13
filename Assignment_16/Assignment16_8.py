def main():
    file = open("Student.txt","r")
    data = file.readlines()
    file2 =  open("marks.txt","w")
    for line in data:
        freshline = line.replace(" ","")
        file2.write(freshline)
    file.close()
    file2.close()

main()