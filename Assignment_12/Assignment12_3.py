class Arithmatic:
    def __init__(self):
        self.value1 , self.value2 = 0,0

    def accept(self):
        self.value1 = int(input("please enter first value : "))
        self.value2 = int(input("please enter second value : "))

    def addition(self):
        res = self.value1 + self.value2
        return res

    def subtraction(self):
        res = self.value1 - self.value2
        return res

    def multiplication(self):
        res = self.value1 * self.value2
        return res

    def division(self):
        res = self.value1 / self.value2
        return res

    def main(self):
        self.accept()
        print("Addition is : ",self.addition())
        print("Subtraction is : ",self.subtraction())
        print("Multiplication is : ",self.multiplication())
        print("Division is : ",self.division())

if __name__ == "__main__":
    obj = Arithmatic()
    obj.main()