#prime
# prime = lambda a : a > 1 and all(i for i in range(2,a) if a % i == 0)
# print(prime(13))

# perfect
# perfect = lambda a : (sum(i for i in range(1,a-1) if a % i == 0) == a)
# print(perfect(29))

# l = list(range(1,100))
# r = list(filter(lambda a : (sum(i for i in range(1,a-1) if a % i == 0) == a),l))
# print(r)


# factor = list(filter(lambda a : num % a ==0,range(1,num+1)))
# print(factor)
sumoffactors = lambda a : sum(i for i in range(1,a-1) if a%i == 0)
print(sumoffactors(12))