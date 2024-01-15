def main():
    data = ("Robin", 10, "chocolates")
    format_string = "Hello %s. You are currently left with %d %s."
    print(format_string %data)
    
    return 0

if __name__ == '__main__':
    main()


'''Python uses C-style string formatting to create new, formatted strings. The ”%” operator is used to format a set of variables enclosed in a “tuple” (a fixed size list), together with a format string, which contains normal text together with “argument specifiers”, special symbols like "%s" and "%d".

my_string = "InterviewBit"
print("Hello %s" InterviewBit)
# prints "Hello InterviewBit"
To use two or more argument specifiers, use a tuple (parentheses):

qty = 10
item_name = "chocolate"
rs = 100
print("You can buy %d %s in %d rupees" % (qty, item_name, rs))
# prints "You can buy 10 chocolate in 100 rupees"
Any object which is not a string can be formatted using the %s operator as well. The string which returns from the “repr” method of that object is formatted as the string. For example:

my_list = [1, 2, 3]
print("Given list: %s" %my_list)
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)

String format() Method

The format() method formats the specified value(s) and insert them inside the string’s placeholder.  

The placeholder is defined using curly brackets: {}.  

The format() method returns the formatted string.

The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.

qty = 10
item_name = "chocolate"
rs = 100
#named indexes
print("You can buy {quantity} {item} in {amt} rupees".format(quantity = qty, item = item_name, amt = rs))
#numbered indexes:
print("You can buy {0} {1} in {2} rupees".format(qty, item_name, rs))
#empty placeholders:
print("You can buy {} {} in {} rupees".format(qty, item_name, rs))
# prints "You can buy 10 chocolate in 100 rupees"
f-strings

PEP 498 introduced a new string formatting mechanism known as Literal String Interpolation or more commonly as F-strings (because of the leading f character preceding the string literal). The idea behind f-strings is to make string interpolation simpler.<?p>
<p>To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format(). F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.") 
# prints Hello, My name is Tushar and I'm 23 years old.
Note : F-strings are faster than the two most commonly used string formatting mechanisms, which are % formatting and str.format().

Try the following example in the editor below.

You will need to write a format string which prints out the data using the following syntax: Hello Robin. You are currently left with 10 chocolates.'''
