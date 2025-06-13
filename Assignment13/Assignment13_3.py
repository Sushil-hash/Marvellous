class Numbers:
    def __init__(self):
        self.value = int(input("please enter a number : "))

    def prime(self):
        if lambda n : n > 1 and all(n % i != 0 for i in range(2,n**0.5+1)):
            print("Number is prime number")
        else:
            print("Number is not a prime number")

    def perfect_number(self):
        add = 0
        for i in range(1,self.value):
            if self.value % i == 0:
                add = add + i
        if add == self.value:
            print("Number is perfect number")
        else:
            print("Number is not a perfect number")
        # lambda n : n> 1 and sum(i for i in range(1,self.value-1) if n % i == 0) == self.value

    def factors(self):
        factor_list = []
        for i in range(1,self.value+1):
            if self.value % i == 0:
                factor_list.append(i)
        print("factors of the number : ",factor_list)
        # return lambda n : all(i for i in range(1,n) if n % i == 0)

    def sumoffactors(self):
        sum_of_factors = 0
        for i in range(1,self.value+1):
            if self.value % i == 0:
                sum_of_factors = sum_of_factors + i
        print("Addition of the all factors of the givne number is : ",sum_of_factors)

    def main(self):
        self.prime()
        self.perfect_number()
        self.factors()
        self.sumoffactors()

if __name__ == "__main__":
    obj = Numbers()
    obj.main()
