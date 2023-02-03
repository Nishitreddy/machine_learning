#Nishit Reddy Lingala
#ID: 700747128

#Question5


#define a funtion countUpperLower
def countUpperLower(s):  
    #sum method used to count the number of cases by counting number of each itteration    
    upper_count = sum(1 for i in s if i.isupper())   #isupper method used to check if its upper case
    lower_count = sum(1 for i in s if i.islower())   #islower method used to check if its lower case
    print( "No. of Upper case characters : %s\nNo. of Lower case characters : %s" % (upper_count,lower_count))


a= "The quick Brow Fox"
countUpperLower(a)
