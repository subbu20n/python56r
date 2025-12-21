#------------FUNCTIONS -TYPES OF ARGUMENTS -------------

#             positional arguments 
#             keyword argument 
#             default arguments 
#             arbitary argument (*args) 
#             keyword arbitory arguement(**kargs) 

#------------- #positional argument -------------- 

# def simple_calculator(num1,num2): 
#     print(num1 + num2) 
#     print(num1 - num2) 
#     print(num1 * num2) 
#     if num2 != 0 : 
#         print(num1 / num2) 
#         print(num1 % num2) 
#         print(num1 // num2) 
#     else: 
#         print('division by zero is not possible') 

# simple_calculator(2,4)


# -------------#keyword arguments --------------(in companies will use this method)

# def simple_calculator(num1=10,num2=32):    #clearly mentioning here (key=value )
#     print(num1 + num2) 
#     print(num1 - num2) 
#     print(num1 * num2) 
#     if num2 != 0 : 
#         print(num1 / num2) 
#         print(num1 % num2) 
#         print(num1 // num2) 
#     else: 
#         print('division by zero is not possible') 

# simple_calculator(num1=10, num2=32)

#--------------Default arguments-------------------

# it will take a default value if you wont provide means
# default arguments writes always "right side"  
# if user provides it takes or else it takes "default value"  
#

# def simple_calculator(num1, num2=4):
#       print(num1 + num2) 

# simple_calculator(num2=5, 3)

# def simple_calculator(num1, num2=4):
#       print(num1 + num2) 

# simple_calculator(num1=5, num2=10) 

# def simple_calculator(num1,  num2=4, num3=1):
#        print()

# simple_calculator(num2=4, 1, num3=1) -----> (it wont works positional arguments give 1)
# simple_calculator(10, num2=4, num3=1) ----- it works positional arguments gave first "10")


# def sum(a,b): 
#      print(a + b) 

# def sum(a,b,c): 
#      print(a+b+c) 

# def sum(a,b,c): 
#      print(a+b+c) 

# #sum(1,2) 
# sum(1,2,3) 
# #sum(1,2,3,4)  # latest one will pick  (method over loading) in python doesnot work with same name functions 

# def subbu(a,b,c):
#     print(a+b+c) 
# def subbu(a,b,c,d): 
#     print(a+b+c+d)    

# subbu(1,3,4)     

#------------------arbitary argument (*args) -----------------------

# def sum(a, *b):  # first argument goes to"a" nd remaining all goes to '*b'
#      print(a)
#      print(b) 

# sum(1,2) 
# sum(1,2,3) 
# sum(1,2,3,4)   

# def sum(a, *b): 
#      print(a) 
#      print(b) 
# sum(1,2,3,4,5,5)    
# print()  #a=1 ,b= 2,3,4,5,5

def sum(*a, b): # it goes all to "*a" only
     print(a)
     print(b) 

sum(1,2,) 
sum(1,2,3) 
sum(1,2,3,4)  
print()


def sum(a, *b): # it goes all to "*a" only
     temp = 0 
     for i in b:
        temp = temp + i
     print(temp)

sum(1,2) 
sum(1,2,3) 
sum(1,2,3,4) 

