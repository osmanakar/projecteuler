# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:05:36 2018

@author: Osman
Project Euler, P60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
 and concatenating them in any order the result will always be prime. 
 For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of 
 these four primes, 792, represents the lowest sum for a set of four primes 
 with this property.

Find the lowest sum for a set of five primes for which any two primes 
concatenate to produce another prime.
"""

from number_theory import isPrime

def remarkable(A, n):
    for i in range(0,n-1):
        p1=A[i]
        for p2 in A[i+1:n]:
            if isPrime(int(str(p1)+str(p2))) is False:
                return False
            if isPrime(int(str(p2)+str(p1))) is False:
                return False
    return True

#assumes A[0:n-1] is iterative
#for speed, assume A is increasing
def remarkable_iterative(A,n):
    p1=A[n-1]
    for i in range(0,n-1):
        p2=A[i]        
        if isPrime(int(str(p1)+str(p2))) is False:
            return False
        if isPrime(int(str(p2)+str(p1))) is False:
            return False
    return True

m=0
solExist=False
four_tuples=set()
minSolExist=False
minSum=0

while minSolExist is False:
    m=m+1
    R1=100*m
    R2=100*(m+1)
    if solExist is False:
        Bound=R2+1
        
    print("Searching 4-remarkable-tuples from ",R1," to ", R2)
    for p4 in range(R1,R2):
        if isPrime(p4) is True:
            for p3 in range(3,p4):
                if isPrime(p3) is True and remarkable([p3,p4],2) is True:
                    for p2 in range(3,p3):
                        if isPrime(p2) is True and remarkable_iterative([p3,p4,p2],3) is True:
                            for p1 in range(3,p2):
                                if isPrime(p1) is True and remarkable([p2,p3,p4,p1],4) is True:
                                    print("4-sol",p1,p2,p3,p4)
                                    four_tuples.add((p1,p2,p3,p4))
                                    
    for A in four_tuples:
        RR1=A[3]
        for n in range(RR1,R2):
            if n>Bound:
                print("Finished")
                exit
            if isPrime(n) is True and remarkable_iterative(list(A)+[n],5) is True:
                if solExist is False:
                    print("First Solution: ",list(A)+[n], "sum: ", sum(A)+n)
                    Bound=5*(sum(A)+n)
                    solExist=True
                    minSum=sum(A)+n
                elif sum(A)+n<minSum:
                    minSum=sum(A)+n                    
                print("Solution: ",list(A)+[n], "sum: ", sum(A)+n,"minSum = ", minSum)        
                
                
                                        
    

"""
while solExist is False:
    m=m+1
    R1=100*m
    R2=100*(m+1)
    print("max prime ranges from ",R1," to ", R2)
    minPossible=5*R2
    Bound=R2+1
    for p1 in range(R1,R2):
        if p1>Bound:
            exit        
        if isPrime(p1) is True:
            for p2 in range(3,p1):
                if isPrime(p2) is True and remarkable([p1,p2],2) is True:
                    for p3 in range(3,p2):
                        if isPrime(p3) is True and remarkable([p1,p2,p3],3) is True:
                            for p4 in range(3,p3):
                                if isPrime(p4) is True and remarkable([p1,p2,p3,p4],4) is True:
                                    print("4-sol",p1,p2,p3,p4)
                                    for p5 in range(3,p4):
                                        if isPrime(p5) is True:
                                            if remarkable([p1,p2,p3,p4,p5],5) is True:
                                                if solExist is False:
                                                    Bound=5*(p1+p2+p3+p4+p5)
                                                solExist=True
                                                if (p1+p2+p3+p4+p5)<minPossible:
                                                    minPossible=p1+p2+p3+p4+p5
                                                    print(p1,p2,p3,p4,p5,minPossible)
                
print(minPossible)        

"""










