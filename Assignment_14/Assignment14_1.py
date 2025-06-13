class Employee:
    def __init__(self,id,name,salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print("Name : ",self.name,"ID : ",self.id,"Salar : ",self.salary)

    def main(self):
        self.display()

if __name__ == "__main__":
    obj = Employee(1,"Rohit",50000)
    obj.main()