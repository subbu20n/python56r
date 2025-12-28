#----------------------RECURSION-----------------------------

#Recursion: A function calling by itself 

# def example(): 

#     print('og ela undi') 
#     example() # here again calling the function 'it goes above and prints 999 times exceeded' 

# example()     

# num1 = 0 

# def example(): 
#     global num1 
#     num1 += 1  
#     print(num1) 
#     print('og ela undi') 
#     example() 

# example()

# o/p 

# 998
# og ela undi
# 999
# og ela undi 

#---------------------------26-09-2025-----------------------


# count = 0 

# def example(): 
#     global count  
#     count += 1  #999  times runs and throw as error exceeded 
#     print(count) 
#     example() 

# example() 

#----------
# count = 0 

# def example(): 
#     global count 

#     if count >= 3: 
#         return 
#     count += 1 
#     print(count)
#     example() 

# example()

# o/p 
# 1
# 2
# 3

#-------

# def sample_function(n): 
#     if n < 1:
#         return 
#     print(n)
#     sample_function(n-1) 
#     #print(n)

# sample_function(10)

# o/p 

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
#-----------

# def sample_function(n): 
#     if n <= 1: 
#         return 
#     print(n) 
#     sample_function(n-1)
#     print(n) 

# sample_function(10)

# o/p 

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 2  # first person will go last  # waitng for 3 
# 3  # last person wil go first only  
# 4
# 5
# 6
# 7
# 8
# 9
# 10 


# --------------------------FACTORIAL OF A NUMBER-----------------
# 5 factorial => 120 
# 5! = 5 * 4! ----> if you want 5! you want first 4! ok 
# 4! = 4 * 3! ----> if you want 4! you want first 3! 
# 3! = 3 * 2! ----> if you want 3! you want first 2! 
# 2! = 2 * 1! ----> if you want 2! you want first 1!  
# 1! ===> directly return the value '1'  --> we know 'base condition right' 


def fact(n): 
    if n == 1: 
        return 1 
    # prev_value = fact(n-1) # here assigned varible 
    # return n * prev_value 
    return n * fact(n-1)
print(fact(5))  #120