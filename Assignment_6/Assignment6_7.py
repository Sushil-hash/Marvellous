from functools import reduce
data = []
for i in range(5):
    data.append(int(input(f"please enter {i} number : ")))

print("largest number is : ",reduce(lambda a,b : a if a>b else b,data))

