# Question 3
# Create a tuple containing names of your sisters and your brothers
sisters = ("siri", "chandana", "sai")
brothers = ("mike", "rahool", "shhivaa")

# Join brothers and sisters assign it to siblings
siblings = sisters + brothers

# Number of siblings you have?
num = len(siblings)

#siblings tuple and add the name of your father and mother and assign it to familyMembers
familyMembers = siblings + ("Father", "Mother")

# Print the results
print("Siblings:", siblings)
print("Number of siblings:", num)
print("Family members:", familyMembers)

#Explanation:
#Create two tuples at first, one for each sibling, then unite them both and assign the items to the siblings. 
#After determining the number of siblings, add the names of the parents to the siblings, and then output the tuple of siblings.
