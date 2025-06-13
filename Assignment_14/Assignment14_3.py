class Book:
    def __init__(self):
        self.__price = 0

    def set_price(self):
        p = int(input("please enter the price"))
        self.__price = p

    def get_price(self):
        print(self.__price)

    def main(self):
        self.set_price()
        self.get_price()

if __name__ == "__main__":
    obj = Book()
    obj.main()