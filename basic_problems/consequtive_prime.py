"""
Project  Euler
Consecutive prime sum
Problem 50 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime 
below one-hundred.

The longest sum of consecutive primes below one-thousand that adds 
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the 
most consecutive primes?

"""

from number_theory import isPrime
limit=1000000

def next_prime(n):
    m=n+1
    while isPrime(m)==False:
        m=m+1
    return m


max_n_prime=1
sol_prime=2
for start in range(2,limit):
    if isPrime(start) is True:
        #print(,start)
        n_prime=1
        p_sum=start
        k=start
        while p_sum < limit:
            k=next_prime(k)
            p_sum=p_sum+k
            n_prime=n_prime+1
            if isPrime(p_sum)==True and n_prime >= max_n_prime and p_sum < limit:
                max_n_prime=n_prime
                sol_prime=p_sum

print(max_n_prime,sol_prime)
