# Question 2

# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'lucky'
dog['color'] = 'white'
dog['breed'] = 'Retriever'
dog['legs'] = 4
dog['age'] = 1
# Create a student dictionary 
# add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Jesse',
    'last_name': 'Pinkman',
    'gender': 'male',
    'age': 28,
    'marital_status': 'single',
    'skills': ['Python', 'JavaScript'],
    'country': 'USA',
    'city': 'Albequrqeu',
    'address': '55th St'
}
# Get the length of the student dictionary
length = len(student)

# Get the value of skills and check the data type
skills = student['skills']
print(type(skills)) #type returns the datatype

# Change the skills values by adding one or two skills
student['skills'].append('CSS')
student['skills'].append('Node')

# Get the dictionary keys as a list
student_keys = list(student.keys())

# Get the dictionary values as a list
student_values = list(student.values())

# Print the results
print("Student dictionary length:", length)
print("Student skills:", student['skills'])
print("Student keys:", student_keys)
print("Student values:", student_values)

#Explanation:
#Construct a dictionary dog and then add the legs, age, breed, color, and name. 
#Create another dictionary named student next, add first name, last name, gender, age, marital status, skills, nation, city, and address to the dictionary you created. 
#Calculate the length of the dictionary using len() after adding all characteristics.

