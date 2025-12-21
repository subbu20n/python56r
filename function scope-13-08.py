#-----------FUNCTION SCOPE-----------------(variables preferences) #like same as we did in (ansible)
 
#LOCAL    -L 
#Enclosed -E 
#Global   -G 
#Builtin  -B 

# num1 = 10 

num1 = 10

def first(): 
    num1 = 40 
    def second(): 
        num1 = 55 
     
        def third(): 
            nonlocal num1 
            num1 = 30 
            print(num1)  #30 
        third() 
        print(num1)#30 
    second()  
    print(num1)   #40 
first() 
print(num1) #  10    
           
# def check_function(): 
#     num2 = 20 
#     print(num2) 
#     print(num1) 

# check_function() 
# print(num1) 

##GLOBAL SCOPE 

# num1 = 10 

# def check_function():
#     num2 = 20 
#     print(num1) 
#     print(num2) 
#     #check_function()  #---> recursion 
#     def inner_function():
#         print(num1) 
#     inner_function() 
# check_function() 
# print(num1)  
# print(num2) #num2 here wont work 
# inner_function() # here it does not work         


#ENCLOSED SCOPE 

# def outer_function():
#     str = 'Good Morning'  #enclosed means within the function inside a function 
#     def inner_function():
#         print(str) 
#     inner_function() 
# outer_function()
# print(str)        


#BUILTIN --> "length" already in python has builtin function we need to define those functions 

#ORDERS  (preferences) 
# L - Local 
# E - Enclosed 
# G - Global 
# B - builtin

# num1 = 10 

# def check_function():
#     num1 = 20 
#     print(num1) # first preference local -20 
# check_function()
# print(num1)  # global -10   

# user_name = 'subbu' 

# def first_function():
#     user_name  = 'arun'  # enclosed  
#     def second_function():
#         user_name = "ram" 
#         print(user_name) #ram 
#     second_function() 
#     print(user_name)  #arun
# first_function()  
# print(user_name)     #subbu   

# user_name = 'subbu' 

# def first_function():
#     user_name = "arun" 
#     def second_function(): 
#          print(user_name) # arun -->becase nearest username refered -enclosed one  
#     second_function() 
#     print(user_name) # arun 
# first_function() 
# print(user_name)     #subbu 

# #-----

# user_name = 'subbu' 

# def first_function():
#     def second_function(): 
#          print(user_name) # subbu -->becase nearest username refered -enclosed one  
#     second_function() 
#     print(user_name) # subbu
# first_function() 
# print(user_name)     #subbu  

#------ 

# num1 = 10 
# def check_function(): 
#      num1 += 1  #UnboundLocalError: cannot access local variable 'num1' where it is not associated with a value
#      print(mum1) 
# check_function() 
# # print(num1)     
 
# num1 = 10 
# def check_function():
#     global num1 # 10
#     num1 += 1 # 10 + 1 = 1 ---> reassignment 
#     print(num1) # 11
# check_function()
# print(num1) # reassignment happened so it becomes # 11 

# num1 = 10 
# def check_function(): 
#     global num1 # global num1 keep means it uses "global num1 only" "key as num1 only value will become '20'" 
#     num1 = 20 #global num1 "wont keep means it create a variable new one num1" 
#     print(num1) # 10 
# check_function() 
# print(num1)     #10 

# num1 = 10
# def check_function():
#     num1 = 20 
#     globals()['num1'] = 30 # reassigning to num1 as '30' from here 
#     print(num1) #20 
# check_function() 
# print(num1) #30     


# def first_function():
#     num1 = 35 
#     def second_function(): 
#         num1 = 45 
#         print(num1)  #45 
#     second_function()  # when function ends value will aslo kill  
#     print(num1)  # 35 
# first_function() 
  

# def first_function():
#     num1 = 35 
#     def second_function(): 
#         nonlocal num1   # nonlocal means enclosed use the value of num1 (enclosed key only valuw will be changed to 45)
#         num1 = 45  
#         print(num1)  #45 
#     second_function()  # when function ends value will aslo kill  
#     print(num1)  # 45  
# first_function()  

# def first_function():
#     num1 = 35 
#     def second_function():
#         num1 = 45  
#         def third_function():
#             nonlocal num1 
#             num1 = 55 # "nonlocal" which are available to "num1" now it becomes num1 in seond function also '55'
#             print(num1) #55 
#         third_function()
#         print(num1) #55 
#     second_function()
#     print(num1) # 35 

# first_function()            
 