# ---------FUNCTIONS ------------

# how many parameters you passed --- so must and should pass the arguments also when function call time  ok 


# def area_of_a_circle():
#     print('started printing area of a circle') 
#     print(3.14*10*10) 
#     print('Area printed successfully') 

# area_of_a_circle()     


# print('some other tasks performed') 

# area_of_a_circle() 
# print('some other tasks performed')
# area_of_a_circle() 
# area_of_a_circle() 
# area_of_a_circle() 

# def area_of_a_circle(r):
#     print('started printing area of a circle') 
#     print(3.14*r*r) 
#     print('Area printed successfully') 

# area_of_a_circle(10)    

# print('some other tasks performed') 

# area_of_a_circle(20) 
# print('some other tasks performed')
# area_of_a_circle(40) 
# area_of_a_circle(20) 
# area_of_a_circle(22) 

# # -----------MULTIPLE PARAMETERS PASSING ----------------- 

# def area_of_a_circle(r, pie):
#     print('started printing area of a circle') 
#     print(3.14*r*r) 
#     print('Area printed successfully') 

# area_of_a_circle(10,80)    
# area_of_a_circle(20,20)   


# def simple_calculator(num1 , num2): 
#     print(num1 + num2) 
#     print(num1 - num2) 
#     print(num1 * num2) 
#     if num2 != 0:
#         print(num1 / num2) 
#         print(num2 % num2) 
#         print(num1 // num2) 
#     else: 
#         print('division by zero is not possible')    

# simple_calculator(10, 23) 
# simple_calculator(10, 3) 
# simple_calculator(1, 23) 

# def simple_calculator(num1,num2): 
#     print(num1 + num2) 
#     print(num1 - num2) 
#     print(num1 * num2) 
#     if num2 != 0: 
#         print(num1 / num2) 
#         print(num1 % num2) 
#         print(num1 // num2) 
#     else: 
#         print('zero division is not possible')    
# simple_calculator(10,0)        

# def table_printer(num1):
#     for i in range(1,21): 
#         print(num1,'x', i, '=', num1 * i)

# table_printer(12) 
# table_printer(9)        

# def table_printer(num1): 
#     for i in range(1,21): 
#         print(num1, 'x', i, '=' , num1 * i )
# table_printer(9)        

# def sum_of_n_nums(n):
#     sum = 0 
#     for i in range(1, n+1): 
#         sum = sum + i 
#     print(sum) 

# sum_of_n_nums(7)

def factorial_of_n_nums(n):
    f2 = 1
    for i in range(1, n+1): 
        f2 = f2 * i 
    print(f2)  

factorial_of_n_nums(7) 


