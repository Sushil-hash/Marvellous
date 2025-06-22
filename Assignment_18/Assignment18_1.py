import os

file = input("Enter the file name you want to check")
res = os.path.exists(file)
if res:
    print("File exists")
else:
    print("File does not exists")