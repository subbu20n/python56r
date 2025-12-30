#--------------------PATTERNS-----------------------------
#---------- D ---------

# n = 5 

# for i in range(n): 
#     for j in range(n): 
#         if i == 0 or i == n-1 or j == 0 or j == n - 1 : 
#             if (i == 0 and j == n - 1) or (i == n-1 and j == n-1): 
#                 print(' ', end=' ')
#             else: 
#                 print('*', end = ' ')    
#         else: 
#             print(' ', end= ' ')
#     print()                

# * * * *   
# *       * 
# *       * 
# *       * 
# * * * *   

#-------------G--------

# n = 5  
# mid = n // 2 

# for i in range(n): 
#     for j in range(n): 
#         if (i == 0 or i == n - 1 or j == 0  or (j == n-1 and i >= mid) or (i == mid )): 
#             print('*', end=' ') 
#         else: 
#             print(' ', end=' ')    
#     print()        

# * * * * * 
# *
# * * * * * 
# *       * 
# * * * * * 

#---------------------K------------------

# n = 7 
# mid = n // 2 
# for i in range(n): 
#     for j in range(n): 
#         if j == 0  or i + j == n-1: 
#             print('*',end = ' ') 
#         else: 
#            print(' ', end=' ') 
#     print()              

# for i in range(1,n): 
#     for j in range(n): 
#         if j == 0 or i == j : 
#             print('*', end=' ') 
#         else: 
#             print(' ',end=' ') 
#     print()                

# *           * 
# *         *   
# *       *     
# *     *       
# *   *
# * *
# *
# * *
# *   *
# *     *       
# *       *     
# *         *
# *           *    

#--------------------------

# n = 7 
# mid = n // 2 
# for i in range(n): 
#     for j in range(n): 
#         if (j == 0 or j == n-1 or i == j or i + j == n - 1):
#             print('*', end=' ')
#         else: 
#             print(' ', end=' ')
#     print()            


# *           * 
# * *       * * 
# *   *   *   *   # we can get with this M , W  
# *     *     * 
# *   *   *   * 
# * *       * * 
# *           * 

#----------------------------Q-----------------------

n = 7 
mid = n // 2 

for i in range(n): 
    for j in range(n): 
        if (i == 0  or i == n-1 or j == 0 or j == n-1 or  (i == j and i >= mid) ): 
            print('*', end=' ')
        else: 
            print(' ', end=' ')
    print()            

for i in range(n + 1): 
    if i == n: 
        print('*', end=' ') 
    else: 
        print(' ', end=' ')     
print()        