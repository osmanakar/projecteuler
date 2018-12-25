# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:56:13 2018

@author: Osman

Project Euler P25
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

F1=1
F2=1
temp=0
n=2
digit=1
bigD=10
while digit<1000:
    n=n+1
    temp=F2
    F2=F2+F1
    F1=temp
    if F2 > bigD:
        bigD=bigD*10
        digit=digit+1





























