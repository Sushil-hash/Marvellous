class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self):
        print("existing balance : ", self.balance)
        deposit_amount = int(input("enter the amount you want to deposit"))
        self.balance = self.balance + deposit_amount
        print("Balance after deposit : ",self.balance)

    def withdraw(self):
        print("existing balance : ", self.balance)
        withdraw_amount = int(input("enter the amount you want to withdraw"))
        self.balance = self.balance - withdraw_amount
        print("Balance after withdraw : ", self.balance)

    def main(self):
        self.deposit()
        self.withdraw()

if __name__ == "__main__":
    obj = BankAccount("Sushil", 111, 1000)
    obj.main()
