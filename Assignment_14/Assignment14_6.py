class Calculator:
    def add(self,a,b):
        return a + b

    def subtract(self,a,b):
        return a - b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a/b

    def main(self):
        val1 = int(input("please enter a first value : "))
        val2 = int(input("please enter a second value : "))
        op = input("please enter a operation")
        if op == "add":
            a = self.add(val1,val2)
            print(a)
        elif op == "subtract":
            a = self.subtract(val1,val2)
            print(a)
        elif op == "mul":
            a = self.mul(val1,val2)
            print(a)
        else:
            a = self.div(val1,val2)
            print(a)

if __name__ == "__main__":
    obj = Calculator()
    obj.main()
