def main():
    # Assign values to the following variable as described above
    # Don't change the variable name
    my_string1 = "InterviewBit"
    my_string2 = "Don't change the variable name"
    my_int = 11
    my_float = 20.0
    
    # Don't change the below code
    print("String1: %s" % my_string1)
    print("String2: %s" % my_string2)
    print("Integer: %d" % my_int)
    print("Float: %f" % my_float)
    return 0

if __name__ == '__main__':
    main()


'''Python is completely object oriented, and not “statically typed”. You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

Numbers

To define an integer, use the following syntax:

my_int = 11
To define a floating point number, you may use one of the following notations:

my_float = 11.0
# You can also use the below syntax
my_float = float(11)
Strings

Strings are defined either with a single quote or a double quotes.

my_string = 'InterviewBit'
my_string  = "InterviewBit"
The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

my_string = "Don't worry about it"
Operators between numbers and strings is not supported:

my_int = 11
my_string = "InterviewBit"
my_intstring = my_int + my_string
NOTE: Above code will not work.

Try the following example in the editor below.

You have to assign the following values in the variable:

"InterviewBit" should be assigned in the variable named my_string1.
"Don't change the variable name" should be assigned in the variable named my_string2.
11 should be assigned in the variable named my_int.
20.0 should be assigned in the variable named my_float.'''
