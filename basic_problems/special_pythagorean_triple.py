"""
Project Euler P9
A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a=2mn, b=m^2-n^2, c=m^2+n^2
a+b+c=2m(m+n)k=1000
m(m+n)k=500 
20.25
"""
m=20
n=5
a=2*m*n
b=m**2-n**2
c=m**2+n**2
print(a*b*c)

