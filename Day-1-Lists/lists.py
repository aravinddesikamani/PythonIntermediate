# Create a list of numbers from 1 to 10, then perform the following tasks:
# Slice the list to get the first 5 elements.
# Slice the list to get every second element.
# Append the number 11 to the list.
# Insert the number 5.5 between 5 and 6.
# Remove the number 3 from the list.
# Sort the list in descending order.

def problem1():
    list1 = []
    for i in range(1, 11):
        list1.append(i)
    print(f'The list contents are: {list1}')
    print(f'The first 5 elements are {list1[:5]}')
    print(f'The every second element is {list1[::2]}')
    list1.append(11)
    print(f'The list contents after appending are: {list1}')
    list1.insert(5, 5.5)
    print(f'The list contents after inserting 5.5 are: {list1}')
    list1.remove(3)
    print(f'The list contents after removing 3 are: {list1}')
    list1.sort()
    list1.reverse()
    print(f'The list contents after sorting in desending order are: {list1}')

# Given a list of names, names = ["John", "Paul", "George", "Ringo"]:
# Add "Yoko" to the end of the list.
# Insert "Brian" at the beginning of the list.
# Find the index of "George".
# Count how many times "John" appears in the list.
# Reverse the order of the list.
    
def problem2():
    names = ["John", "Paul", "George", "Ringo"]
    print(f'The initial contents of the list is {names}')
    names.append('Yoko')
    print(f'The contents after inserting Yoko to end of the list {names}')
    names.insert(0, 'Brian')
    print(f'The contents after inserting Brian to the beginning of the list {names}')
    print(f'The index of Geroge in the list is: {names.index("George")}')
    names.reverse()
    print(f'The reversed list is: {names}')
    return

# Create a list that contains both numbers and strings: mixed = [1, "apple", 3.14, "banana", 5]:
# Remove the string "apple" from the list.
# Add a new number at the end of the list.
# Replace the string "banana" with the string "grape".
# Find the length of the list.
# Extract all numeric values from the list and create a new list with just these numbers.

def problem3():
    mixed = [1, "apple", 3.14, "banana", 5]
    print(f'The initial list is: {mixed}')
    mixed.remove('apple')
    print(f'The list after removing apple is: {mixed}')
    mixed.append(100)
    print(f'The list after adding a new number at the end: {mixed}')
    banana_index = mixed.index('banana')
    mixed.remove('banana')
    mixed.insert(banana_index, 'grape')
    print(f'The list after replaing banana with grape: {mixed}')
    new_list = []
    for item in mixed:
        if isinstance(item, (int, float)):
            new_list.append(item)
    print(f'The list after extracting all numeric values from the mixed list : {new_list}')
    return

# Given a list of numbers: numbers = [8, 3, 7, 2, 5, 6, 4, 1]:
# Sort the list in ascending order.
# Reverse the sorted list.
# Remove the largest number.
# Insert a new number at the correct position to keep the list sorted.
# Create a new list that contains only the even numbers from the sorted list.
def problem4():
    numbers = [8, 3, 7, 2, 5, 6, 4, 1]
    print(f'Initial list of numbers: {numbers}')
    numbers.sort()
    print(f'Sorted list: {numbers}')
    numbers.reverse()
    print(f'Reversed sorted list: {numbers}')
    numbers.remove(max(numbers))
    print(f'Removed the biggest number: {numbers}')
    number = 10
    numbers.append(10)
    numbers.sort()
    print(f'The list after inserting 10 at sorted place: {numbers}')
    new_list = []
    for item in numbers:
        if item % 2 == 0:
            new_list.append(item)
    print(f'The new list with only even numbers from sorted number list: {new_list}')
    return

# problem1()
# problem2()
# problem3()
# problem4()