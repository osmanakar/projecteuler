"""
Project Euler P21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""
import math

def sum_of_divisors(n):
    sum=0
    s_n = math.floor(math.sqrt(n))
    for k in range(1,s_n+1):
        if n%k==0:
            sum=sum+k+(n/k)
    if s_n**2==n:
        sum=sum-s_n
    return sum-n

sum_amiable=0

for n in range(1,10001):
    if sum_of_divisors(sum_of_divisors(n))==n:
        if n != sum_of_divisors(n):
            sum_amiable += n

print(sum_amiable)


