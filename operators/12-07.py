#-------OPERATORS-------  

# Arithmetic oprators  -:  +, -, *, /, //, %, ** 
# Assignment operators -: =, +=, -= 
# Relational operators -: ==, <, >, <=, >= , != 
# Membership operator  -: IN , Not IN 
# Logical operators    -: AND , OR , NOT 
# Bitwise operator     -: &, |, ^, ~, !, <<, >> 



#  ----Arithmetic operators----
#       +, -, *, /, //, %, ** 

#---BODMAS --- 
#print(2 + (3*5)) #17

# num1 = 0 
# num2 = 5 # in division denominator could not be zero ok 

# print((2**3) * (3 - (6 // 2))) 
#print((2 ** 3) * (3- (6 //2 )))  #0  2x2x2x=8 * 0=0 

# -------Assignment operators ------- 
#         =, +=, -= 

# num1 = 6 
# num1 = 5.6  #reassignment  
# print(num1) #5.6 
# num1 = 5  #reassignment 
# print(num1) #5 

# num1 = float(num1) #reassign #5.0 
# print(num1) #5.0 

# num1 = 5 

# num1 = num1 + 3 ==>both same==> num1 += 3  ---> this is short hand 
# num1 = num1 + 3 #5+3 = 8 
# print(num1)

#  num1 += 3 #8+3=11
#  print(num1) #11 

# num1 -= 3 #11-3=8 
# print(num1) #8 

#-------Relational operators -------- 
#       ==, <, >, <=, >= , != 
#  print(2>3)
#  print(2==3)
#  print(2<=3) 
#  print(22 == '22')
#  print('a' == 3)
#  print(2>3) == (3<5)  #false*true=false 
#  print(2>5) == (3 <= 5) 
#  print('a' == 3)

 #!= 
# print(3 != 3)
# print(4 != 8)
# print(3 != 'a') 


# print('abc' > 'ba')
# print('abc' > 'abb')

#------Membership operator----- 
#      IN , Not IN  
# print(31 in range(0,33)) 
# print(3 in [1,3,4,5])
# print(3 not in [2,5,7,8])
# print(6 in (1,5,8,9)) 
# print(4 not in (2,7,0)) 

print(30 in range(0,20)) 
print(11 in range(2,15))
print(13 not in range(2,16))

# dict1 = {
#     1: "subbu",
#     2: "subbu"
# }

# print(1 in dict1)
# print('1' in dict1) 

dict = {
    1: 'subbu',
    '1': 'sai',
    4: 'sai'
}

print(1 in dict) 
print(sai in dict)