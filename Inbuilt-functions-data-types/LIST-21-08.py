#----------DATA-TYPES -------INBUILT-FUNCTIONS----------------- 

#---------"LIST"-----(heterogeneous)----inside list float,complex anything is possible

# 1.Adding ---->APPEND,EXTEND,INSERT  
# 2.Removing--->remove(x),pop(i),clear() 
# 3.search-----> index(x, start,end) count()
# 4.reverse----> reverse() 
# 5.sort-------> sort(key=none, reverse=false) 
# 6.copy:- 
#       (a). SHALLOW COPY --->copies the outer conatiner but reference to inner conatiner  
#       (b). DEEP COPY --->copies both outer and inner connections  


  
# list1 = [1,2,4,4.3,[1,3,6]] 
# print(list1[4])
# print(list1[4][2])
# print(list1[4][-2]) 
# print(list1[7 : 4 : -1]) #slicing lo extra indexing iste empty string vstundi 


# print(list1 + [1,2,3])  #-cancatinate = 'adding to list 1 '#[1,2,4,4.3,[1,3,6],1,2,3]
# print(list1)
# list1 = list1 + [1] #--reassigning --> [1, 2, 4, 4.3, [1, 3, 6], 1] --> Added '1' to list1 reassigned 
# print(list1) # [1, 2, 4, 4.3, [1, 3, 6], 1] --> ad


#--------------------APPEND-------------------------

#list1.append()---> takes only "one argument" 
# adding elements/arguments  will add in "last"

# list1 = [1,3,4,5] 
# list1.append(6) 
# print(list1)  #[1, 3, 4, 5, 6]

# list1.append([1,2,3])
# print(list1)  #[1, 3, 4, 5, 6, [1, 2, 3]] 

# #list1.append(1,5) 
# print(list1)   #    list1.append(1,5) TypeError: list.append() takes exactly one argument (2 given)


#-----------------EXTEND----------------------

#in this we can add "multiple arguments" 
# WHEN we give 'tuple' type it wont work -must give list type 

# list1 = [1,2,3,4,5] 
# list1.extend([8,9]) 
# print(list1) #[1, 2, 3, 4, 5, 8, 9]  


# list1.extend([[2,7,4],22]) #--- it will add like list 
# print(list1)   #[1, 2, 3, 4, 5, 8, 9, [2, 7, 4], 22] 

# list1 = [1,2,3,4] 
# list1.extend((1,2,3,4))
# print(list1)  #[1, 2, 3, 4, 1, 2, 3, 4] 



#-----------------Insert------------------------- 

# INSERT --takes "2-elements/arguments"  (insert index, ele)

#if we give index ledu -meeru icchina index ledu then "it will treat as append" -error 

# list1 = [1,3,5,6,7,8] 
# list1.insert(3,0) #3rd indexing '6' will replace to - '0'  
# print(list1)  #[1, 3, 5, 0, 6, 7, 8]   


# #list1.append(8,6) #8 indexing not there so it will treat as 'append' ' 

# print(list1)  #TypeError: list.append() takes exactly one argument (2 given)

# list1 = [3,6.7,8,9] 
# list1.insert(-4,9) # [9, 3, 6.7, 8, 9]  #3 replaced to '9' 
# print(list1) #[9, 3, 6.7, 8, 9]  

# list1 = [3,6.7,8,9] 
# list1.insert(-4,9,[1,3]) # TypeError: insert expected 2 arguments, got 3
# print(list1)


#--------------------REMOVE------------------------------------- 
#clear - everything will remove 

# list1 = [1,2,3,4] 
# list1.clear()  #evrthing will remove 
# print(list1) #[]


#-----------------------POP-------------------------------------- 

# 'pop will return a value '
#it will remove specific index  
# if you wont give index number "it will remove last number" 

# list1 = [1,2,3,4] 
# # list1.pop(2) #it will remove '3' 
# # print(list1) #[1, 2, 4]

# res = list1.pop(2) # in r'res' stores the values #3 
# print(res) #3 total 3 values are there so printed '3' 
# print(list1) # [1,2,4] 

# list1 = [1,2,3,4,5,6]
# res = list1.pop(7) 
# print(res) 
# print(list1) #IndexError: pop index out of range 


# list1 = [1,2,3,4,5,6]
# res = list1.pop() # index not given it will remove 'last digit' 
# print(res) #6 
# print(list1) #[1, 2, 3, 4, 5]
 

# list1 = [1,2,5.5,7,9,5.5,5.5] 
# list1.remove(5.5)    # it removes 'first '5.5'
# print(list1)           # [1, 2, 3, 4, 7, 9, 5.5,5,5]
 

# list1 = [1,2,5.5,7,9,5.5,5.5] 
# list1.remove(5.55)    # it removes 'first '5.5'
# print(list1)     #valueerror: 5.55 is not in list1 


#  5.5 ni at a time we can do for loop  we can remove 5.5 -at a time  

# list1 = [1,2,5.5,7,9,5.5,5.5] 
# print(list1.count(5.5)) # 3 times happens for loop 

# for i in range(3): 
#     list1.remove(5.5) 
# print(list1.index(7))    # 7 index will become '2'  

#-----------------------------INDEX------------------------ 

# list1 = [2,4,5.5,84,61,5.5,5.5,61] #here 7 index lo undi '61'
# print(list1.count(5.5)) #3 

# print(list1.index(61, 5,8)) #(7)# here '61' index 5 to index 7 lo unte --> display chestundi which "index number" anesi 



# #------------------------REVERSE--------------------------- 

# list1 = [1,2,3,4] 
# list1.reverse() 
# print(list1) #[4, 3, 2, 1] 

# -------------------SORT--------------------------------

# sort = (key=None , reverse=false) 
# if u have "descending order" it will keep 'ascending order'  
# it arrange the values 'first negative -next positive numbers' 'it keep in order'

# list1 = [1,2,-31,45,32,-33,-93] 
# list1.sort() 
# print(list1)  #[-93, -33, -31, 1, 2, 32, 45] 


# list1 = [1,2,-31,45,32,-33,-93] 
# list1.sort(reverse=True) #[45, 32, 2, 1, -31, -33, -93]
# print(list1) #reverse = true pedite first positive pedutundi next it keeps negative numbers  

# list1 = ['apple','dog','egg','ball'] 
# list1.sort() 
# print(list1)  #['apple', 'ball', 'dog', 'egg']  --it arrange 'A-Z' order 

# list1 = [[1,2,3],[5,6,1],[4,8,0]] 
# list1.sort(key = lambda l1: l1[0], reverse=True)  # '0' index goes to last 
# print(list1)  # [[5,6, 1], [4, 8, 0], [1, 2, 3]] 

# list1 = [[1,8,7],[1,6,1],[4,8,0]] 
# list1.sort(key = lambda l1: (l1[0], l1[1]))  # #if in index0 and 1 -have same indexes it search in "1-th placw"
# print(list1)  # [[1, 6, 1], [1, 8, 7], [4, 8, 0]] #first order wise will set small numbers to big numbers  


#------------------------------COPY----------------------------- 

#-------------------SHALLOW COPY----------- 
#newly created copy has link to prvious copy   
# # if you do changes in one copy it reflects both will aply the changes 

# list1 = [1,2,3,4,5] 
# list2 = list1  

# list1[0] = 10  #reassignment to list1 as index - 0 as 10 replacing -it reflect to list2 also 
# print(list1) #[10, 2, 3, 4, 5]
# print(list2) # [10, 2, 3, 4, 5]

# list1 = [1,2,3,4,8] 
# list2 = list1 

# list1[0] = 10 
# list1.append(5) # 5 -added to both 
# print(list1) #[10, 2, 3, 4, 8, 5] #
# print(list2) #[10, 2, 3, 4, 8, 5]


# list1 = [1,2,4.5,7,6] 
# list3 = list1.copy() 
# print(list3)  #[1, 2, 4.5, 7, 6] ---see same values to "list3" --ok 

# list1 = [3,5,6,[9,4,0]] #3 rd elemnet '9' replaced to '8'
# list1[3][0] = 8
# print(list1) #[3, 5, 6, [8, 4, 0]] 


# list1 = [3,5,6,[9,4,0]] #inside list are 'mutable elements' it can "share both same values" - 'immutable elements'outer list "cant share same values" ok 
# list1[3][0] = 8
# list1[2] = 2 #it changed in only "second list" - "copid list comes changes"it wont rreflect to both lists 
# print(list1) #[3, 5, 6, [8, 4, 0]]
# print(list1) #[3, 5, 2, [8, 4, 0]]  ---> in this reflects list[2] = 2 ok 

#--------------------------------DEEP COPY------------------------- 
#copies both outer and inner lists  

list1 = [1,2,3,[2,5,6],4,5] 
list2 = list1 
list1[3][2] = 8 
list1[2] = 9 

import copy 
list2 =copy.deepcopy(list1) 

print(list2)
print(list1) 



