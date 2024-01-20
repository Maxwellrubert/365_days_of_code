class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    def printfunction(self):
        print(self.name + " " + self.branch)

def main():
    #Your code goes here
    stud1=Student('Robin','CSE')
    stud2=Student('Rahul','ECE')
    stud1.printfunction()
    stud2.printfunction()
    return 0

if __name__ == '__main__':
    main()


'''Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.

Objects are an encapsulation of variables and functions into a single entity.

Objects get their variables and functions from classes. Classes are essentially a template to create your objects.

To create a class, use the keyword class

class my_class:
    my_var = "InterviewBit"
    def my_function(self):
        print("Welcome to " + self.my_var)
        
# Create an object of the above class

my_obj = my_class()
my_obj.my_function()
# prints Welcome to InterviewBit
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

The init() Function

To understand the meaning of classes we have to understand the built-in __init__() function.

__init__() is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
obj = Student("Robin", "CSE")
print(obj.name)
print(obj.branch)
Try the following example in the editor below

We have a class defined for Student. Create two new object for students called stud1 and stud2. Set stud1 name as ‘Robin’ and branch ‘CSE’ and stud2 name as ‘Rahul’ and branch as ‘ECE’.'''
