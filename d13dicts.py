def main():
    my_dict = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 0
    }

    # update value for key "Sunday" to 7
    my_dict["Sunday"]=7
    
    # adding another item with key "Default" having value 0
    my_dict["Default"]=0
    for i in sorted(my_dict):
        print ("(\'" + i + "\',", str(my_dict[i]) + ")")

    return 0

if __name__ == '__main__':
    main()


'''A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
print(my_dict)
# Dictionary with the use of Mixed Keys.
my_dict = {'One' : 'Robin', 2 : 'Rahul'}
print(my_dict)
Accessing Items

You can access the items of a dictionary by referring to its key name, inside square brackets.

There is also a method called get() that will give you the same result.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
val = my_dict[2]
print(val) # print 'Rahul'

# using get()
val = my_dict.get(2)
print(val) # print 'Rahul'
Change Values

You can change the value of a specific item by referring to its key name.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
my_dict[2] = 'Rohan'
val = my_dict[2]
print(val) # print 'Rohan'
Loop through a Dictionary

You can loop through a dictionary by using a for loop.
 When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
for x in my_dict:
    print(x)    # print 1 2 3

# values() method to return values of a dictionary
for x in my_dict.values():
    print(x)    # print 'Robin' 'Rahul' 'Aman'

# Loop through both keys and values, by using the items() method
for key, val in my_dict.items():
    print(key, val)
Adding Items

Adding an item to the dictionary is done by using a new index key and assigning a value to it.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
my_dict[4] = 'Shivam'  # Added item key is 4 and value is 'Shivam'
print(my_dict)
Removing Items

There are several methods to remove items from a dictionary.

The pop() method removes the item with the specified key name.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
my_dict.pop(2) # Removes item with key 2 and value 'Rahul'
print(my_dict)
The del keyword removes the item with the specified key name.

my_dict = {1 : 'Robin', 2 : 'Rahul', 3 : 'Aman'}
del my_dict[2] # Removes item with key 2 and value 'Rahul'
print(my_dict)
Dict() constructor

It is also possible to use the dict() constructor to make a new dictionary.

my_dict = dict(1 = 'Robin', 2 = 'Rahul', 3 = 'Aman')
# note the use of equals rather than colon for the assignment
print(my_dict)
Try the following exercise in the editor below.

Given a dictionary called ‘my_dict’, perform the operations described in the comments:

# update value for key "Sunday" to 7
# adding another item with key "Default" having value 0'''
