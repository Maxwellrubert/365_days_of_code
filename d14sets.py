def main():
    my_set = set([1, 3, 2, 4, 1, 3, 3, 0])
    
    # add 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 to my_set
    my_set.update([10,12,13,14,15,16,17,18,19,20,21,22,23])
    
    # delete 2 and 3 from my_set
    my_set.discard(2)
    my_set.discard(3)
    li = list(my_set)
    li.sort()

    print(li)
    return 0

if __name__ == '__main__':
    main()


'''A set is a collection which is unordered and unindexed. In Python, sets are written with curly brackets. 
 A set cannot contain duplicates.

my_set = {'one', 'two', 'three'}
print(my_set)

# using set()

my_set = set(['one', 'two', 'three'])
print(my_set)
Sets are unordered, so you cannot be sure in which order the items will appear.

Access Items

You cannot access items in a set by referring to an index or a key.
 But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

my_set = {'one', 'two', 'three'}
for val in my_set:
    print(val)
NOTE: Once set is created, you cannot change its items, but you can add new items.
 Below is an example:

my_set = {'one', 'two', 'three'}
my_set.add('four')

# update is used to update set with another sequence
my_set.update(['four', 'five', 'six'])

print(my_set)
# my_set will contain {'one', 'two', 'three', 'four', 'five', 'six'}
# Since there will be no duplicates. 
Remove Item

You can remove an item in a set, use the remove(), or the discard() method.

NOTE: If the item to remove does not exist, remove() will raise an error, but discard() will NOT raise any error.

my_set = {'one', 'two', 'three', 'four'}
my_set.remove('one') # removes 'one' from my_set
my_set.discard('three') # removes 'three' from my_set
my_set.remove('five') # throws an error
my_set.discard('five') # Will not throw an error
Try the following example in the editor given below.

Given a set called ‘my_set’, perform the operations described in the comments.'''
