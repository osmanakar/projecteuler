"""
Project Euler P2
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. By starting with 1 
and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find the 
sum of the even-valued terms.
"""

sum_even=0 
limit=4000000

index=2
f0=1
f1=2
temp=0
while f1<limit:
    temp=f1
    f1=f1+f0
    f0=temp
    if index % 3 == 2:
        sum_even +=temp
    index = index+1

print(sum_even,f0,f1,index)