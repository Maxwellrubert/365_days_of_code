import numpy as np
def main():
    arr = [1, 3, 2, 2, 5, 3, 8, 2]
    
    # Convert the above array into ndarray
    arr = np.array(arr)
    
    print(type(arr))
    
    # Use where to find all the indexes of 2
    x = np.where(arr==2)
    
    print(x)
    return 0

if __name__ == '__main__':
    main()


'''Numpy arrays are great alternatives to Python Lists. Some of the key advantages of Numpy arrays are that they are fast, easy to work with, and give users the opportunity to perform calculations across entire arrays.

The array object in NumPy is called ndarray. We can create a NumPy ndarray object by using the array() function.

import numpy as np
my_arr = np.array([1, 2, 3, 4, 5])

print(my_arr)

print(type(my_arr))
#  It shows that my_arr is numpy.ndarray type.
NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) # prints 0
print(b.ndim) # prints 1
print(c.ndim) # prints 2
print(d.ndim) # prints 3
Access Array Elements

1-D Array

Array indexing is the same as accessing an array element.

import numpy as np

my_arr = np.array([1, 2, 3, 4])

print(my_arr[0]) # prints 1
2-D Array

To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

# Access the 5th element on 2nd dimension:
import numpy as np

my_arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd dimension: ', my_arr[1, 4]) # prints 10
Negative Indexing

# Use negative indexing to access an array from the end.
import numpy as np

my_arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', my_arr[1, -1]) # prints 10
Searching array

You can search an array for a certain value, and return the indexes that get a match.
 To search an array, use the where() method.

my_arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(my_arr == 4)
print(x) # Finds all the indexes of 4
Try the following example in the editor below.

You are given a list of integers called ‘arr’, convert this into ndarray and use where to find all the occurences of 2 in the array and assign that to x.'''
