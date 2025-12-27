#---------------------------Bubble Sort------------------------------

# we will keep sorting rule in that rule base  
# value -- increasing order in sort gets it calls  --ascending order sorting
# value -- decreasing order in sort gets it calls  --descending order sorting  

# in list maximum element gets in last last  

# list1 = [10,-3,700,45,23,100,-300] #max element gets last '700' max element gets 'last'  

# #[-3,10,45,23,100,-300,700] 

# for i in range(0, len(list1) -1): 
#     if list1[i] > list1[i+1]: 
#         list1[i] , list1[i+1]  = list1[i+1] , list1[i] 

# print(list1)  #[-3, 10, 45, 23, 100, -300, 700] 

# #"bubble sort --> we need to do 'subpart' to move it gets maximum value to get last" it iterates to get correct format  

# for i in range(0, len(list1) -1): 
#     if list1[i] > list1[i+1]: 
#         list1[i] , list1[i+1]  = list1[i+1] , list1[i] 

# print(list1)

# for i in range(0, len(list1) -1): 
#     if list1[i] > list1[i+1]: 
#         list1[i] , list1[i+1]  = list1[i+1] , list1[i] 

# print(list1)

# for i in range(0, len(list1) -1): 
#     if list1[i] > list1[i+1]: 
#         list1[i] , list1[i+1]  = list1[i+1] , list1[i] 

# print(list1)

# for i in range(0, len(list1) -1): 
#     if list1[i] > list1[i+1]: 
#         list1[i] , list1[i+1]  = list1[i+1] , list1[i] 

# print(list1)

# for i in range(0, len(list1) -1): 
#     if list1[i] > list1[i+1]: 
#         list1[i] , list1[i+1]  = list1[i+1] , list1[i] 

# print(list1)

# [-3, 10, 45, 23, 100, -300, 700]
# [-3, 10, 23, 45, -300, 100, 700]
# [-3, 10, 23, -300, 45, 100, 700]
# [-3, 10, -300, 23, 45, 100, 700]
# [-3, -300, 10, 23, 45, 100, 700]
# [-300, -3, 10, 23, 45, 100, 700]

# list1 = [10,-3,700,45,23,100,-300]

# for  j in range(0,6): # outer loop iteration '6 times'
#    for i in range(0, len(list1)-1): #inner loop iterates -for every outerloops 1 iteration = innerloop 6 iteration   
#        if list1[i] > list1[i+1]: 
#             list1[i] , list1[i+1] = list1[i+1] , list1[i]  

# print(list1)   #[-300, -3, 10, 23, 45, 100, 700]  only (36 iterations)  here 6*6=36  

#----------------------------



# list1 = [10,-3,700,45,23,100,-300] 

# 1st iteration j = 0 => 0 members ignored #max elemnt 700 
# 2nd iteration j = 1 => 1 memebrs ignored  #100 
# 3rd iteration j = 2 => 2 members ignored # 45 

# for j in range(0, len(list1) -1): 
#     for i in range(0, len(list1) -1 -j): # for 'j' is iterations ignores the 'for 1st iteration 0 ignored and 2 nd iteration 1 ignored like that  
#        if list1[i] > list1[i+1]: 
#            list1[i] , list1[i+1]  = list1[i+1] , list1[i] 

# print(list1)    #[-300, -3, 10, 23, 45, 100, 700]  only (36 iterations)  here 6*6=36 
 
#-----------------------------

#--------------In some case almost sorted only few numbers has to sort ------------

list1 = [-3,-300,10,23,45,100,700] # here almost sorted only sort has to happend then write algorithm 

for j in range(0, len(list1)-1): 
    flag = False  
    for i in range(0, len(list1)-1): 
        if list1[i] > list1[i+1]: 
            flag = True   # here atleast ont time iterate sort happens also then it becomes "TRUE"
            list1[i] , list1[i+1] = list1[i+1] , list1[i] 
    if flag == False:  # here atleast one time also did not have happened sorted  
        break 
print(list1)        
