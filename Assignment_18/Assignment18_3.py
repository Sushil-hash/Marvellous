import sys
file1 = sys.argv[1]
file2 = "Demo.txt"

f1obj = open(file1,"r")
f1content = f1obj.read()
f1obj.close()

f2obj = open(file2,"w")
f2obj.write(f1content)
f2obj.close()