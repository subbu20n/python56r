#---------------------------Iterators-------------------------

#Iterable: string,tuple is an iterable but its iterate from first to last 
# list1 = [1,2,3,4,5] 
# for i in list1: 
#     print(i)

# 1
# 2
# 3
# 4
# 5


# ITERATORS : means what they want that only it takes ok 

# 1 
# using 1 in the part of the code  it finnish the operation and then calls seond one 

# 2  

# ----------'iter'------   and ------'next' ------------------ (functions)
 
# list1 = [1,2,3,4,5,6] 
# iter1 = iter(list1)  #here it convetrs list1 to 'iter'

# print(next(iter1)) #1  # here no need to mention index , when we call then it automatically comes 
# print(next(iter1)) #2
# print(next(iter1)) #3
# print(next(iter1)) #4
# print(next(iter1)) #5
# print(next(iter1)) #6  # when we mention to print more than in list elements it displays 'error' 

# print(next(iter1)) # error: StopIteration

# string 

# str1 = 'good morning' 
# iter1 = iter(str1) 

# print(next(iter1))# g 
# print(next(iter1))# o


#----------------------custom Iterators ----------------------- your own iterators  can write  

# class EvenIterator():
#     pass 
    
#     def __next__(self): 
#         pass 
# el = EvenIterator() 
# next(e1) 

# e1 + e2  #__add__  #we need to use dunder method because inbuilt functions in our objects has to work means we need to use dunder methods 


# class EvenIterator():
#     def __init__(self): 
#         self.curr_value=0 

#     def __iter__(self): 
#         return self 

#     def __next__(self): 
#         temp = self.curr_value #0 
#         self.curr_value += 2 
#         return temp  #0  #2 
# e1 = EvenIterator() 
# print(next(e1))  # 0  # it stops(pause) here iterator again when we call then only it starts  
# print(next(e1))  #2  


# class EvenIterator(): 
#     def __init__(self,limit): 
#         self.curr_value = 0 
#         self.limit = limit 
#     def __next__(self): 
#         return self 
#     def __next__(self): 
#         if self.curr_value > self.limit:  
#             raise StopIteration 
#         temp = self.curr_value 
#         self.curr_value += 2 
#         return temp 
# e1 = EvenIterator(10) 
# print(next(e1))     #0 
# print(next(e1))     #2
# print(next(e1))     #4
# print(next(e1))     #6 
# print(next(e1))     #8 
# print(next(e1))     #10
# print(next(e1))     # error: Stop Iteration  


#RANGE ITERARATOR 

#start_value #5 
# end_value #12  

#next() #5,6,7  

# class RangeIterator():
#     def __init__(self,start_value,end_value): 
#         self.curr_value = start_value  
#         #self.end_value = end_value 
#         self.limit =  end_value 
#     def __iter__(self): 
#         return self  
#     def __next__(self): 
#         if self.curr_value > self.limit: 
#             raise StopIteration
#         temp = self.curr_value 
#         self.curr_value += 1 
#         return temp 
# r1 = RangeIterator(5,12)

# print(next(r1)) #5 
# print(next(r1)) #6 

# -------ITERATORS: Iter, Next ---methods 
# 1 . list example 
# 2 . stop exception 
# 3 . custom exception  
# 4 . range like iterator 
# 5 . even number iterartor  
# 6 . reverse iterator  
# 7 . square iterator  
# 8 . infinite iterator   

# --------------------------------GENERATORS --------------------

# GENERATOR IS EASIER FORM TO PRODUCE ITERATORS(it is similar to functions only) 
# in functions (return(will give at a time o/p and stop the function) when we use 'yield' it pause the it returns only 1 value  )

# def gen(): 
#    yield 1 
#    yield 2 
#    yield 3 

# # def func1(): 
# #     print(1)
# #     print(2)
# #     print(3) 

# # print(func1())      
# # print(func1())       
# # print(func1())        

# # var1 = gen() 
# # print(next(var1)) #1
# # print(next(var1))  #2  


# def gen2(): 
#     num1 = 0 
#     while True: # it runs continuous infiinity 
#         temp = num1 
#         num1 += 2 
#         yield temp 

# var3 = gen2() 
# print(next(var3)) #0 
# print(next(var3)) # 2 

# def gen(limit): 
#     num1 = 0 
#     while num1 < limit: 
#         temp = num1 
#         num1 += 2 
#         yield temp 
# var3 = gen(10) 
# print(next(var3))   #0      
# print(next(var3))   # 2
# print(next(var3))   # 4
# print(next(var3))   # 6 
# print(next(var3))   # 8 
# print(next(var3))   # stop Iteration 

# -------fibonacci--------------- infinite ga ravali 

# def fib(): 
#     num1 , num2 = 0,1 
#     while True: 
#         # temp = num1 + num2 
#         # num1 = num2
#         # num2 = temp  
         
#         yield num1   # i need from '0' so i have give before udating the 
#         num1 , num2 = num2, num1 + num2 

# var1 = fib() 
# print(next(var1))  # 0   
# print(next(var1))  # 1 
# print(next(var1))  # 2
# print(next(var1))  # 3 


# #----- when we give 'return and yield '--------- 

# def gen(): 
#     yield 1 
#     yield 2 
#     return 3  
#     yield 4 

# var1 = gen() 
# print(next(var1)) 
# print(next(var1)) 
# print(next(var1))  #StopIteration: 3  what u have mentioned nesides return the value also return ins top iteration  

# ------------
# list1 = [1,2,3,4,5] 
# iter1 = iter(list1) 
# for i in iter1:  # we can like ths also this is same for iterable right 
#     print(i)

# 1
# 2
# 3
# 4
# 5

# ----------------Generators also we write shortcuts (comprehenesions) --- 

list1 = [num1 for num1 in range(1,10)] 
print(list1)  #[1, 2, 3, 4, 5, 6, 7, 8, 9] 

list1 = [num1*2 for num1 in range(1,10)] 
print(list1)  #[2, 4, 6, 8, 10, 12, 14, 16, 18]

gen1 = (num1 for num1 in range(1,10)) 
print(next(gen1))  # 1
print(next(gen1))  # 2 