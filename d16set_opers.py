'''
def printset(setx):
    li = list(setx)
    li.sort()
    print(li)
'''

def main():
    # Below are the three sets 
    
    X = set([1, 3, 7, 5, 6, 10, 20, 21, 22, 23, 55, 51, 2, 19, 9, 17, 27, 26, 25, 35])
    Y = set([2, 10, 13, 18, 17, 22, 28, 27, 5, 49, 46, 43, 3])
    Z = set([21, 1, 32, 25, 12, 11, 8, 10, 26, 16, 31, 20, 30, 14])
    
    # 'set1' contains the student who loves to play all three sports
    setab= set(X.intersection(Y))
    set1 = setab.intersection(Z)
    
    printset(set1)
    
    # 'set2' contains the student who loves to play both Football and Cricket, but don't play Basketball
    set2 = setab.difference(Z)
    
    printset(set2)
    
    # 'set3' contains the student who loves to play Cricket, but don't loves any other sport
    setac=set(X.union(Z))
    set3 = Y.difference(setac)
    
    printset(set3)
    return 0

if __name__ == '__main__':
    main()


'''There are many operations which we can perform on set, some of them are described below.

Set union



The .union() operator returns the union of a set and the set of elements in an iterable.
 Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
 Set is immutable to the .union() operation (or | operation).

s = set("Scaler")
print s.union("Academy")
# set(['a', 'S', 'c', 'l', 'e', 'r', 'A', 'd', 'm', 'y'])
Set intersection



The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
 Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
 The set is immutable to the .intersection() operation (or & operation).

s = set("Scaler")
print s.intersection("Academy")
# set(['c', 'a', 'e'])
Set difference



The tool .difference() returns a set with all the elements from the set that are not in an iterable.
 Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
 Set is immutable to the .difference() operation (or the - operation).

s = set("Scaler")
print s.difference("Academy")
# set(['r', 'l', 'S'])
Try the following excercise in the editor below.
You are given three sets X, Y, Z where X contains the children id who loves to play Football, Y contains the children id who loves to play Cricket, and Z contains the children id who loves to play BasketBall. You need to perform operations on these sets as decribed in comments.

Note: You are only required to add your code, no need to change any of the given statements.'''
