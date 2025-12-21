# num1 = 1 
# n = 15 
# fact = 1 
# while num1 <= n: 
#     fact = fact * num1  #1 *1=1 ,1*2=2, 2*3=6, 6*4=24 ----it goes like that 
#     print(num1) #12345678910112131415 
#     num1 += 1 #1+1=2, 2+1=3,3+1=4 -----

# print(fact)    

# ----same above code---- with function 

# def calc_fact(n): 
#     if n < 0: 
#         return 'fact is not possible' 
#     num1 = 1 
#     fact = 1  
#     while num1 <= n:  
#         fact = fact * num1 
#         print(num1) 
#         num1 += 1  
#     print(fact) 
# calc_fact(-1)        


# implement a basic login system where the user has three 3 attempts to enter the correct password  using a loop 

# db_username = 'subbu' 
# db_password = '12345' 

# input_username = input('Enter username')  
# input_password = input('Enter password') 

# if input_username == db_username and input_password == db_password: 
#     print('Login done') 
# else: 
# #     print('Login failed') 

###--------
# db_username = 'subbu' 
# db_password = '1234' 
# remaining_attempts = 3  

# while remaining_attempts > 0: 
#     input_username = input('enter username') 
#     input_password = input('enter password') 

#     if input_username == db_username and input_password == db_password: 
#         print('login done')

#     else: 
#         remaining_attempts -= 1  # 3-1=2 , 2-1=0 , 1-1=0 
#         print('login failed')    

#------------

# db_username = 'subbu' 
# db_password = '12345' 
# remaining_attempts = 3 

# while remaining_attempts > 0: 
#     input_username = input('Enter username') 
#     input_password = input('Enter password') 

#     if input_username == db_username and input_password == db_password: 
#         print('login done') 

#     else: 
#       remaining_attempts -= 1 #3 - 1 = 2 , 2-1 =1 , 1-1 =0  
#       print('Login failed')     
#---------- 

# db_username = 'subbu' 
# db_password = '12345' 
# remaining_attempts = 3 
# while remaining_attempts > 0: 
#     input_username = input('Enter username') 
#     input_password = input('Enter password') 

#     if input_username == db_username and input_password == db_password: 
#         print('login done') 
#         print('redirecting') 
#         break   

#     else: 
#       remaining_attempts -= 1 #3 - 1 = 2 , 2-1 =1 , 1-1 =0  
#       print('Login failed')      


# ---------questions------------- 

# reverse a number using a while loop 
# 1. also can we get the sum of all digits 
# write the progarm to count the number of digits in a given numbers usinga while loop

# num1 = 12534 
# # 5 = ---> no . of digits 
# # 15 = ---> sum of digits (1+2+5+3+4=15) 

# #-------using STRINGS 

# print(len(str(num1))) 
# str1 = str(num1)  # 5  
# sum = 0 
# for i in str1: 
#     sum = sum + int(i)  
# print(sum)     

# print(int(str(num1) [: : -1])) #negative indexing 12534 ==> 43521 

#-------using NUMBER SYSTEM PROPERTIES --------------- 

# 356 % 10 => 6 # remainders will be 6 
# 459 % 10 => 9 
# 321 % 10 => 1 
# 50  % 10 => 0 
# 5   % 10 =>  # it becomes 5 only 

# 2456 % 10 --> remainer = 6 and que = 245 , 245 %10 -r-5 q=24, 24%10 = r=4 q=2 , 2%10 = r-2 q=0 

# num1 = 2456 
# sum = 0 
# count = 0

# while num1 > 0: 
#     rem = num1 % 10 
#     print(rem) 

#     #que = num1 // 10 
#     # num1 = que  
#     num1 = num1 // 10  # quetioent will used for next iteration 
#     count += 1  
#     sum += rem 
# print(count) 
# print(sum)     


num1 = 234 
sum = 0 #4+3+2=9
count = 0 

while num1 > 0: 
    rem = num1 % 10 # 234%10 = 4 , 23 %10 = 3 2%10= 2 , 0 
    print(rem) 
    num1 = num1 // 10 
    count += 1 #0+1=1+1=2+1=3
    sum += rem #0+4 = 4 , 4+3 = 7, 7+2=9 
print(count)  # no. of counts ==> 3 
print(sum)       # 4+3+2=9 