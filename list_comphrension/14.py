prime=[n for n in range (2,101)if all(n%i!=0 for i in range (2,n))]
print(prime)