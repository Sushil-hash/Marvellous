class Demo:
    value = 0;
    def __init__(self, no1, no2):
        self.no1 = no1
        self.no2 = no2

    def fun(self):
        print(self.no1)
        print(self.no2)

    def gun(self):
        print(self.no1)
        print(self.no2)

    def main(self):
        self.fun()
        self.gun()

if __name__ == "__main__":
    obj1 = Demo(10, 11)
    obj1.main()
    obj2 = Demo(20, 21)
    obj2.main()