#Nishit Reddy Lingala
#ID: 700747128

#Question2

#Declare a list with given elements

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Given List :")
print(my_list)
print("List with only odd indices position are : ")
# Using for loop to traverse along the list 
for i in range(1, len(my_list), 2): # Len function used to find the length of the list
   print(my_list[i])                # Third parameter in third loop helps us traverse 2 elemts at a time
  