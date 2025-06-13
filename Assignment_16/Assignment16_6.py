def main():
    file1 = open("Student.txt","r")
    file1_content = file1.read()
    file2 = open("marks.txt", "w")
    file2.write(file1_content)

main()