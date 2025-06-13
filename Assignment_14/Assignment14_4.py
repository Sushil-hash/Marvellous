class Student:
    school_name = "SSC"
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(Student.school_name)
        print(self.name)
        print(self.roll_no)

    def main(self):
        self.display()
        Student.school_name = "HSC"
        self.display()

if __name__ == "__main__":
    obj = Student("Sushil",1)
    obj.main()