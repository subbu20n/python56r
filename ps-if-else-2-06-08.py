# num1 , num2, num3 = 1,4,5 

# if num1 > num2 and num1 > num3 : 
#     print(num1) 
# elif num2 > num1 and num2 > num3: # here wont write like this (elif num2 > num1 and num2 > num3:)==> num2 > num3 
#     print(num2) 
# else: 
#     print(num3)         

# num1 , num2, num3 = 6,4,2

# if num1 > num2 and num1 > num3 : 
#     print(num1) 
# elif num2 > num1 and num2 > num3: # here wont write like this (elif num2 > num1 and num2 > num3:)==> num2 > num3 
#     print(num2) 
# else: 
#  print(num3)             

# check IF a year is leap year 

# def leap_year(year): 
#    if year < 0: 
#       return 'invalid year' 
#    elif year % 400 == 0: 
#       return 'Leap Year' 
#    elif year % 400 != 0 and year % 4 == 0: 
#       return 'Leap year' 
#    else: 
#       return 'Not a leap year' 
# input_op = int(input('enter year'))    
# print(leap_year(input_op)) 

def leap_year(year): 
   if year < 0: 
      return "invalid year" 
   elif year % 400 == 0: 
      return 'leap year' 
   elif year != 400 and year % 4 == 0 : 
      return 'leap year' 
   else: 
      return 'not a leap year' 
input_sub = int(input('enter')) 
print(leap_year(input))    

