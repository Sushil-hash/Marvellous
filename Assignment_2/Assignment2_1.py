import Arithmatic as A

print("Enter the first number")
a = int(input())

print("Enter the second number")
b = int(input())

aans = A.Addition(a,b)
print("Addition is : ",aans)

sans = A.Subtraction(a,b)
print("Subtraction is : ",sans)

mans = A.Multiplication(a,b)
print("Multiplication is : ", mans)

dans = A.Division(a,b)
print("Division is : ", dans)
