#--------------problem solving-----------LIST---------------------

# 1. wap to print duplicates and unique numbers in an array list 

# list1 = [1,2,3,4,3,2,5,6,7,8] 

# #unique elements = 1,4,5,6,7,8 
# # duplicate elements: 2,3 
# u = [] 
# d = [] 

# for i in list1: 

#    if list1.count(i) > 1 and i not in d: 
#       d.append(i)   #duplicate elements will not have in duplicate elements then add to [d] 

#    elif  list1.count(i) == 1: 
#       u.append(i) # unique elements will not have in unique elements then add to [u] 

# print(u) #[1, 4, 5, 6, 7, 8]
# print(d) #[2,3] 

# #----------

# #------------subset findout in 2 lists-------------------

# # elements will have in '2lists' then count -or else no need to count leave that element in any list find extra element  
# # subset --> we have in same numbers in 2 lists then it call as subset  

# # arr1 = [1,3,4,5,2,0] 
# # arr2 = [2,4,3,1,75,15] # in this array-1 elements does not match so it would be the 'subset'

# arr1 = [1,2,3]  #in array1 elements has to see the same elements in array2 then it would be "subset" 
# arr2 = [3,2,1,5,6]

# c = 0 
# for i in arr1: 
#    if i in arr2: 
#       c += 1 
# if c == len(arr1):      
#    print('Subset') 
# else: 
#    print('Not a subset')   


#---calculate 'sum of 'digit' of each number in list --------------

list1 = [202,89,112,88] 

#202=2+0+2=4 , # 89=8+9=16, 112=1+1+2=4, 88=8+8=16 

list1 = [202, 89, 112, 88]

l1 = []
s = 0

for i in list1:
    s = 0              # reset here
    n = i              # temp variable
    while n > 0:
        r = n % 10
        s = s + r   #s += r == s+r 
        n = n // 10
    l1.append(s)

print(l1)
