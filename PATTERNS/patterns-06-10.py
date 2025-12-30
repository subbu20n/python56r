#--------------------------patterns------------------------------

# print('*' * 5)  #* * * * * # it works in python and java only remaining languages wont works  

# n = 5 
# for i in range(n): # outer loop for row value  
#     for j in range(n): # inner loops for column value  
#         if i == n // 2 : 
#          print('*', end=' ') 
#     print()     #* * * * *  

# n = 5 
# for i in range(n): 
#     for j in range(n): 
#         if j == n // 2: 
#             print('*', end=' ')
#         else: 
#             print(' ', end=' ')     
#     print()    

    # *     
    # *     
    # *
    # *
    # * 

#-------------------

# n = 5  
# for i in range(n): 
#     for j in range(n): 
#         if i >= j: 
#             print('*', end=' ')
#         else:
#             print(' ', end=' ') 
#     print()            

# *
# * *       
# * * *
# * * * *
# * * * * * 

#--------------------- 

# n = 5 
# for i in range(n): 
#     for j in range(n): 
#         if i <= j: 
#             print('*', end=' ')
#         else: 
#             print(' ', end=' ')
#     print() 

# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         * 
               
#---------------------

# n = 5 
# for i in range(n): 
#     for j in range(n): 
#         if i <= j or i+j == n-1 : 
#            print('*', end=' ') 
#         else:
#             print(' ', end=' ') 
#     print()           

# * * * * * 
#   * * * * 
#     * * * 
#   *   * * 
# *       *     

#--------Hallow square----------------
n = 5 
for i in range(n): 
    for j in range(n): 
        if i == 0 or i == n - 1 or j == 0 or j == n-1 : 
            print('*', end=' ') 
        else: 
            print(' ', end=' ') 
    print()             