# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 21:33:27 2018

@author: Osman

Project Euler P33: Digit Cancelling Fractions
    
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting 
to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by 
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in 
value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value 
of the denominator.

"""
for a in range(1,10):
    for b in range(1,10):
        x=10*a+b
        for c in range(1,10):
            y1=10*c+a
            y2=10*b+c
            if x*c==y1*b:
                print('ab, ca',a,b,c)
            if x*c==y2*a:
                print('ab, bc',a,b,c)
            
            
# 16, 64
# 19, 95
# 26, 65               
# 49, 98               
                