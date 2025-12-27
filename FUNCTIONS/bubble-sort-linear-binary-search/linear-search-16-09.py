#------------------------------LINEAR SEARCH-------------------------------

#linear search : works in any list 
#binary search : works only in sorted list only  

# *****in linear search we have 100 input --> then it iterates 100 times only****" 
# 0(n) ---> time complexity (worst case it terates if we give 30 as input it itertes 30 times ) 

list1 = [-3,-300,10,23,45,100,700]  

#search_elem = -3 
# flag = True 
# for i in range(len(list1)-1): #==> (0, len(list1) -1) it takes automatcally from '0' to len(list1)-1' 
#     if list1[i] == search_elem: 
#         print(i)   # we have found "atleast 1 element in list it breaks here itself"
#         flag = False 
#         break 
#     if flag == True: 
#         print('Not found') 

#0(n) --> time complexity "worst cases it iterates if u want in list 100 but 100 is in last in list but it iterates 100 times"

#same code  i will write in 'method' 

def linear_search(list1, search_elem): 
    for i in range(len(list1)-1): #0 to starts 
        if list1[i] > list1[i+1]: 
            return i  
    return False # we did not find atleast one element also it comes here  

res = linear_search(list1, 700)
print(res) 