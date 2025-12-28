#-------------------------FIBONACCI-----using recursion------------------------

# 0,1,2,3,4,5 

#f(n) = f(n-1) + f(n-2) 
# 6 =  5 - 1 + 5 - 3 = 4+ 2 = 6 

def fib(n): 
    if n == 0 :
        return 0 
    if n == 1: 
        return 1
        
    return fib(n-1) + fib(n-2)  

# Step-by-step execution for fib(6)
# print(fib(6))

# fib(6)
# = fib(5) + fib(4)

# fib(5)
# = fib(4) + fib(3)

# fib(4)
# = fib(3) + fib(2)

# fib(3)
# = fib(2) + fib(1)

# fib(2)
# = fib(1) + fib(0)
# = 1 + 0 = 1

# fib(3) = 1 + 1 = 2
# fib(4) = 2 + 1 = 3
# fib(5) = 3 + 2 = 5
# fib(6) = 5 + 3 = 8   


#--------

# ----------------------PALINDROME------------------------

# If a string is palindrome  
# str1 = 'MALAYALAM' 
# print(str1[:: -1] = str1) 
# str1 ==> first_elem == last__elem and (remaining string also should be palindrome) 

str1 = 'MALAYALAM' 

def palindrome(str1): 
    if len(str1) <= 1: 
        return True 
    return (str1[0] == str1[-1] and palindrome(str1[1 : -1])) 
print(palindrome(str1))

