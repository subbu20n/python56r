# def check_num_input(num1): 
#     if num1 > 0: 
#         print('positive') 
#     else: 
#         if num1 == 0: 
#             print('zero') 
#         else: 
#             print('Negative')  

# num_input = int(input('enter num1:')) 
# check_num_input(num_input) 


#-------using "return" -------------

# def check_num_status(num1): 
#     if num1 > 0: 
#         return('positive') 
#     else: 
#         if num1 == 0: 
#             return('zero') 
#         else: 
#             return('Negative') 

# num_input = int(input('enter a number'))  
# result = check_num_status(num_input)   
# print(result) 

# ---------------TERMINATORY OPERATOR------------------------
#---------Determine given number is a odd or even  -----------****

# def even_or_odd(num1): 
#     res = 'EVEN' if num1 % 2 == 0 else 'ODD'    
#     print(res) 
# even_or_odd(4)    

# def even_or_odd(num1): 
#     res = 'EVEN' if num1 % 2 == 0 else 'ODD' 
#     print(res) 
# even_or_odd(20)     


# # -------------check if a person is eligible to vote (age >=18) --------- ****

# def check_greater(num1,num2): 
#     return num1 if num1 > num2 else num2   
# print(check_greater(18,17)) 

# def check_greater(num1, num2): 
#     if num1 > num2: 
#         return num1 
#     elif num1 == num2: 
#         return 'both are equal' 
#     else:
#         return num2 
# print(check_greater(10,80))    

# def check_higher(num1,num2): 
#     if num1 > num2: 
#         return num1 
#     elif num1 == num2: 
#         return "both are equal"  
#     else: 
#         return num2  
# res = print(check_higher(10,90))    

# -----using terminary operator - same above only 
# def check_greater(num1,num2): 
#     return num1 if num1 > num2 else 'both are equal' if num1 == num2 else num2 
# print(check_greater(10,10))

# #---- implemnet a simple calculator ADDITION, SUBSTRACTION,DIVISION,MULTIPLICATION ----****

# def simple_calc(n1,n2,op): 
#     if  op == '+': 
#         print(n1+n2) 
#     elif op == '-': 
#         print(n1-n2) 
#     elif  op == '*': 
#         print(n1 * n2) 
#     elif op == (n1/n2): 
#         print(n1 / n2)  if n2 != 0 else print('not possible')
# num1 = float(input('enter num1'))  
# num2 = float(input('enter num2'))    
# input_op = input('enter operation')
# simple_calc(num1,num2,input_op) 

# def simple_calc(n1,n2,op): 
#     if  op == '+' or op == 'add':     #if  op == '+' or 'add':  ()'add') wont give like this # or (op == 'add' )
#         print(n1+n2) 
#     elif op == '-' or op == 'sub': 
#         print(n1-n2) 
#     elif  op == '*' or op == 'mul': 
#         print(n1 * n2) 
#     elif op == (n1/n2) or op == 'div': 
#         print(n1 / n2)  if n2 != 0 else print('not possible')
#     else:
#         print('invalid input')    
# num1 = float(input('enter num1'))  
# num2 = float(input('enter num2'))    
# input_op = input('enter operation')  # here we can perform add , sub,mul,div instead of this [+,-,*./]
# simple_calc(num1,num2,input_op) 

#--------same abouve code using "MEMBERSHIP OPERATOR" ----------------

def simple_calc(n1,n2,op): 
    if op in ['+', 'add', 'ADD']: 
        print(n1+n2) 
    elif op in ['-', 'sub','SUB']:  
        print(n1-n2) 
    elif op in ['*', 'mul', 'MUL']: 
        print(n1*n2) 
    elif op in ['/' , 'div', 'DIV']: 
        print(n1 / n2) 
    else: 
        print('invalid input') 

num1 = float(input('enter num1'))  
num2 = float(input('enter num2'))    
input_op = input('enter operation').lower() # here we can perform add , sub,mul,div instead of this [+,-,*./]
print(input_op)                       #.lower() if u provide "capital letters" i will convert to "small letters"
simple_calc(num1,num2,input_op)            






