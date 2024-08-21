# Create and Modify a Dictionary
# Create a dictionary representing a book with keys: title, author, year, and genre.
# Add a new key publisher to the dictionary.
# Update the year of the book.
# Print the updated dictionary.

def problem1():
    my_dict = {'title': "Aravind's life", 'author': 'Aravind Desikamani', 'year': 2000, 'genre': 'tragedy'}
    print(f'The initial dictionary: {my_dict}')
    my_dict['publisher'] = 'Friends publications'
    print(f'The current dictionary after inserting publisher: {my_dict}')
    my_dict.update({'year': 2024})
    print(f'The updated dictionary after updating the year value: {my_dict}')

# Create a dictionary representing a student with keys: name, age, grade, and subjects (a list of subjects).
# Access and print the student's name and grade.
# Use the get() method to access a non-existent key like address, and provide a default value None.
    
def problem2():
    my_student_dict = {'name': 'Aravind', 'age': 23, 'grade': 4, 'subjects': ['Batch', 'PSS', 'Automations']}
    print(f'The current student dictionary is {my_student_dict}')
    print(f"The student's name is: {my_student_dict.get('name')}")
    print(f"The student's grade is: {my_student_dict.get('grade')}")
    print(f"The student's address is: {my_student_dict.get('address', 'Default value')}")
    return

# Using Dictionary Methods
# Create a dictionary with some sample data.
# Print all the keys in the dictionary using the keys() method.
# Print all the values using the values() method.
# Print all key-value pairs using the items() method.

def problem3():
    my_student_dict = {'name': 'Aravind', 'age': 23, 'grade': 4, 'subjects': ['Batch', 'PSS', 'Automations']}
    print(f'The initial dictionary is: {my_student_dict}')
    print(f'The keys in the dictionary are: {my_student_dict.keys()}')
    print(f'The values in the dictionary are: {my_student_dict.values()}')
    print(f'The items in the dictionary are: {my_student_dict.items()}')
    return
    

# Manipulating a Dictionary
# Create a dictionary representing a car with keys: make, model, year, and color.
# Update the color of the car.
# Use the pop() method to remove the year from the dictionary.
# Use the popitem() method to remove the last inserted key-value pair.
# Clear the dictionary and print it to confirm it’s empty.

def problem4():
    my_car_dict = {'make': 'Maruti Suzuki', 'model': 'Ciaz', 'year': 2022, 'color': 'white'}
    print(f'The initial car dictionary: {my_car_dict}')
    my_car_dict['color'] = 'Eggshell White with Chrome'
    print(f'The car dictionary after updating color: {my_car_dict}')
    my_car_dict.pop('year')
    print(f'The car dictionary after popping year: {my_car_dict}')
    my_car_dict.popitem()
    print(f'The car dictionary after popping item: {my_car_dict}')
    my_car_dict.clear()
    print(f'The car dictionary after clearing: {my_car_dict}')
    return

# Nested Dictionary Access
# Create a dictionary representing a person, with nested dictionaries for address and job.
# Access and print specific information like job title and city from the address.

def problem5():
    address_dict = {'number': 1, 'street': 'Kaveri street', 'nagar':'Rajaji Nagar', 'town': 'Villivakkam', 'city': 'Chennai'}
    job_dict = {'title': 'Software Engineer', 'company': 'Fidelity investments'}
    person_dict = {'name': 'Aravind Desikamani', 'address': address_dict, 'job': job_dict}
    print(f'The person dictionary is: {person_dict}')
    print(f'The job title of the person is: {person_dict["job"]["title"]}')
    print(f'The city of the person is: {person_dict["address"]["city"]}')
    return

