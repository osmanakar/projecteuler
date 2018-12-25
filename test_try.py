"""
import string
import sets
x="\"this is string\""
print(x)
y=x.replace("\"","")
x=x.replace("\"","")

print(x,y)

A=set()
A.add(1)
print(A)

for i in range(1,6):
    A.add(i)

print(A)
sum=0
for i in range(1,10):
    if i in A:
        sum=sum+i

print(sum)

#Dictionary Test
a={2:1,3:3}
#print(a)
a[2]=4
a[5]=1
print(a)


import itertools

stuff = [1, 2, 3]

for subset in itertools.combinations(stuff, 2):
    print(subset,type(subset))
    print(subset[0])

"""
import number_theory as nt
import itertools as it


def is8prime(nList):
    non_prime_count=0
    for n in nList:
        if nt.isPrime(n)==False:
            non_prime_count = non_prime_count+1
            if non_prime_count>2:
                return False
    return True

n=100000000
subset=[1,2,4]
str_n=list(str(n))
list_n=[]
temp_n=n
for digit in range(0,10):
    for j in subset:       
        str_n[j]=str(digit)                        
    temp_n="".join(str_n)                        
    list_n.append(int(temp_n))                

#print(nt.isPrime(333333361))
#print(list_n)
#print(is8prime(list_n))

primes=[111109, 222109, 333109, 444109, 555109, 666109, 777109,888109, 999109]

for n in primes:
    print(nt.isPrime(n))


