file = input("Enter the filename : ")
fobj = open(file,"r")
content = fobj.read()
print(content)