import math
# The radius of a circle is 30 meters.
radius = 30

# Calculate the area of a circle 
areaOfCircle = math.pi * (radius ** 2)

# Calculate the circumference of a circle
circumOfCircle = 2 * math.pi * radius

# Print the results
print("Area of circle:", areaOfCircle)
print("Circumference of circle:", circumOfCircle)

# Take radius as user input and calculate the area.
radius = int(input("Enter the radius : "))
areaOfCircle = math.pi * (radius ** 2)
print("Area of circle with radius",radius," :", areaOfCircle)

#Explanation:
#Determine the circle's area and assign a value to areaOfCircle. 
#Next, determine the circle's circumference and assign a value to circumOfCircle. 
#Now compute the area using the radius as an input.
#We here import math class to retrieve the value of pi using math.pi method.
