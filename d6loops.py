def main():
    N = int(input())
    # YOUR CODE GOES HERE
    for i in range (1,N,2):
        print(i)
    return 0

if __name__ == '__main__':
    main()


'''There are two types of loops in Python, for and while.

The “for” loop

For loops iterate over a given sequence.

my_list = [1, 2, 3]
for num in my_list:
    print(num) 
#Prints 1, 2, 3
For loops can iterate over a sequence of numbers using the “range” and “xrange” functions.
 The difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient. (Python 3 uses the range function, which acts like xrange).
 Note that the range function is zero based.

# Prints out the numbers 0,1,2,3,4
for i in range(5):
    print(i)

# Prints out 2,3,4
for i in range(2, 5):
    print(i)

# Prints out 2, 4, 6
for i in range(2, 8, 2):
    print(i)
while loops

While loops repeat as long as a certain boolean condition is met. For example:

# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
Now, let’s dive into Jump statemets.

break

continue

Why break statement?

Let’s take a real scenario where we can use break statements.</li>

Let us consider a repetitive task to send email to 100 employees.

Suppose after sending 10 emails, suddenly internet disconnected. What action you will perform at that time?

You can either attempt a try to send rest 90 emails, which will result in error. Alternatively, you can terminate the mailing process with a warning or error message.

Definitely, it is better to postpone or terminate the mailing process for now than sending mails further that will result in error.

break is used to exit a for loop or a while loop, whereas continue is used to skip the current block, and return to the “for” or “while” statement. A few examples:

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
NOTE: Unlike languages like C,CPP.. we can use else for loops. When the loop condition of “for” or “while” statement fails then code part in “else” is executed. If break statement is executed inside for loop then the “else” part is skipped. Note that “else” part is executed even if there is a continue statement.

# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
Try the following example in the editor below.

You are given an integer N, print all the odd values, for all i, where 0 <= i < N. Print each values on a seperate line.'''
