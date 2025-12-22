#------CONTROLFLOW STATEMENTS---------

#1.Conditional statement --> if, else, elif-->(else if) 
#2. Loops --> for, while 
#3. Jump statements --> break, continue and pass 

#Indentation 

# ------1.Conditonal statements ----- 
# ----IF----- Else-----elif---- 

# --IF-- 
# age = 19 

# if age >= 18: 
#     print('I can vote')
#     print('Dabbulu vastay') 

# if age <= 18: 
#     print('I cannot vote')  


# num1 =20 

# if num1 % 2 == 0: 
#     print('EVEN') 

# if num1 % 2 != 0: 
#     print('Odd') 

# str1 = 'python' 
# if len(str1) > 10: 
#     print('password is strong') 

# if len(str1) <= 10: 
#     print('password is weak')  

# # str1 = 'python' 
# # l = len(str1) 

# # if l > 10: 
# #     print('l')

# # if 1 < 10:
# #     print('1') 

# ----IF-ELSE-------- 

# age = 19 
# if age <= 18: 
#     print('I can vote') 
#     print('dabbulu vastayi') 
# else: 
#     print('I cant vote') 
        


# num1 = 1 

# if num1 > 0 : 
#     print('positive') 
# else: 
#     print('negative')    

num1 = 0 
if num1 > 0: 
    print('positive') 
else: 
    if num1 == 0: 
        print('zero') 
print('Negative')            
   

#********-------18-07.py  -------*****


# ----------nested if-else -------------


num1 = 0 

if num1 >= 0 : 
    print('positive') 
else: 
    if num1 <= 0:
        print('zero') 
    else: 
        if num1 == -1: 
            print(-1) 
        else: 
            print('Negative')             

# -----elif--------- 

num1 = -1 

if num1 > 0: #--> generic condition 
    print('positive') 
elif num1 == 0: 
    print('zero') 
elif num1 == -1: 
    print('-1') 
else: 
    print('Negative') 

num1 = 5

if num1 > 0:  # --> generic condition 
    print('positive') 
elif num1 == 5: 
    print('5 star') 
elif num1 == 0: 
    print('zero') 
elif num1 == 6: 
    print('6 star') 
else: 
    print('Negative')                 

num1 = 6 

if num1 == 5: # ---> specific condition 
    print('5 star') 
elif num1 == 6: 
    print('6 star') 
elif num1 > 0:     #----> specific condition 
    print('positive') 
elif num1 == 0: 
    print('zero') 
else: 
    print('Negative')                

marks = 61

if marks >= 90: 
    print('Grade A') 
elif marks >= 75:  
    print('Grade B') 
elif marks >= 60: 
    print('Grade C') 
elif marks >= 40: 
    print('Grade D') 
else: 
    print('fail') 

# --------Nested if else ------ 

units = float(input('Enter units')) 

if units >= 100: 
    print(0) 
else: 
     if units <= 200:
          print(units * 1) 
     else: 
         if units <= 300: 
             print(units * 2) 
         else: 
             if units < 400: 
                 print(units * 3) 
             else: 
                 print(units * 5)         

