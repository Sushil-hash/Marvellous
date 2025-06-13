class BankAccount:
    ROI = 10.50
    def __init__(self):
        self.name = input("Please enter a name : ")
        self.amount = int(input("please enter a amount while creating the account : "))

    def deposit(self):
        self.amount = self.amount + int(input("please enter the amount you want to deposit : "))

    def withdraw(self):
        self.amount = self.amount - int(input("please enter the amount you want to withdraw : "))

    def calculateintrest(self):
        self.amount = self.amount + BankAccount.ROI
        print("total amount after interest  : ",self.amount)

    def display(self):
        print("Name is : ",self.name)
        print("Account balance is : ",self.amount)

    def main(self):
        self.deposit()
        self.withdraw()
        self.calculateintrest()
        self.display()

if __name__ == "__main__":
    obj = BankAccount()
    obj.main()