#  LOGICAL OPERATOR ---> AND, OR , NOT 
#  BITWISE OPERAOTR ---> &, | , ^ , << , >> , ~ 

# print(2 and 3 ) 
# print(0 and 5)  #operands will return (any one operand)
# print(2 and 6) 
# print( 4 and -5) 
# print(2 or 7) #2 

# ---bitwise operator----- 
 
# # 2 --> 0010 
# # 3 --> 0011 => 2
# print(2 & 3)   #2 

# #12 --> 01100 
# #22 --> 10110 
# print(12 & 22) #4 


# #12 --> 01100 
# #22 --> 10110 
# print(12 | 22)  #30  


# #12 --> 01100 
# #22 --> 10110 
# print(12 ^ 22) #26 xor become 0,0 =0 1,1,=0 0,1=1 

#LEFT SHIFT and RIGHT SHIFT 
#LEFT SHIFT --> moves from right to left one bit  if even number give it 5*2=10 
#RIGHT SHIFT --> moves from left to right and we omit the last bit because we didnt have space it gives odd number means 25-1/2=12 .
print(5 << 1)      #5*2=10 
print(10 >> 1)      #10/2=5 
print(20 << 1)      #20*2=40 
print(11 >> 1)      #11-1/2=5
print(44 << 1)      #44*2=88
print(23 >> 1)      #23-1/2=11 
  
#LEFT SHIFT 
print(5 << 1) 

#5-->  0101 --> 5 
#     01010 -->10 #will be the answer (5*2=10) 

#RIGHT SHIFT 
print(23 >> 1) 
#23 --> 10111--> this one we omit(removed) will not space 
#        1011 --> #11  (23-1/2=11)

# ~ (NOT) or ones compliment 
#  for not when we give number to add +1 and chnging signs if (+) is there chnage to (-)
print(~5) #5+1=6 
print(~10) #10=1=11 
print(~-12) #-12+1=11 

#IDENTITY OPERATORS ==> [IS , is not]
#When we declare the value is there means it show "true"

num1 = 10 
num2 = 10 

print(id(num1), id(num2)) # it gives same id 
print(num1 is num1) 

num1 = 10
num2 = '10' 

print(num1 is num2) #false
print(id(num1), id(num2)) 
print(num1 is not num2)#true 



