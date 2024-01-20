def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm', 'allows', 'community', 'phase', 'single']
    my_list = [x for x in str_list if len(x)%2==1]
    
    print(my_list)
    return 0

if __name__ == '__main__':
    main()


'''List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.

Suppose, we want to separate the letters of the word InterviewBit and add the letters as items of a list.

The first thing that comes in mind would be using for loop.

S = 'Interviewbit'
letter_S = []
for l in S:
    letter_S.append(l)
print(letter_S)
However, Python has an easier way to solve this issue using List Comprehension. List comprehension is an elegant way to define and create lists based on existing lists.

S = 'InterviewBit'
letter_S = [l for l in S]
print(letter_S)
Conditions in Comprehension

Using if

Create a list of odd numbers in the range of 1 to 10

my_list = [x for x in range(1, 10) if x%2 == 1]
print(my_list)
Try the following example in the editor below.

You are given a list of strings, using list comprehensions create a new list of strings called ‘my_list’, which only contain the strings that have odd length.'''
