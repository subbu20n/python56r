#-----------------------------Time complexity---------------------------------

# time = number of iterations  we measured 

#by "time" we cannot define which code is more efficient  
# t1 > t2 --> we have A and C -- codes A codes  executes 0.012 seconds(t1) --> B-code executes in 0.8 secondes(t2) 

#-------Linear Time complexity --------------
# o(n) 

#10 = 10 
# 100 = 100 
# 1000 = 1000
# n = 10 
# sum = 0 

# for i in range(1, n+1):  # 10 iterations 
#     sum += i    

# print((n * (n+1))//2) # 3 iterations     



# # ------COnstant Time complexity ( time will be constant) -----------
# # o(1)
# print((n * (n+1))//2) # 3 iterations 


# n=10 

# for i in range(n): 
#     for j in range(1,n): 
#         print(i+j)  

# n =10 = 100 # 10*10 = 100 # here time will be constnat  sir 
# n = 20 = 400 
# n = 100 = 10000 #100*1000=10000        

#----------DAY-60---------------(TIME COMPLEXITY)-------------

# TIME is more 'efficiency is less' 
# Time is less 'efficiency is more' 

# n = 10 
# m = 20 

# for i in range(1, n+1): 
#     for j in range(1, m+1): 
#         print(i+j)  

#0(m*n) 
# #0(logn)---> binary search  
#0(nlogn) --> optimized buble sort 
#0(n2logn) 

#TIME ==> 0(1) < 0(logn) < 0(n) < 0(nlogn) < 0(n2) < 0(n3) 
# efficiency ==> 0(1) > 0(logn) > 0(n) > 0(nlogn) > 0(n2) > 0(n3) 

# | Complexity | Time growth       | Example             |
# | ---------- | ----------------- | ------------------- |
# | O(1)       | Constant          | arr[0]              |
# | O(log n)   | Slow              | Binary search       |
# | O(n)       | Linear            | Linear search       |
# | O(n log n) | Medium            | Merge sort          |
# | O(n²)      | Fast growing      | Bubble sort         |
# | O(n³)      | Very fast growing | Triple nested loops |

# | Complexity | Growth    | Example                      |
# | ---------- | --------- | ---------------------------- |
# | O(1)       | Constant  | Accessing an array element   |
# | O(n)       | Linear    | Single loop over n items     |
# | O(n²)      | Quadratic | Nested loop over n × n items  


# O(1) – Constant time

# Number of steps does not change with input size.

# Always the same, no matter how big n is.
# Iterations
# ^
# | *
# | *
# | *
# | *
# +-----------------> n
#Example: arr[0] or n*(n+1)//2 


#---------

# O(n) – Linear time

# Number of steps grows proportionally with n.

# Double n → roughly double iterations.
# Iterations
# ^
# |       *
# |      *
# |     *
# |    *
# |   *
# |  *
# | *
# +-----------------> n
# Example: for i in range(n): print(i)

#---------
# O(n²) – Quadratic time

# Nested loop over same n → grows much faster.

# Double n → iterations quadruple.

# Iterations
# ^
# |               *
# |             *
# |           *
# |         *
# |       *
# |     *
# |   *
# | *
# +-----------------> n
#ex:
# for i in range(n):
#     for j in range(n):
#         print(i+j)


# num1 = 24  

# for i in range(2,num1): 
#     if num1 % i == 0: #24 % 2 == 0  condition satisfied (print -not prime) 
#         print('Not prime') 
#         break 
#  #not prime 

# num1 = 17  

# for i in range(2,num1): 
#     if num1 % i == 0: # 15 iterations hppens here  
#         print('Not prime') 
#         break 

# #
# num1 = 4567 

# while num1 > 0: 
#     digit = num1 % 10 
#     num1 //= 10 
#     print(digit)  #7654  #num1 is constant so only 4 iterations hapeened  

#----------------------------SPACE COMPLEXITY----------------------------

# space complexity: we will talk here about "memory"
# time compexity: we will talk about "operations" 

#space complexity: repeated elements i dont want to print - it want to checks is it printed already for every element we need to check  
#cpu - access ram  

#RAM : faster,cost, volatile--if your code executes then the file will delete 
#ROm : slow, cheap, non-volatile--> once u save the file unless you delete it wont deletes 

# 0(n) space complexity --> worst case 
# 0(1)  space complexity best case  

# | Complexity Type | Complexity | Reason                              |
# | --------------- | ---------- | ----------------------------------- |
# | Time            | O(log n)   | Iterates once per digit             |
# | Space           | O(1)       | Only a few variables used, constant |

#----------- exmples---------

# num1 = 4567

# while num1 > 0:
#     digit = num1 % 10
#     num1 //= 10
#     print(digit)

# Time Complexity – O(log n)

# Number of iterations = number of digits in num1

# Number of digits ≈ log10(num1)    

# Iterations (time)
# ^
# |        *
# |       *
# |      *
# |     *
# |    *
# |   *
# |  *
# +-----------------> num1 size (n)

# As num1 grows larger, the number of iterations increases logarithmically

# Example:

# num1 = 4567 → 4 iterations

# num1 = 456789 → 6 iterations

#----------

# Space Complexity – O(1)

# Variables used: num1, digit

# No extra storage grows with input → constant space

# Memory used (space)
# ^
# |  *
# |  *
# |  *
# +-----------------> num1 size (n)
# Space does not increase as num1 grows

# Always just a couple of variables → O(1)

#----------

# list1 = [10,20,30,40,50,20,30] 

# visited = set () 
# for i in list1: 
#     if i not in visited:  
#         print(i, 'first time visited')
#         visited.add(i) 
#     else: 
#         print(i, 'already visited')     


# if you are trying to do  decrease the time -- memory consumption will increase 
# if you are trying to do decrease  memory consumption --- time will increses 

#here also same when input increses 10 times -memory also increse 100 times 0(n2)-like same of time complexity 


#------------------------float(inf)---------------------

# positive element find out --> float(-inf)
# Negative element find out --> float(inf) 

# -inf  -------------------  0  -------------------  inf 

#-∞ < ... < -2 < -1 < 0 < 1 < 2 < ... < ∞

# float('-inf') → far left, smaller than any number

# 0 → middle, normal numbers

# float('inf') → far right, bigger than any number

list1 = [-1,-2,-3,-4,-5,-9,-32,-45] 

max_elem = 50
# min_elem = -20 
max_elem = float('-inf') 
for i in list1: 
    if i > max_elem: 
        max_elem = i 

    # if i < min_elem: 
    #     min_elem = i     

    print(max_elem)
    # print(min_elem)   
