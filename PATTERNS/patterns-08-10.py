#---------------------PATTERNS------------------------------

#  i >= j 

# n = 7 
# mid = n // 2 

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
# * * * * * *   
# * * * * * * *  

# ---- we need to get pyramid ----- 

# n = 7  
# mid = n // 2 

# for i in range(n): 
   
#     for sp in range(n - i - 1): 
#             print(' ', end='') 
#     for  j in range(n):
#         if i >= j:
#              print('*', end=' ')
#         else: 
#              print(' ', end=' ')
#     print()

#       *
#      * *
#     * * *
#    * * * *       
#   * * * * *     
#  * * * * * *   
# * * * * * * *     


#-------------

# n = 7 
# mid = n // 2
# for i in range(n): 
#      for sp in range(i): 
#           print(' ', end='')# for end wont give spaces ok 
#      for j in range(n): 
#           print('*',end=' ')    
#      print()      

# * * * * * * * 
#  * * * * * * * 
#   * * * * * * * 
#    * * * * * * * 
#     * * * * * * * 
#      * * * * * * * 
#       * * * * * * *      

#------------

# n = 4 
# mid = n // 2 

# curr = 0 
# for i in range(n): 
#     for sp in range(n - i - 1): 
#         print(' ', end='') 
#     for j in range(n): 
#         if i >= j: 
#             print(curr, end=' ') # we need to write if-block only 'curr' + 1 
#             curr += 1

#         else: 
#             print(' ', end=' ') 
#     print()                

#    0       
#   1 2     
#  3 4 5   
# 6 7 8 9   


#------------
    
# n = 4 
# mid = n // 2 

# for i in range(n): 
#     curr = 1
#     for j in range(n): 
#         if i >= j: 
#             print(curr, end=' ') 
#             curr += 1
#         else: 
#             print(' ', end=' ') 
#     print()            

# 1       
# 1 2     
# 1 2 3   
# 1 2 3 4 

#----------same code just change 'curr' inside there and here 'outside' ok 

# n = 4 
# mid = n // 2 
# curr = 1  
# for i in range(n):
#     for j in range(n): 
#         if i >= j: 
#             print(curr,end=' ') 
#             curr += 1 
#         else: 
#             print(' ', end=' ') 
#     print() 

# 1       
# 2 3     
# 4 5 6   
# 7 8 9 10                 

#---------- 

# n = 4 
# mid = n // 2 

# for i in range(n): 
#     for sp in range(n - i - 1): 
#         print(' ', end='') 
#     for j in range(n): 
#         if i >= j: 
#             print(i+1, end=' ')  # just added equation here 'i+1' ok 
#         else: 
#             print(' ', end=' ') 
#     print()           

#    1       
#   2 2     
#  3 3 3   
# 4 4 4 4          

#------------------Butterfly star pattern-----------------

# n = 7 
# mid = n // 2 
# for i in range(n):
#     for j in range(n): 
#         if ((i >= j) and (i+j <= n - 1) or (i <= j) and (i+j >= n - 1)): 
#             print('*', end=' ') 
#         else: 
#             print(' ', end=' ') 
#     print()            

# *           * 
# * *       * * 
# * * *   * * * 
# * * * * * * * 
# * * *   * * * 
# * *       * * 
# *           * 

#--------------------Pascals---------------- right 

n = 7 

for i in range(n): 
    if i % 2 == 0 : 
        visible = True 
    else: 
        visible = False 

    for j in range(n): 
        if ((i >=j ) and (i+j <= n - 1 )):  
           if visible == True:
              print('*', end=' ') 
              visible = False  
           else:  
             print(' ', end=' ') 
             visible = True
        else: 
           print(' ',end=' ')       
    print()             