#---------------------problem solving---------------------- 

# ----------------1.prime-function: ---------------------

#  ----3 ways for prime function to find out------------- 
#     1.by using count var 
#     2. just by iterating  
#     3. optimized of 2nd sol 


# --------------1.by using count var------METHOD-1--------------- 

# def is_prime(n): 
#     if n < 2: 
#         return False  
#     count = 0 
#     for i in range(1,n +1 ): 
#         if n % i == 0: 
#           count += 1 
#     if count == 2: 
#         return True  
#     return False  

# n = int(input('enter')) 
# print(is_prime(n))        

# #-------------------just by iterating - METHOD-2-------------------- 

# def is_prime(n): 
#     if n < 2: 
#         return False  
#     for i in range(2,n): 
#         if n % i  == 0: 
#             return False  
#     return True  
# n = int(input('enter')) 
# print(is_prime(n))     

# #-----------------optimized by factors---METHOD-3------------------- 

# def is_prime(n): 
#     if n < 2: 
#         return False  
#     for i in range(2, int(n ** 0.5) + 1): 
#         if n % i == 0: 
#             return False 
#     return True  
# n = int(input('enter')) 
# print(is_prime(n))    

# # ------- Find out 'NEXT PRIME NUMBER" ---------------------- 
# n = int(input('enter'))
# if is_prime(n): 
#     print(n) 
# else: 
#     while True: 
#         n += 1 
#         if is_prime(n): 
#             print(n) 
#             break 
 
# print(is_prime(n)) 


#-------------------FIND 2 largest numbers (sum)-------------------------- 

# a = 1 
# b = 2 
# c = 3 

# if a >= b and a >= c: 
#     if b >= c: 
#         print(a+b) 
#     else: 
#         print(a+c) 

# elif b >= a  and b >= a: 
#     if  a >= c: 
#         print(b+a) 
#     else: 
#         print(b+c) 
# else:
#   if a >= b: 
#       print(c+a) 
#   else: 
#       print(c+b)  #5 


#------------------------FRQUENCY-----------------------------finding encoding running length  
#Q- ----------aabbaaaccbb ----->o/p---a2b2a3c3b3 
         
s = "aaabbaaaccbb"
res = s[0]  # start with the first character
c = 1       # counter for consecutive characters

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        c += 1
    else:
        res += str(c) + s[i]  # append count and next character
        c = 1

res += str(c)  # append the count of the last sequence

print(res)   #a3b2a3c2b2 

# 
s =  'aabbaa' 
res = s[0] 
c =1  
for i in range(1, len(s)): 
    if s[i] == s[i-1] : 
       c += 1 
    else: 
        res = res + str(c) + s[i] 
res += str(c) 
print(res)         


