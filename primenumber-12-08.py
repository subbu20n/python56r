#------PRIME NUMBER ------> 2,3,5,7,11,13,17,19,23,29  [1 AND ITSELF]


# -----------------METHOD-1 -----------------


# ONLY has  2 factors 
#total iterations same as input  

# num1 = 7
# count = 0 

# for i in range(1, num1 + 1):  #1,2,3,4,5,6,7 (num1 +1 --> 9+1=10 -so it will iterate till 9 also) #(7 iterations happened )
#     if num1 % i == 0: 
#         count += 1 # reassignment if num1 % i == 0 --> ayitene (count +1) or else no need  
# if count == 2: 
#     print('prime number')    
# else:
#     print('Not a prime number')  



#---------------------METHOD-2 ---------------------# 

# num1 = 7

# if num1 <=1: 
#     print('Not a prime number') 
# else: 
#     flag = True 

#     for i in range(2, num1): #2,3,4,5,6 varaku iterate avutundi), 7 iterate avvakudadu 
#         if num1 % i == 0:  
#             flag = False  
#             print('Not a prime number') 
#             break 
#     if flag == True: # "IF flag:" we can write here ok  # this IF block has to 'write' "for loop outer side" ok
#        print('Prime')    

# ########


# num1 = 2
 
# def check_even(num1): 
#     if num1 % 2 == 0: 
#         return True 
#     return False 

# r1 = check_even(num1) 
# print(r1) 

# num1 = 2 
# def check_even(num1): 
#     if num1 % 2 == 0: # ()"2 % 2 == 0 returns TRUE")
#         return True  
#     return False 
# r2 = check_even(num1)  #return value stores in r1 
# # print(r2)

# def check_prime(in_num): 
#     if in_num <= 1: 
#         return 'Not a prime number' 
#     for i in range(2,in_num): 
#         if in_num % i == 0: 
#             return 'Not a prime number' 
#     return 'prime' 

# r2 = check_prime(7) 
# print(r2) 


# def check_prime(num1):
#     if num1 <= 1: 
#         return 'Not a prime number' 
#     for i in range(2, num1): 
#         if num1 % 2 ==0: 
#             return 'Not a prime number' 
#         return 'prime' 
# r2 = check_prime(4) 
# print(r2)        

#--------------------METHOD-3------------------------------#   


#24 => 1,2,3,4,6,8,12,24 
#12 => 1,2,3,4,6,12 
#26 => 1,2,13,26 
#17 => 1,17 
#27 => 1,3,9,27 

#24 => 2-12 
#26 => 2-13 

              
# def check_prime(num1): 
#     if num1 <= 1: 
#         return 'Not a prime number' 
#     for i in range(2, num1 // 2 + 1): 
#         if num1 % i == 0: 
#             return 'Not a prime number' 
#     return 'prime' 

# r2 = check_prime(13)
# print(r2)     


#-------------------------METHOD-4------------------------------# 


#64 
# 1 * 64    # CAREFULLY OBSERVE HERE There is a pattern i dont want to check repeated it quite sequence  
# 2 * 32 
# 4 * 16   # here i check for 16 and i dont want to check again for 16  right 
# 8 * 8 
#16 * 4 
#32 * 2 
#64 * 1 

# 81 
# 1 * 81 
# 3 * 27 
# 9 * 9 
# 27 * 3 
# 1 * 81  

# def check_prime(num1): 
#     if num1 <= 1: 
#         return 'Not a prime number' 
#     for i in range(2, int(num1 ** 0.5 + 1)):  # 
#         if num1 % 2 == 0: 
#             return 'Not a prime  number' 
#     return 'prime'  # return value stores in r2 
# r2 = check_prime(13) 
# print(r2)     

def prime(num1): 
    if num1 <= 1: 
        return 'Not a prime number' 
    for i in range(2, int(num1 ** 0.5 + 1 ) ): 
        print(int(num1 ** 0.5 + 1 )) 
        print(int(num1)) 
        if num1 % 2 == 0: 
            return 'Not a prime number' 
    return 'prime' 
res = print(prime(13))    