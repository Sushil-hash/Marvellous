class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other,Product):
            return self.name == other.name and self.price == other.price
        return False

P1 =Product("abc",1)
P2 =Product("abc",1)
P3 =Product("abcd",2)

print(P1 == P2)
print(P1 == P3)
