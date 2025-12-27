#---------------------------LIST REVERSE-----PS--------------------------- 

# list1 = [10,20,30,-32,67] 

# #method-1 

# list1.reverse() 
# print(list1)   #[67, -32, 30, 20, 10]  

# #----method-2 ----

# #print(list1[ : : -1]) #when slicing we need to reassign to change the value  ok 

# list1 = list1[ : : -1]   #reassignment [67, -32, 30, 20, 10]  then it get o/p ok 
# print(list1)   
 

#------------------method-3------------ it iterates from starting to reverse----

# list1 = [10,20,30,-32,67]  

# new_list = [] 
# for i in list1:  
#     new_list.insert(0, i) #insert will add all values in last  
# print(list1)  #[10,20,30,-32,67]    --> we need to reassign values 

# list1 = new_list #reassignment  
# print(list1)  #[67, -32, 30, 20, 10]


#-----method-4---------"using range we get element value" ------------- 

# list1 = [10,20,30,-32,67]   

# for i in range(0, len(list1)): #5-1=4 
#     print(i) 
#     print(list1[i]) 
# print(len(list1))#5 

# 0
# 10
# 1
# 20
# 2
# 30
# 3
# -32
# 4
# 67  

# for i in range(len(list1) -1, -1, -1): #negative indexing format  
#     print(i) 
#     print([list1[i]]) 

# print(range(0,5)) # it works []
# #print(range(5,0)) #this wont work because in slicing it moves from "left to right" 

# 4
# [67]
# 3
# [-32]
# 2
# [30]
# 1
# [20]
# 0
# [10]


#---------------EFFICIENT APPROACH------------REVERSE LIST-------------(swapping)------ 

#in placed reverse "low+1 , high-1"  

# list1 = [10,20,50,-32,67] 

# low = 0 
# high = len(list1) -1  #5-1 = 4 

# while low < high: 
#     list1[low] , list1[high] = list1[high] , list1[low]
    
#     low += 1 #10 
#     high -= 1 
# print(list1)  #[67, -32, 30, 20, 10] 

#-------------I need half in the list -------------------------------
list1 = [10,20,50,-32,67] 

low = 0 
high = (len(list1) -1) // 2  #4/2 = 2 #in index-- 0,1,2 ---> mid value= 50 

while low < high: 
    list1[low] , list1[high] = list1[high] , list1[low] 
        
    low += 1 
    high -= 1   

print(list1)      # [50, 20, 10, -32, 67]  




