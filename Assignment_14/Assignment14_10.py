class Employee:
    def __init__(self,name,dep,salary):
        self.name = name
        self._department = dep
        self.__salary = salary

obj = Employee("abc","IT",10000)
print(obj.name)
print(obj._department) #not recommended
print(obj._Employee__salary)  #name mangling