def main():
    names = []
    # YOUR CODE GOES HERE
    names.append("Robin")
    names.append("Aman")
    names.append("Rahul")
    print(names)
    return 0

if __name__ == '__main__':
    main()


'''Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish.

List is a collection which is ordered and changeable. Allows duplicate members.

Lists can also be iterated over in a very simple manner. Below is an example to build a list.

my_list = []
# append insert the element at the end of the list
my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list[0]) # prints 1
print(my_list[1]) # prints 2
print(my_list[2]) # prints 3
Accessing an index which does not exist generates an exception (an error).

my_list = [1,2,3]
print(my_list[5]) # Gives an error
Negative Indexing

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

my_list = [1, 2, 3]
print(my_list[-1]) #prints 3
print(my_list[-2]) #prints 2
Try the following example in the editor below:

You are given an empty list named names, you have to insert “Robin”, “Aman”, “Rahul” at the end of list one after other.'''
