def main():
    file = open("marks.txt","r")
    data = file.readlines()
    for line in data:
        name = line.split(" ")[0]
        marks = int(line.split(" ")[1])
        if marks > 75:
            print(name)

main()