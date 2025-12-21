#----INPUTS----  

# num1 = 10 
# num2 = 20 

# print(num1 + num2 ) 

# num1  = input() 
# num2 = input() 
# print(num1 + num2) #2030 

# num1 = input('enter num1:') 
# num2 = input('enter num2:') 
# print(num1 + num2 )

# print(type(num1 + num2)) #string 
# print(int(num1) + int(num2)) #20,20=40 will print convert to integer 
# print(int(num1) - int(num2)) 

# print(type(num1)) #string  
# print(type(num2)) #string

# num1 = input('Enter num1:') 
# num2 = input('Enter num2:') 

# num1 , num2 = int(num1) , int(num2) #--->  # (reassign) 
# print(num1 + num2)

# num1 = int(input('Enter num1:')) 
# num2 = int(input('Enter num2:')) #enter num1: '1.3' --string ni direct ga float ne chnage cheyalemu 
#                                  #ValueError: invalid literal for int() with base 10: '1.3'
# print(num1 + num2)  

# num1 = float(input('Enter num1:'))
# num2 = float(input('Enter num2:'))

# print(num1 + num2)


#     "--DATA CONVERISION--"

# num1 = 5.6 
# print(int(num1) , num1) # int =5 , num1 = 5.6 
# num1 = int(num1) # conversion to int it becomes 5 
# print(num1) #5  

# num1 = 5.6 
# num1 = int(num1) #5 
# num1 = float(num1) #5.0 
# print(num1) #5.0 

num1 = 32
print(float(num1)) #32.0 
num1 = 0 
print(float(num1))  #0.0 
num1 = 0 
print(complex(num1)) #0j 

print(list('Good Morning Hyd'))  #['G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g', ' ', 'H', 'y', 'd']

# #""---OPERATORS---"" 

num1 = 5 
print(num1 + 1) #6 
print(num1) #5 

num1 = 5 
num1 = num1 + 1 #reassign
print(num1)#6

num1 += 3  
num1 = num1 + 3 
print(num1)



