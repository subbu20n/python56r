#-----------------------MATRIX-----------NESTEDLIST also called as matrix---------------ps--

# l = [
#     [11,22,33], #-->rows 
#     [44,55,66],
#     [77,88,99]
# ]

# print(l[2][1]) #88
# print(l[1][2]) #66 

# for i in range(len(l)): 
#     for j in range(len(l)): 
#         print(0, end=' ') 
#     print(l)    

# # 0 0 0 
# # 0 0 0  
# # 0 0 0 

# # problem --- "rows ni sum chesta" ---------

# # o/p -- 66, 165, 264 
# l = [
#     [11,22,33], #--66 
#     [44,55,66], #-- 165 
#     [77,88,99]  #-- 264 
# ]

# for i in range(len(l)): 
#     sum = 0 
#     for j in range(len(l)): 
#         sum += l[i][j] 
#     print(sum, end=" ")    #66 165 264  

#-----------------DIAGONAL ELEMENTS---------------------

# l = [
#     [11,22,33], #-->rows   o/p --> [0,22,33],  (i=j)  o/p ila ravaali 
#     [44,55,66],                   #[44,0,66], 
#     [77,88,99]                    #[77,88,0]   
# ]

# for i in range(len(l)): 
#     for j in range(len(l)): 
#         if j == i: 
#             l[i][j] = 0 #11,11=0 
# print(l)        

#[[0, 22, 33],(0,0)
# [44, 0, 66], (1,1)
# [77, 88, 0]] (2,2)

#---------Right Diagonal --------------(i+j=n-1)----------------

l = [
    [11,22,33], #-->rows   o/p --> [11,22,0],  (i+j=n-1)  o/p ila ravaali 
    [44,55,66],                   #[44,0,66], 
    [77,88,99]                    #[0,88,99]   
]
 
for i in range(len(l)): 
    for j in range(len(l)): 
        if i + j == len(l) - 1: 
            l[i][j] = 0 #11,11=0 
print(l)        



