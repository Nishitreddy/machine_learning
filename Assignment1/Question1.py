# Question 1

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()  # Sort the list

# Find the min and max age
minimum_age = min(ages)
maximum_age = max(ages)

# Add the min age and the max age again to the list
ages.append(minimum_age)
ages.append(maximum_age)

# Find the median age
if len(ages) % 2 == 0:   #check if there are 2 medians
    med = (ages[len(ages)//2] + ages[len(ages)//2 - 1])/2
else:                    #else 1 median
    med = ages[len(ages)//2]

# Find the average age
average = sum(ages) / len(ages)

# Find the range of ages
range = maximum_age - minimum_age

# Print the results
print("Min age: ", minimum_age )
print("Max age: ", maximum_age)
print("Median age:", med)
print("Average age:", average)
print("Range of ages:", range)

#Explanation:
#As the supplied query sorted the list of ages first, it then used min() and max() to find the least and maximum ages and imported those values into the ages list.
#We then found the median, average and the age. We have also checked if the number of elements are even or odd accordingly and found the median.