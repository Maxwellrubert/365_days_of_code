def main():
    my_list = [['a', 'b'], ['cc', 'dd', ['eee', 'fff']], ['g', 'h']]
    
    # insert a new list [1, 2, 3] at the end of my_list
    # Your code goes here
    my_list.append([1,2,3])
    print(my_list)
    # Delete 'eee' from the list
    # Your code goes here
    my_list[1][2].remove('eee')
    print(my_list)
    return 0
if __name__ == '__main__':
    main()


'''A list can contain any sort object, even another list (sublist), which in turn can contain sublists themselves, and so on. This is known as nested list.

You can use them to arrange data into hierarchical structures.

Creating a Nested List

my_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
Access Nested List

You can access individual items in a nested list using multiple indexes.



my_list = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
print(L[2])  
# Prints ['cc', 'dd', ['eee', 'fff']]  

print(L[2][2])  
# Prints ['eee', 'fff']  

print(L[2][2][0])  
# Prints 'eee'
Add items

To add new values to the end of the nested list, use append() method.

When you want to insert an item at a specific position in a nested list, use insert() method.

You can merge one list into another by using extend() method.

my_list = ['a', ['bb', 'cc'], 'd']
my_list[1].append('xx')
print(my_list)
# Prints ['a', ['bb', 'cc', 'xx'], 'd']

my_list = ['a', ['bb', 'cc'], 'd']
my_list[1].insert(0,'xx')
print(my_list)
# Prints ['a', ['xx', 'bb', 'cc'], 'd']

my_list = ['a', ['bb', 'cc'], 'd']
my_list[1].extend([1,2,3])
print(my_list)
# Prints ['a', ['bb', 'cc', 1, 2, 3], 'd']
Remove items

If you know the index of the item you want, you can use pop() method. It modifies the list and returns the removed item.

If you’re not sure where the item is in the list, use remove() method to delete it by value.

my_list = ['a', ['bb', 'cc', 'dd'], 'e']
x = my_list[1].pop(1)
print(my_list)
# Prints ['a', ['bb', 'dd'], 'e']

# removed item
print(x)
# Prints cc

my_list = ['a', ['bb', 'cc', 'dd'], 'e']
my_list[1].remove('cc')
print(my_list)
# Prints ['a', ['bb', 'dd'], 'e']
Try the following example in the editor below.

You are given a nested list named ‘my_list’, perform the operations as defined in the comments.

NOTE: You don’t need to change/remove any code. Only add the line of code, wherever needed.'''
