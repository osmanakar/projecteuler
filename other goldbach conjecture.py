# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 01:33:17 2018

@author: Osman
Project Euler, P

It was proposed by Christian Goldbach that every odd composite number can be 
written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a 
prime and twice a square?

"""

import number_theory as nt
#import numpy as np

done=False
n=33

while done is False:
    n=n+2
    if nt.isPrime(n) is False:
        print(n)
        nSatisfy=False
        m=1
        while 2*m*m<n and nSatisfy is False:
            if nt.isPrime(n-2*m*m) is True:
                nSatisfy=True
            m=m+1
        if nSatisfy is False:
            done=True
            solution=n
            
            
        



























