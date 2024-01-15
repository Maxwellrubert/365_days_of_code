def main():
    A = int(input())
    B = int(input())
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A/B)
    print(A%B)
    print(A**B)
    # Print seven lines as described above
    return 0

if __name__ == '__main__':
    main()




'''Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

Python follows the similar precedence as other languages does.

number = 4+2*6-4/2
print(number) # prints 14
In Python, there are two kinds of division: integer division and float division.

Integer Division

Integer division returns the floor of the division. That is, the values after the decimal point are discarded.
 It is written as ‘//’ in Python 3. So, 1//3 = 0, 2//3 = 0 and 3//3 = 1. Integer values are precisely stored, so they are safe to use in comparisons.

In Python 2, the ‘//’ operator is not included, so it must be imported from the future module. 
 See the code below for how to use the ‘//’ operator in Python 2. The ‘/’ operator in Python 2 returns an integer result if both of the operands are integers.

Python 2

# Python 2 integer division using '//'
from __future__ import division
print 4//3  # prints 1
or

# Python 2 integer division using '/'
print 4/3  # prints 1
Python 3

# Python 3 integer division
print(4//3) # prints 1
Float Division

Float division returns a floating point approximation of the result of a division.
 For example, Only a certain number of values after the decimal can be stored, so it is not possible to store an exact binary representation of many floating point numbers. This sometimes leads to problems when comparing numbers or when rounding.

In Python 2, the only standard division operator is ‘/’. If both values are integers, the result is an integer. If either of the values is a float, the return is a float.
 The future module can be used so that ‘/’ represents floating point division as it does in Python 3.

Python 2

from __future__ import division
# floating point division using __future__ syntax
print 4 / 3 # prints 1.33333333333
or

# floating point division using a float to force float result
# no need to import from __future__
print 4 / 3.0 # prints 1.33333333333
Python 3

print(4 / 3) # prints 1.33333333333
Other operators availabe are modulo(%) and power(**).

remainder = 10%4
print(remainder) # prints 2
power = 2 ** 4
print(power) # prints 16
Try the following example in the editor below.

The provided code stub reads two integers from STDIN, A and B. Add code to print seven lines where:

First line shows the sum of two integers A and B.
Second line shows the difference between two numbers(A-B).
Third line shows the product of the two integers A and B.
Fourth line shows the Integer Division where A is the numerator and B is the denominator.
Fifth line shows the Float Division where A is the numerator and B is the denominator.
Sixth line shows the Remainder when A is divided by B.
Seventh line shows the Power i.e AB'''
