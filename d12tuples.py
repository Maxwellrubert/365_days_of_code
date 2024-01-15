def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    list1=list(tuple1)
    list2=list(tuple2)
    list1[0]="number"
    list2[0]="number"
    tuple1=tuple(list1)
    tuple2=tuple(list2)
    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()


'''Python Collections

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.

Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

Set is a collection which is unordered and unindexed. No duplicate members.

Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

We will discuss all four collection one by one, we had discussed List in one of the previous article.

Tuple

Tuple is similar to a list but once the tuple is created we can’t change the elements directly.

Creating a Tuple

my_tuple = ('one', 'two', 'three')
print(my_tuple)
# print ('one', 'two', 'three')
You can access tuple items by referring to the index number, inside square brackets:

my_tuple = ('one', 'two', 'three')
print(my_tuple[1])
# print two
Is there any way to change Tuple Values?

Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
 But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

my_tuple = ('one', 'two', 'three')
my_list = list(my_tuple)
my_list[2] = 'two'
my_tuple = tuple(my_list)
print(my_tuple)
# print ('one', 'two', 'two')
Create Tuple with One item

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

my_tuple = ("one",)
print(type(my_tuple))

# NOT a tuple
my_tuple = ("one")
print(type(my_tuple))
Join Two Tuples

To join two or more tuples you can use the + operator:

my_tuple1 = ('one', 'two', 'three')
my_tuple2 = ('1', '2', '3')
my_tuple3 = my_tuple1 + my+tuple2
print(my_tuple3)
Try the following example in the editor below.

Given two tuples called tuple1 and tuple2, perform the operations described in comments in the editor.'''
