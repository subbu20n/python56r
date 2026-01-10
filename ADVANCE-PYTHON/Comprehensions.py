#--------------------------------COMPRENHENSIONS---------------------

# prime number 

# num1 = int(input('enter a number')) 
# #9 
# flag = False 
# for i in range(2,num1): 
#     if num1 % i == 0 :  # here we found a one element also then it is  not a prime number  ok 
#         flag = True 
#         print('not a prime number') 
#         break 
# if flag == False:  # still flag == flase then it becomes a prime numer 
#     print('prime number')     


# --------------FOR-Else------------------
# for loop when code breaks in middel it goes to "else"
# for loop successfully iterates then it ont go to 'else-block' 

# for i in range(1,20): 
#     print(i) 
#     if i == 5:  # here for loop successfully iterated  it wont go to 'else'
#         break 
# else: 
#     ('else called')    

#---------------------WHILE-Else-----------------------  
# while loop when code breaks in middel it goes to "else"
# while loop successfully iterates then it ont go to 'else-block' 

# num1 = 1 
# while num1 < 20: 
#     print(num1) 
#     num1 += 1 

#     if num1 == 10: 
#         break
# else:        
#     ('Else block called')  


# IF for loop breaks ==> It will not go to else block 
# If loop does not breaks ==> then it will go to else block 

# for i in range(2,num1): 
#     if num1 % i == 0: 
#         print('not a prime number') 
#         break 
# else: 
#     print('prime') 

# # -------LINEAR SEARCH------ 

# list1 = [1,10,-3,5,-32,48] 
# search_elem = 54 
# for i  in list1:
#     if i == search_elem: 
#         print('Element found') 
# else: 
#     print('Not found') 

# ------Binary search --------

# low, high = 0,len(list1) -1 

# while low <= high: 
#     mid = (low+high) // 2  
#     if list1[mid] == search_elem: 
#         print(mid, 'Element found') 
#         break 
#     elif list1[mid] > search_elem: 
#         high = mid-1
#     else: 
#         low = mid+1 
# else: 
#     print('Not found')        

# ---------------------------------------COMPREHENSIONS---------------------------------
# comprehensions - are to create shortcuts 

# list1 = [] 
# for i in range(1,10): 
#     list1.append(i**2)  #1square,2square 1*1,2*2,-----
# print(list1)    #[1, 4, 9, 16, 25, 36, 49, 64, 81]

# #same code in shortcut 

# list2=[i**2 for i in range(1,10)]   # we will use in to plot a graphs 
# print(list2)    #[1, 4, 9, 16, 25, 36, 49, 64, 81]
                #[1, 4, 9, 16, 25, 36, 49, 64, 81]

# list2 = [3*x+2 for x in range(1,10)]   # 3*1=3+2=5 , 3*2=6+2=8 .....
# print(list2) #[5, 8, 11, 14, 17, 20, 23, 26, 29]

# list2 = [3*x+2 for x in range(1,10) if x%2 ==0]  # we can write condition also 
# print(list2) #[8, 14, 20, 26]


# [expression for Var in iterable condition] ---> syntax  
# exp,for with iterable condition 

# list3 = [ 4,5,-10,11,32,45,77] 
# list4 = [i for i in list3 if i < 35]  # condition check it  
# print(list4)  # [4, 5, -10, 11, 32]

# ----set --- 

# list3 = [ 4,5,-10,11,32,45,77] 
# list4 = {i for i in list3 if i <35} 
# print(list4)   #{32, 4, 5, 11, -10}  set is unordered

# -------dict--------------

# list3 = [ 4,5,-10,11,32,45,77] 
# list4 = {i:i**2  for i in list3 if i <35}   # first 'i'=indexes i**2='i' square 
# print(list4)  #{4: 16, 5: 25, -10: 100, 11: 121, 32: 1024}

#----------------IF-ELSE---------------------- 

# list3 = [ 4,5,-10,11,32,45,77] 
# list4 = ['EVEN'  for i in list3 if i %2 == 0 ]   # here comes only even 
# list5 = ['EVEN' if i % 2 == 0 else 'odd' for i in list3]  # here comes only odd 

# print(list4)   #['EVEN', 'EVEN', 'EVEN']
# print(list5)   #['EVEN', 'odd', 'EVEN', 'odd', 'EVEN', 'odd', 'odd']

#---
# list3 = [ 4,5,-10,11,32,45,77] 
# list5 = [3*i if i % 2 == 0 else 3*i - 2 for i in list3] 
# print(list5) #[12, 13, -30, 31, 96, 133, 229]

# generator method using shortcuts  
#-------------------------------------

# def gen(): 
#     num1 = 1 
#     while num1 < 10: 
#         yield num1 
#         num1 += 1 

# var1 = gen()  
# print(next(var1)) 
# print(next(var1)) 
# print(next(var1)) 
# print(next(var1)) 

# #shortcut geberator  
# var2 = (x for x in range(1,5))

# print(type(var2))  #<class 'generator'>
# print(next(var2)) #1
# print(next(var2)) #2
# print(next(var2)) #3
# print(next(var2)) #4
# print(next(var2)) #StopIteration  


# -------------------unpacking---------------- 

# a,b,c = [1,2,3] 
# print(a) #1
# print(b) #2
# print(c) #3 

# a,b,c = [1,2,3,4] # i age extra element here  

# print(a) 
# print(b) 
# print(c)

#ValueError: too many values to unpack (expected 3, got 4)

# ------------------EXTENDED Packing ---------------------


# a,*b,c = [1,2,3,4] # i age extra element here   (using arbitory)

# print(a) #1
# print(b) #[2, 3]
# print(c) # 4 

# str1 = input('enter all numbers in csv format') 
# #print(str1.split(','))  #['12', '3', '4', '6', '7'] 

# num1, num2 = list(map(int,str1.split(','))) 
# print(num1,num2)  #12 34


# --------------EMURATE---------------- 


# for i in list1: # here comes values 
#     print(i) 

# for i in range(len(list1)):  # here comes indexes 
#     print(i)    

list1 = [32,45,67] 
#for i,j in enumerate(list1):
for index,elem in enumerate(list1): 
    #print(i,j)
    print(index,elem)

