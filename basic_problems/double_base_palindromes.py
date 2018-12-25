"""
The decimal number, 585 = (1001001001)_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic 
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
"""
import string


def int2base(x, base):
    digs = string.digits + string.ascii_letters
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    return ''.join(digits)

def reverse(s):
    return s[::-1]
 
def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)
    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False

print(int2base(14,base=3))

print(type(int2base(14,base=3)))
"""
sum=0
for n in range(1,1000000):
    if isPalindrome(str(n))==True:
        if isPalindrome(int2base(n,base=2))==True:
            sum=sum+n

print(sum)
"""




