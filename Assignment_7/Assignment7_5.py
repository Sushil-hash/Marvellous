word = input("Please enter a string : ")
flag = True
for i in range(len(word)):
    if word[i] != word[-(i+1)]:
        flag = False
if flag:
    print("Palindrome")
else:
    print("Not a palindrome")