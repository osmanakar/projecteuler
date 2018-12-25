def isPrime(n):
    i=2
    while i <= n**0.5:  
        if n % i == 0:  
            return False 
        else:  
            i += 1  
    return True

def numberPrime(n):
    i = 2
    sequentialPrimes = []
    while len(sequentialPrimes) < n:
        if isPrime(i) is True:
            sequentialPrimes.append(i)
            i += 1
        else:
            i += 1
    return sequentialPrimes.pop()

x=input("The n'th prime number. n=")
y="the "+str(x)+"'th prime number is "+str(numberPrime(int(x)))
print(y)