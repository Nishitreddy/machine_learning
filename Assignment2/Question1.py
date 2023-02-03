#Nishit Reddy Lingala
#ID: 700747128

#Question1
#ith loop is used to travel the number of columns
#jth loop is used to travel the number of stars in column


#First half helps to print the pattern upto 5 lines in increasing order
for i in range (0, 5):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")  #\r is a carriage return so we use \r instead of \n



#This half of the program helps to print the pattern for the next half in decresing order
for i in range (5, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")  #\r is a carriage return so we use \r instead of \n