# ----------------ARMSTRONG NUMBER----------------- 

#154= 1^3 + 5^3 + 4^3= 1 + 125 + 64 = 190 ----> this is not a armstrong number  ok 
# 153 = 1^3 + 5^3 + 3^3 = 1+ 125+ 27= " 153" ------> this is armstrong number  

# armstrong number -- when we calculate the given number with total digit power with number given to get the same number it becomes arm strong number ok 

#2431 
# num1 = int(input('enter num1:')) #input will be alsways string so 'converting into integr'
# while num1 > 0: 
#     rem = num1 % 10 #2431 % 10 = 1 , 243%10=3 , 24%10=4, 2%10=2, 
#     print(rem) #1342 reverse will come o/p 
#     num1 = num1 // 10  # quetiont reassigning to num1  


#-----
# #243 
# num1 = int(input('enter num1')) 
# sum = 0 
# temp = num1  #243 

# while num1 > 0: 
#     rem = num1 % 10 
#     print(rem) 
#     sum += rem ** 3 # here 3 ^3 , 4^ 3 2^3 = 27+64+ 8 = "99" not an armstrong number  
#     num1 = num1 // 10 # quotient - reassignming to num1 
# print(sum) 
# if temp == sum: 
#     print('Armstrong number')    
# else: 
#     print('Arms weak number')      

# #243 ----same just counting the digits to do power of number --->same just adding 'count' 

# #243 
# num1 = int(input('enter num1')) 
# sum = 0 
# temp = num1  
# count = 0

# while num1 < 0: 
#     count += 1 
#     num1 = num1 // 10 
#     num1 = temp # reassigning temp value  

# while num1 < 0:   
#     rem = num1 % 10 
#     print(rem) 
#     sum += rem ** count  
#     num1 = num1 // 10 # reaasignning 'quotient' 
# print(sum) 

# if temp == sum: 
#     print('Armstrong number') 
# else: 
#     print('Arms weak number')     
#---------------------
#--------same above in string method-------------- 

num1 = int(input('enternum1')) #4321 
str_num = str(num1) 
sum =0 
for i in str_num: 
    sum += int(i) ** len(str_num) 
if sum == num1: 
    print('Armstrong number')    

#------------check prime------------- 

num1 = int(input('enter num1')) 
num2 = int(input('enter num2')) 

def check_prime(input_num): 
    if input_num <= 1: 
        return False  
    for k in range(2, int(input_num ** 0.5 )+ 1): 
        if input_num % k == 0: 
            return False  
    return True
for i in range(num1, num2 +1 ): 
   # res = print(check_prime(i)) ---> we can write like this also ok
    if  check_prime(i): #if Trueonly if block will run ok 
        print(i)  

