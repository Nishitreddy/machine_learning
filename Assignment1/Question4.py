# Question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
length_it_companies = len(it_companies)
print("Length of IT companies set:", length_it_companies)

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("After adding Twitter:", it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['wipro','TCS','Infosys'])
print("After adding multiple companies:", it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove('wipro')
print("IT companies set after removing Uber:", it_companies)

it_companies.discard('TCS')
print("IT companies set after discarding Tesla:", it_companies)

# Diff between remove and discard
# 'remove' raises an error if the item is not found in the set, 'discard' does not

# Join A and B
AunionB = A.union(B)
print("A union B:", AunionB)

# Find A intersection B
AintersectionB = A.intersection(B)
print("A intersection B:", AintersectionB)

# Is A subset of B
isAsubsetofB = A.issubset(B)
print("Is A subset of B:", isAsubsetofB)

# Are A and B disjoint sets
isABdisjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", isABdisjoint)

# Join A with B and B with A
ABjoin = A.symmetric_difference(B)
print("Symmetric difference between A and B:", ABjoin)

# Delete the sets completely
del A
del B

# Convert the ages to a set and compare the length of the list and the set
ageSet = set(age)
lengthAgeList = len(age)
lengthAgeSet = len(ageSet)
print("Length of age list:", lengthAgeList)
print("Length of age set:", lengthAgeSet)