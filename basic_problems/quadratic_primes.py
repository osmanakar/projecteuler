"""
Project Euler P27

Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive 
integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible 
by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 
primes for the consecutive values 0≤n≤79. The product of the coefficients, 
−79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n,
 starting with n=0.
"""
small_prime_list=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
small_prime_set=set({2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97})
#import number_theory as nt

def isPrime(n):
    if n<101:   
        if n in small_prime_set:
            return True
        else:
            return False
    else:
        for p in small_prime_list:
            if n % p ==0:
                return False

        i=101
        while i <= n**0.5:  
            if isPrime(i)==True:
                if n % i == 0:  
                    return False                  
            i += 1  
        return True

def func(a,b,n):    
    return n**2+a*n+b

max=1
a_max=-1001
b_max=-1001
n_max=0


for a in range(-1000,1001):
    for b in range(-1000,1001):
        continue0=True
        n=0
        while continue0==True:
            if isPrime(func(a,b,n))==True:
                n=n+1
            else:
                n_max_cand=n-1
                continue0=False
        if n_max_cand>n_max:
            a_max=a
            b_max=b
            n_max=n_max_cand
print(a_max,b_max,n_max,a_max*b_max)

