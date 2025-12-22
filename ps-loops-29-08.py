#-----------------problem solving on loops-------------------

#-------------reversing a number------------------- 

#1542 
#2451 

# num1 = 2451 
# temp = num1 

# while num1 > 0: 
#     digit = num1 % 10 
#     print(digit) 
#     num1 = num1 // 10 # reassigning a quotient to 'num1'  #1542   

# num1 = 2451

# rev_num = 0 

# while num1 > 0:
#        digit = num1 % 10  #1,#5,#4,#2, 
#        rev_num = rev_num * 10 + digit   #0*10+1=1 , 1*10+5= 15, 15*10+4=154, 154*10+2 = 1542 
#        print(digit) 
#        num1 = num1 // 10 #245 ,#24,#2,# 
# print(rev_num)       # 1542 

# temp = 1241
# print("palindrome" if rev_num == temp else "not a palindrome")

# #----------------------PALINDROME----------------------------- 
# # 121 ---> To this revere will do it gets same number right  ---> so its a palindrome  

# temp = 1241
# print("palindrome" if rev_num == temp else "not a palindrome")


#------------------------------SWAPPING---------------------

#SWAPPING: for 'num1' num2' both have corresponging values ---> when we do swapping num1 values goes to num2 --> num2 values comes to num1
#num1 values ---> goes to num2 
# num2 values --> comes to num1  


# --swapping-- 
# num1 = 10 
# num2 = 20 

# # num1 = num2 
# # num2 = num1 # this wont work 
# # print(num1) 
# # print(num2) 

# #---------METHOD-1------------------ 

# num1, num2 = num2 , num1  

# print(num1) 
# print(num2) 

#-----METHOD-2----------------
# #using 3rd variable "temp" 

# num1 = 10  
# num2 =20 

# temp = num2 
# num2 = num1  # reassigning num1 value to num2  
# num1 = temp #reassignmning temp value to num1
# print(num1 , num2)  # num1 =20 , num2 = 10 -->swapping  happend 'changed values' 

# #-----------------method-3---------------------------- 

# num1 = 10 
# num2 = 20 

# num1 = num1 + num2 #30 --> 10+20=30 
# num2 = num1 - num2 # 10 --> 30-20=10 
# num1 = num1 - num2  #10 -->30-10 =20   

# print(num1) #20 
# print(num2) #10 

#----------------METHOD-4------["XOR-property"]------------------- 

# if we have 2 smae bits it becomes zero 
# if we did not have 2 same bits it becomes 1 

#x = 5 
#5 ^ 0 = 5 only  

# print(x ^ x) #----> 0 
# print(x ^ 0) #-----> x  

num1 = 10 
num2 = 20 

#10-01010 
#20-10100  

num1 = num1 ^ num2  #(10 ^ 20) 
num2 = num1 ^ num2  # 
num1 = num1 ^ num2  

print(num1) 
print(num2) 