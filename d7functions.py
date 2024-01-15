#Return the factorial of the number N
def factorial(N):
    # Your code goes ee    o  nrneN1-)
    i=1
    while N>0:
        i=i*N
        N=N-1
    print(i)


'''A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

Defining a Function

In Python a function is defined using the def keyword followed by the function name and parenthesis.
def my_function():
    print("Hello InterviewBit")
Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
def my_function(name):
    print("Hello %s" %name)
Functions may return a value to the caller, using the keyword- ‘return’.

def add_numbers(x, y):
    return x + y
Calling Function

Simply write the function’s name followed by (), placing any required arguments within the brackets.

def my_function():
    print("Hello InterviewBit")
def add_numbers(x, y):
    return x + y

# print "Hello InterviewBit"
my_function()

val = add_numbers(2, 3)
print(val)
# print 5
Functions with keyword arguments

The arguments which have a default value are termed as keyword arguments and required ones are positional arguments.
These arguments should always be the last ones, i.e. All the required (positional) arguments go first. They are then followed by the optional keyword arguments.
Arguments without defaults are required otherwise you get a syntax error.
def distance_travelled(t, u = 0, g = 9.81):
    """
    Function distance_travelled calculates the distance travelled by an object
    with initial speed u, in a time interval of t, where acceleration due to gravity is g

    input: t (time taken), u (initial speed) g (acceleration due to gravity)
    output: distance travelled

    Example: 
      >>> distance_travelled(1.0)

          4.905
    """
    d = u*t + 0.5 * g * t**2
    return d

print(distance_travelled(2.0))
print(distance_travelled(2.0, u = 1.0))
print(distance_travelled(2.0, g = 9.7))
print(distance_travelled(g = 9.7, t = 2.0))
Try the following example in the editor below.

You have to complete a function named factorial which will return the factorial of the integer N.
Note: Main code is already implemented, you need to complete the factorial function only.'''
