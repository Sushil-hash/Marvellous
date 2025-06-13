class BookStore:
    NoOfBooks = 0
    def __init__(self):
        self.name = input("please enter name of the book : ")
        self.Author = input("please enter author of the book : ")
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def display(self):
        print(self.name + "By" + self.Author)
        print("Number of books : ", BookStore.NoOfBooks)

    def main(self):
        self.display()

if __name__ == "__main__":
    obj1 = BookStore()
    obj1.main()
    obj2 = BookStore()
    obj2.main()