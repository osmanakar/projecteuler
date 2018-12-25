"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from number_theory import isPrime

limit=2*10**6
print(limit)
sum=0
for n in range(1,limit):
    if isPrime(n) is True:
        print(n)
        sum += n

print(sum)