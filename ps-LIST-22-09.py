#------------probliem soliving---------------dictionary format -----------frequency-----------


#--without using a extra solving with a dictionary format --------
# list1 = [10,2,5,10,5,77,2,10] 

# dict1 = {}

# for i in list1: 
#     if i not in dict1: 
#         dict1[i] = 1 # if first time iterating add to dict as i = 1 
#     else: 
#         dict1[i] += 1  # then u get same value in that i = 2 nd time repeating add i += 1 = 1+1 = 2 times, i += 1 = 2+1 = 3 
#         #dict[i] = dict[i] + 1 
# # if '2nd time repeats it add increments' -- if '1st time it add only key value pirs'
# print(dict1)  #{10: 3, 2: 2, 5: 2, 77: 1}

#--same code -----in method type------

# dict2 = {} 

# for i in list1: 
#     dict2[i] = dict2.get(i,0) + 1 
#                          #(10,0) + 1 = 0+1 =1 for 10- as 1st time  (ok) 
# print(dict2)    #{10: 3, 2: 2, 5: 2, 77: 1}

#----------u will get unique elements---------- 

# dict1 = {10: 3, 2: 2, 5: 2, 77: 1}
# for key, value in dict1.items(): 
#     if value == 1: 
        
#      print(key)

# #--FInd missing number in lists ----- 

# # num1 = [3,4,1,7,5] 
# list1 = [1,7,5,4,3] 

# list_min = min(list1) 
# list_max = max(list1) 

# for i in range(list_min,list_max): 
#    if i not in list1: 
#       print(i) #2,6 are missing 

#-------FIND SUM  of all elements in list 'inner list element sum'------

# list1 = [[1,2,5],[-3,4,5,6],[42,33]] #cummulative sum (1+2+5)=8+(-3+4+5+6)=20+(42+33) =95
# sum = 0 

# for i in list1: 

#    for j in i : 
#       sum += j 
# print(sum)  #95 

#-----------------same code but it gets inner list sum ----------------

# list1 = [[1,2,5],[-3,4,5,6],[42,33]] 
# sum = 0 
# for i in list1: 
#    for j in i: 
#       sum += j 
#    print(sum)  # for every list it get sum 8 + 20+ +95 

#---------------

#Q. Given  array of N integer , the task is to replace each element of the array by  its rank in the array 
#INPUT: 20 15 26 2 98 6      OUTPUT: 4 3 5 1 6 2  

#Explanation: when the array is sorter 2 rank is 1, 6 rank is 2 , 15 rank is 3 

# when we do sorted list it becomes [2,6,15,20,26,98] 

list1 = [20,15,26,2,98,6] 

#list2 = list1 # list 1 memory block will loose so for "list1 also assigns new value" 
#list2.sort() # so its not possible  

# ---method-1----------

# import copy 
# list2 = copy.deepcopy(list1)

# print(list1) # it creates same as 'list1' 

# #----method-2---------using inbuilt method  

# list2 = sorted(list1) 

# print(list2) #[2, 6, 15, 20, 26, 98] 

#------method-3------------- we did not change list and get new list  

# list2 = []
# for i in list1: 
#     list2.append(i) 

# print(list2)    #[20,15,26,2,98,6]  

#-----------method-2-------------- 

list1 = [20,15,26,2,98,6]  
list2 = sorted(list1)  

list2 = [20,15,26,2,98,6]  

rank_list = [] 

# for i in list1: 
#     for j in range(len(list2)): 
#         if i == list2[j]: 
#             rank_list.append(j+1) 
#             break 

# print(rank_list)   #[4, 3, 5, 1, 6, 2] 

for i in list1: 
    rank_list.append(list2.index(i)+1) 
print(rank_list)    
