# Tuple Creation & Access:
# Create a tuple with elements (10, 20, 30, 40, 50).
# Access the third element in the tuple.
# Attempt to change the second element and observe the result.

def problem1():
    my_tuple = (10, 20, 30, 40, 50)
    print(f'The value of my tuple is: {my_tuple}')
    print(f'The third element of my tuple is: {my_tuple[2]}')
    try:
        my_tuple[1] = 200
    except Exception as e:
        print(e)
    return

# Tuple Slicing:
# Create a tuple with elements from 1 to 10.
# Slice the tuple to get elements from index 2 to 5.

def problem2():
    my_tuple = (1,2,3,4,5,6,7,8,9,10)
    print(f'The elements in my tuple is: {my_tuple}')
    print(f'My tuple sliced to get elements from index 2 to 5 is: {my_tuple[2:6]}')
    return

# Set Operations:
# Create two sets: A = {1, 2, 3, 4} and B = {3, 4, 5, 6}.
# Find the union and intersection of sets A and B.
# Add the element 7 to set A and remove the element 2.

def problem3():
    setA = {1, 2, 3, 4}
    setB = {3, 4, 5, 6}
    print(f'SetA and SetB are: {setA} {setB}')
    print(f'Union of A and B: {setA.union(setB)}')
    print(f'Intersection of A and B: {setA.intersection(setB)}')
    setA.add(7)
    print(f'A after adding 7: {setA}')
    setA.remove(2)
    print(f'A after removing 2: {setA}')
    return

# Create the following sets:
# C = {1, 2, 3, 4}
# D = {2, 3}
# Perform the following operations:
# Find the difference between C and D. This should give you the elements that are in C but not in D.
# Check if D is a subset of C. This checks if all elements in D are also in C.
# Expected Outputs:
# Difference between C and D
# Whether D is a subset of C

def problem4():
    setC = {1,2,3,4}
    setD = {2,3}
    print(f'Set C and D are: {setC} {setD}')
    print(f'The difference between C and D are: {setC.difference(setD)}')
    if len(setD.difference(setC)) == 0:
        print(f'Set D is a subset of set C')
    else:
        print('Set D is not a subset of set C')
    return

# Problem 5: Tuple Immutability
# Create a tuple:
# Create a tuple my_tuple with elements (5, 10, 15, 20).
# Attempt to modify the tuple:
# Try to append a new element 25 to my_tuple.
# Create a set and try to add a tuple to it. Then, try to add a list to it and observe the result.

def problem5():
    my_tuple = (5, 10, 15, 20)
    print(f'My initial tuple: {my_tuple}')
    try:
        print('Trying to add 25 to tuple')
        my_tuple[4] = 25
    except Exception as e:
        print(e)
    my_set = {2,}
    my_set.add(my_tuple)
    print(f'My initial set: {my_set}')
    print('Adding a list')
    my_set.add([2,3,4])
    print(my_set)
    return
