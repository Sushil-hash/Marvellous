class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def d(self):
        print("in parent class")


class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.subject)
        print(self.age)
        print(self.salary)
        self.d()

if __name__ == "__main__":
    obj = Teacher("abc",5,"maths",10000)
    obj.display()

