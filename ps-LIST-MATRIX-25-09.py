#---------------------ps---LIST MATRIX ------------------Ajay sir 

# list1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for i in range(len(list1)): 
#     for j in range(len(list1[i])): 
#         print(list1[i][j], end=' ') 
#     print()       
# # 1 2 3  0/p  
# # 4 5 6 
# # 7 8 9    
# #-----------

# #----------- if you want 1st row ---------------

# list1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for i in range(len(list1)): 
#     for j in range(len(list1[i])): 
#         if i == 0: 
#             print(list1[i][j], end=' ')
# print()    
# #1 2 3  -o/p 

# ---------------similarly 1st column if you want ---------------
# list1 = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ] 

# for i in range(len(list1)): 
#     for j in range(len(list1[i])): 
#         if j == 0: 
#             print(list1[i][j], end=' ') 
# #1 4 7  -o/p   

#-------------DIAGONAL EQUATION---------------------------- 
# primary diagonal right side [i=j] 

# list1 = [   #[i=j] 
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ] 

# for i in range(len(list1)): 
#     for j in range(len(list1[i])): 
#         if i == j: 
#             print(list1 [i][j], end=' ')  
#         else: 
#             #print ('$' ,end=' ')  
#             print(' ', end=' ')    
#     print()    

# # 1     o/p 
# #   5   
# #     9 

#----------left side diagonal [i+j=n-1] --------------

#secondry diagonal [i+j=n-1] 

# list1 = [   #[i=j] 
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ] 

# n = len(list1) 
# sum = 0 

# for i in range(len(list1)): 
#     for j in range(len(list1[i])): 
#         if i == j or i + j == n - 1: 
#             sum += list1[i][j]
#             print(list1 [i][j], end=' ')  
#         else: 
#             #print ('$' ,end=' ')  
#             print(' ', end=' ')    
#     print()    

# print(sum)    

# 1   3 o/p
#   5   
# 7    9 

#------------identity MAtrix-----------

#1 
#  1 
#    1  

#--------------UNIQUE MATRIX --------------

#1 
#1 
#1 

#----------------------Transpose MATRIX-------------- 
# ROWS will become columns  
# COLUMNS will become rows 

# we need to do the swapping   #(a,b=b,a) 

# i/p         o/p 
# 1 2 3       1 4 7 
# 4 5 6       2 5 8 
# 7 8 9       3 6 9 

# [i][j] [j][i] = [j][i], [i][j] 
# a, b , = b, a 


# list1 = [         # diagonal matrix [i=j] 
#     [1,2,3,4],    # below diagonal [i>j] 
#     [4,5,6,4],    # above diagonal [i<j] 
#     [7,8,9,4]     # "i will do only swapping below diagonal"  
# ] 


# for i in range(len(list1)): 
#     for j in range(len(list1[i])): 
#         if i > j: 
#             list1[i][j],list1[j][i] = list1[j][i],list1[i][j]

# for i in range(len(list1)): 
#     for j in range(len(list1[i])): 
#         print(list1[i][j], end=' ') 
#     print()  

# o/p    
# 1 4 7 4 
# 2 5 8 4 
# 3 6 9 4 

#------BOUNDARIES i want to print ------------

list1 = [         # diagonal matrix [i=j] 
    [1,2,3,4],    # below diagonal [i>j] 
    [4,5,6,4],    # above diagonal [i<j] 
    [7,8,9,4]     # "i will do only swapping below diagonal"  
] 

for i in range(len(list1)): 
    for j in range(len(list1[i])): 
        if i == 0 or j == 0 or i == len(list1)-1 or j == (len(list1[i])-1): 
            print(list1[i][j], end=' ') 
        else: 
            #print('$', end=' ')  
            print(' ', end=' ')  
    print()        

