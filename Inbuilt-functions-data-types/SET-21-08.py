#-----------------------SET-------------------INBUILT-FUNCTIONS-------------- (indexing kudaradu) 

# SET: selection of -unordered,infinite,unique -elemnets 

#-----------------ADD-------------------

# s = {1,2} 
# s.add(3) 
# print(s)  #{1, 2, 3}

#-------------remove-----------

# s = {1,2,3} 
# s.remove(3) 
# print(s) #{1,2} 

# #------------discard------------------. is also "remove" only same  

# s = {1,2,3} 
# s.discard(2) 
# print(s) #{1,3} 


#---------pop-----------

#randomly any one selects element and removes it  

# s = {1,2,3}  
# print(s.pop()) #1 
# print(s) #{1,3} 


#---------------clear--------------------

# s = {1,2,3,} 
# s.clear() 
# print(s) #sect() 

# #-----------------union---------------------

# #common ga undevi "it writes one time" in both 

# s1 = {1,2} 
# s2 = {1,3}  
# print(s1.union(s2)) #{1, 2, 3} -1 is common so writes only '1time'

#------------------INTERSECTION---------------------

# Intersection --- same values willbe is there means those will  printed  

# s1 = {1,2,3} 
# s2 = {4,2,6} 
# print(s1.intersection(s2))  #{2} 

# --------------difference----------------------
#difference values is there means those will print  

# s1 = {1,2,3} 
# s2 = {2,4,3} 
# print(s1.difference(s2)) #{1},{2} are different values printed --(s1 -diff values comapredto s2) 
# print(s2.difference(s1)) #{4}  (s2 values compared to s1) 

#----------------SYMMETRIC DIFFERENCE---------------------------

#Common elements will ignores remaining will print  

# s1 = {1,2,4} 
# s2 = {1,2,5} 
# print(s1.symmetric_difference(s2)) #{}4,5}  common values ignored 

# #----------------------isDISJOINT----------------------

# # in "2 sets" did not have common elements then it prints "TRUE" 

# s1 = {1,3,4} 
# s2 = {6,5,7}
# print(s1.isdisjoint(s2))  #no common elements so "TRUE" 


#------------------isSUBSET--------------------------- 

#IF 'A-SET' HAVE all elements in 'B-SET' then it is subset 

# s1 = {1,2,3} 
# s2 = [1,4,3] 
# print(s1.issubset(s2)) #false  

# s1 = {1,2,3} 
# s2 = [1,2,3] 
# print(s1.issubset(s2)) #TRUE 

#-------------------------isSUPERSET-------------------------

# in "both sets " have same values "then it become both superset and subsets"

s1 = {1,2,3} 
s2 = {1,2} 
print(s1.issuperset(s2)) #TRUE  



s1 = {1,2,3} 
s2 = {1,4} 
print(s1.issuperset(s2))