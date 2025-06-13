class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def calculate(self):
        area =  self.width * self.length
        print(area)
        perimeter = 2 * (self.width + self.length)
        print(perimeter)

    def main(self):
        self.calculate()

if __name__ == "__main__":
    obj = Rectangle(5,4)
    obj.main()