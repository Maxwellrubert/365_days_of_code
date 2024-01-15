def main():
    num = int(input())
    # YOUR CODE GOES HERE
    if num >= 90:
        print("A")
    elif num >= 80:
        print("B")
    elif num >= 70:
        print("C")
    elif num >= 60:
        print("D")
    elif num >= 50:
        print("E")
    else:
        print("F")
    return 0

if __name__ == '__main__':
    main()


'''Decision making and constructs

Decision making statements in programming languages decide the direction of flow of program execution.
There comes situations in real life when we need to make some decisions and based on these decisions, we decide what should we do next.
Similar situations arise in programming also where we need to make some decisions and based on these decision we will execute the next block of code.
Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated. For example:

num = 10
print(num == 5) #prints False
print(num == 10) #prints True
Notice that variable assignment is done using a single equals operator ”=”, whereas comparison between two variables is done using the double equals operator ”==”. The “not equals” operator is marked as ”!=”.

Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in “if statements” and loops.

An “if statement” is written by using the if keyword.

x = 100
y = 200
if y > x:
    print("y is greater than x")
Elif

The elif keyword is pythons way of saying “if the previous conditions were not true, then try this condition”.

x = 100
y = 100
if x > y:
    print("x is greater than y")
elif x == y:
    print("x and y are equal")
Else

The else keyword catches anything which isn’t caught by the preceding conditions.

x = 200
y = 100
if y > x:
    print("y is greater than x")
elif x == y:
    print("x and y are equal")
else:
    print("x is greater than y")
Try the following example in the editor below.

Given an integer num denoting percentage of a student, calculate the grade according to the below rules:

If num >= 90, grade A.
If num >= 80, grade B.
If num >= 70, grade C.
If num >= 60, grade D.
If num >= 50, grade E.
Else grade will be F.
Print a string consisting of single character denoting the grade.

Sample Input

59
Sample Output

E'''
