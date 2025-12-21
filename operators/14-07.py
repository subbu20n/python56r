#Operators 
#Arithmetic operators
# +, -, /, *, //, %, **

#Assignment operators 
# =, +=, -=

#Relational operator 
# ==, < , >, <=, >= !== 

#Membership operator 
#IN , Not IN 

#print(2 in [1,2,4]) 
#print(22 in [23,45,[22,89,0]])  # here we need to see the main list not in inside the list of sublist 

#------Logical Operators------
#       AND , OR, NOT 

# given 1st input is 'true'. depends on 2nd input 
#given 1st input is 'fasle' . O/P is FALSE  

# print(True and True) 
# print(True and False) 
# print(False and False) 

# print(True and(False and (True and (True and False)))) #false -here once we get false false it damn sure it becomes false only 
# print(True and (True and  (False and (True and False )))) 
# print(2 and 3) 
# print(0 and 3) 
# print('' and 'balayya')  #empty string  vastundi  
# print(False and False) #false 


# ----OR-----  
# # in this (or) gate only one operand will be true it becomes true 

# print(True or False) #true 
# print(True or True) #true 
# print(False or False) #false  

# print(2 or 3) 
# print(-5 or 2) 
# print(7 or 'a') 
# print(2 or 3) 
# print(2 or -5) 
# print(-5 or 3) 
# print(0 or 8) 
# print([] or '') #empty string  

# -----NOT-------
#  
# print(not True)
# print(not False) 



#-------BITWISE OPERATOR --------
#5 ==> 0101 
#7 ==> 0111 

print(5 & 7)  #5 

#9 = 1001 
#11 = 1011
print(9 & 11)  #9 

#9 = 1001 
#3 = 0011
print(9 & 3) #1

print(bin(11))
print(oct(11)) 
print(int(0b1011))  # it will convert to integer it becomes '11'  
print(int(0b1111))
print(oct(0b1111)) 

print(0x1A) #26 0x = hexa=16 --> 1x16=16 + A =10 = 26 . 26/16 = 10 remainder, 1 is quotient 
print(int(0o1111)) #17 ==>1111=15, 0o = octa=8 --> 15/8=7 is remainder 1 is quotient =17 

#22 = 10110
#11 = 01011 
print(22 & 11) #2 

#OR  

#22 = 10110
#11 = 01011 = 11111=31
print(22 | 11) #31 

#XOR 
# in this same bits becomes '0' 0,0=0 , 1,1=0 1,0=1 
# in this different bits become 1,0 =1 
#22 = 10110
#11 = 01011 = 11101 = '29'
print(22 ^ 11) #29 

print(oct(11))