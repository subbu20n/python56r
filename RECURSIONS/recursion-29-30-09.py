# -------------------------------RECURSION -----------------ps-----------------ajay sir 

#Q. sum of digits 
1234 #10 
# BIgger problems in terms of smaller problems  

# 4 + sum_of_digits(123)   #  --> big problem ni small ga chestunna  

#sum_of_digits(123) ==> 3 + sum_of_digits(12) 

# 1 + sum_of_digits(2) 
# 2 + sum_of_digits(0) 

# num1 = 1234 

# def sum_of_digits(num1):  #1234 => rem = 4 ==> num1 // 10 ==> 123  
#    # if num1 == 0:         # 123 => rem = 3 ==> num1 //10  ==> 12  
#     if num1 < 1: 
#         return num1          # 12  => rem = 2 ==> num1 // 10 ==> 2  ==> 1==> 1 
    
#     return num1 % 10 + sum_of_digits(num1 // 10)#num1 % 10 = 

# print(sum_of_digits(num1))


#------------- 

#rev('bad morning') ==> 'g' + rev('bad mornin') 

# def rev_string(str1): 
#     if len(str1) <= 1: 
#         return str1 
#     return str1[-1] + rev_string(str1[ : len(str1)-1]) 
#            # g                    bad mornin
# print(rev_string('bad morning'))  #gninrom dab   

#---------------

#Q. -------------Multiply 2 numbers without using '*' star -------------------
#m * n 
# f(m,n)==> m + f(m, n-1) 
# 3 * 5

# def mul(m,n): 
#     if n == 1: 
#         return m 
#     if n == 0: 
#         return 0 
#     return m + mul(m,n-1)   
#          # 3 + mul(3, 5-1=4) = (3,4) => 3 + 12 = 15   
# print(mul(3,5))

#------------
# -------------exponent---------------

# m ** n ==> m * (m ** n-1) 
# f(m,n) ==> return m * f(m, n-1)  

# def exponent(m,n): 
#     if n == 0: 
#         return 1  
#     return m * exponent(m, n-1) 
# print(exponent(3,5)) 

# exponent(3,5) → 3 * exponent(3,4)
# exponent(3,4) → 3 * exponent(3,3)
# exponent(3,3) → 3 * exponent(3,2)
# exponent(3,2) → 3 * exponent(3,1)
# exponent(3,1) → 3 * exponent(3,0)
# exponent(3,0) → 1 (base case) 

# 3 * 3 * 3 * 3 * 3 = 243

#--------------


#Q.--------LIST ptinting reverse order ------------------using subset  

list1 = [1,2,3,4,5,10] 

def rev_list(list1): 
    if len(list1) == 0: 
        return 
    print(list1[-1]) # 10  
    return rev_list(list1[ : -1]) 
rev_list(list1)