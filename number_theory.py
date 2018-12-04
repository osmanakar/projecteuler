# number_theory module
"""
Functions:

isPrime
primeFactorization
numberOfDivisors
sumOfDivisors
lcm
gcd


"""

import string

small_prime_list=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
small_prime_set=set({2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97})

def isPrime(n,*positional_parameters, **keyword_parameters):
    if 'acceptNegative' in keyword_parameters:
        if keyword_parameters[acceptNegative] in {'y','yes','Yes', 'True'}:
            n=abs(n)
        else:
            if n<0:
                print('n is either 0 or negative')

    if n<101:   
        if n in small_prime_set:
            return True
        else:
            return False
    else:
        for p in small_prime_list:
            if n % p == 0:
                return False

        i=101
        while i <= n**0.5:  
            if isPrime(i)==True:
                if n % i == 0:  
                    return False                  
            i += 1  
        return True
    


def primeFactorization(n):
    factorization={}
    if n==1:
        print('n=1, exeptional case, no prime factorization')
        return False
    
    while isPrime(n)==False:
        d=2
        while d<n:
            if n % d == 0:
                if d in factorization:
                    factorization[d]=factorization[d]+1
                else:
                    factorization[d]=1
                temp=n
                n=n//d
                d=temp
            else: 
                d=d+1 
                  
    if n in factorization:
        factorization[n]=factorization[n]+1
    else:
        factorization[n]=1

    return factorization

def numberOfDivisors(n):
#Returns the number of positive divisors of n
    if n==1:
        print('n=1, exceptional case')
        return 1

    pfn=primeFactorization(n)
    numD=1
    for p in pfn:
        numD = numD *(pfn[p]+1)
    return numD

def sumOfDivisors(n):
    pfn=primeFactorization(n)
    sumD=1
    for p in pfn:
        sumD = sumD *((p**(pfn[p]+1)-1)//(p-1))
    return sumD

def lcm(S):
    primes={}
    anw=1
    for n in S:
        pfn=primeFactorization(n)
        for p in pfn:
            if p in primes:
                primes[p]=max(pfn[p],primes[p])
            else:
                primes[p]=pfn[p]
    for p in primes:
        anw = anw * (p**primes[p])
    return anw

def gcd(S):
    primes={}
    anw=1
    for n in S:
        pfn=prime_factorization(n)
        for p in pfn:
            if p in primes:
                primes[p]=min(pfn[p],primes[p])
            else:
                primes[p]=pfn[p]
    for p in primes:
        anw = anw * (p**primes[p])
    return anw


def int2base(x, base):
    digs = string.digits + string.ascii_letters
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return int(''.join(digits))

def reverse(s):
    return s[::-1]
 
def isPalindrome(s):  
    #input should be string
    # Calling reverse function
    rev = reverse(s)
    # Checking if both string are equal or not
    if (s == rev):
        return True
