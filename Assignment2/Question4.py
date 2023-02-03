#Nishit Reddy Lingala
#ID: 700747128

#Question4

#We define a function with name unique 
def unique(input):
  print("Sample list:", input)
  my_list = []
  for a in input:  #using a for loop to traverse the given input list
    if a not in my_list:  # not in keyword is used to find the unique elements in the list and stored in a 
      my_list.append(a)   
  print("Unique list : ", my_list)


unique([1,2,3,3,3,3,4,5])  
