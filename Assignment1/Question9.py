# Question 9
# Read the number of students
num_students = int(input("Enter the number of students: "))
# Initialize an empty list to store the weights in pounds
weightsLbs = []

# Read the weights of the students in pounds
for i in range(num_students):
    weight = float(input(f"Enter the weight of student {i+1} in pounds: "))
    weightsLbs.append(weight)

# Initialize an empty list to store the weights in kilograms
weightsKgs = []

# Convert the weights from pounds to kilograms
for weight in weightsLbs:
    weightKg = weight * 0.453592 # formula to convert pounds to kgs
    weightsKgs.append(weightKg)

# Print the results
print("Weights in pounds:", weightsLbs)
print("Weights in kilograms:", weightsKgs)

#Explanation:
#We take input from users asking for the number of students and weight of each corresponding student in lbs and 
#we store it in a list. We declare the empty weightKgs list and then in the range of the previous list we use
#the formula (weight * 0.453592) to convert lbs into kgs and store the values in the weightKgs list.