"""
By replacing the 1st digit of the 2-digit number *3, it turns out that 
six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 
5-digit number is the first example having seven primes among the ten 
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 
56773, and 56993. Consequently 56003, being the first member of this family, 
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not 
necessarily adjacent digits) with the same digit, is part of an eight 
prime value family.

Ans: 121313
subset:  (0, 2, 4) 
[121313, 222323, 323333, 424343, 525353, 626363, 727373, 828383, 929393]
"""
import number_theory as nt
import itertools as it


def is8prime(nList):
    non_prime_count=0
    min_limit=len(nList)-8
    for n in nList:
        if nt.isPrime(n)==False:
            non_prime_count = non_prime_count+1
            if non_prime_count>min_limit:
                return False
    return True

def find8prime(exponent_max):
    answer=0
    temp_answer=0
    for exponent in range(1,exponent_max):
        n_min=10**exponent
        n_max=10**(exponent+1)
        for k in range(3,exponent,3):
            indexes=range(0,exponent+1)
            for n in range(n_min,n_max):
                if (n % 3 != 0) and (n % 2 == 1):
                    print(n)
                    for subset in it.combinations(indexes,k):
                        if 0 in subset:
                            str_n=list(str(n))
                            list_n=[]
                            temp_n=""
                            for digit in range(1,10):
                                for j in subset:                        
                                    str_n[j]=str(digit)                        
                                temp_n="".join(str_n)                        
                                list_n.append(int(temp_n))                          
                            if is8prime(list_n) == True:
                                print('subset: ',subset, list_n)
                                return min(list_n)
                        else:
                            str_n=list(str(n))
                            list_n=[]
                            temp_n=""
                            for digit in range(0,10):
                                for j in subset:                        
                                    str_n[j]=str(digit)                        
                                temp_n="".join(str_n)                        
                                list_n.append(int(temp_n))                          
                            if is8prime(list_n) == True:
                                print('subset: ',subset, list_n)
                                return min(list_n)

print(find8prime(100))
