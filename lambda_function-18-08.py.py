#------------LAMBDA FUNCTION -----------------

#Anonymous one line functions in python are called lambda functions 
#only has one expression in their function body 
#return is not explicit # no need to write return automatically returns 

# def add(a,b):
#     return a+b 

# print(add(2,3)) 

# example_function = lambda a,b : a+b
# print(example_function(4,5))  
# example_function = 50 # here reassigned the value  
# #print(example_function(4,5)) # wont work this now becoz reassigned example_function ok 

# lam2 = lambda a : a ** 2 
# print(lam2(22))  #(484 )

# lam3 = lambda : 'Good Morning'  # here i wrote without parameters  
# print(lam3())  #good morning

#------------------- WHY LAMBDA FUNCTIONS -----------------------

#Generaaly they are used in higher order functions  
# MAP, FILTER , REDUCE  

#--------------- MAP ----------------- 

# MAP(FUNCTION,ITERABLE)  --> SYNTAX 


def square(x):
    return x ** 2

map(square , [1,2,3,4,5,6])
print(map(square, [1,2,3,4,5,6])) 
 
print(list(map(square,[1,2,3,4,5,6])))  #1-2, 2-4, 3-9, 4,16,5-25, 6-36  # 1 becomes 2, 2 becom4 . 


# 

def check_even(x): 
    return x % 2 == 0

print(list(map(check_even,[1,2,3,4,5,6])))   #F,T,F,T,F,T  


#-----------WHY LAMBDA FUNCTION USES --> (to remove "DEPENDENCY" functions) 

def square(x):  
    return x % 2 == 0  # we cannot change this value ok 2 to 3 becoz someone using this value (dependency) is there 
           #someone is using this function right  - "so we cannot change the square we need to write own function"
def cube(x):  #NORMAL FUNCTION will have dependency // LAMBDA function will not have dependency (removes depenedncy)
    return x ** 3 ==0  # in this we cannot change the values 2 is there 'i need to change for 3' we cannot change some one using this  

print(list(map(square,[1,2,3,4,5,6])))  #insted of square i need to change "cube" it wont work 

print(list(map(cube,[1,5,33,44,55,66])))   

# 
# -------------To remove dependency we use lambda functions-----------------------
#   
print(list(map(lambda x: x ** 2, [1,2,3,4,5,6]))) #x **2 = x(square) #1-2, 2-4, 3-9, 4,16,5-25, 6-36 

print(list(map(lambda x: x ** 3, [1,5,33,44,55,66]))) #here we can change the values ("x ** 2 -- x **3 ") # dependency will removed  

#industry example (company) 

#you need to write your own code 
# no need to change other person code and no need to create for other person code no need to do changes  so write your own code  
def square(x): 
    return x ** 2

def cube(x): 
    return x ** 3 

#----------your code--------------- 
#   
print(list(map(square,[1,2,3,4,5,6]))) 

#--------another personcode ---------
print(list(map(cube,[1,5,33,44,55,66]))) 

print(list(map(lambda x: (x % 7 == 0 or x % 8 == 0),[1,5,33,44,55,66]))) #if x % 7 and 8 will becomes ==0 returns "true" 

#----FILTER------ (higher order functions -inbuilt functions) 

# in this we need to write the 'conditon' as "TRUE OR FALSE" 
# it will give you only CONDTION STATISFY VALUES IN "O/P" TRUE ELEMNETS  

#filter(map,iterable) ---> syntax

print(tuple(filter(lambda x: x % 2 == 0 , [1,2,44,66,76,33]))) # in this we get 2 44 66 76  # convert to tuple doing 

print(tuple(filter(lambda x: True, [1,2,44,66,76,33]))) # here we give 'TRUE' means it "gives all values"

# we will get different IDS when we using (higher order functions)
list1 = [1,2,4,55,7,88]  # here we the previous list will not change (here we assigned a variable as list1)

print(id(list1)) #this "ID" list is different 

print(id(list(filter(lambda x: True, list1)))) # THIS "ID" is different ok "previouse list doesnt change it is creating a new list"


#----------"REDUCE"------------ (higher order function) 

# reduce(function,iterable) ---->syntax 

# It gives in single o/p --compress all values and gives in a single o/p ---> ok higher value return in single value  

from functools import reduce  
print(reduce(lambda a,b : a+b, [1,2,3,4,5,6])) #1+2+3+4+5=6===> 21 

print(reduce(lambda a,b : a-b, [1,2,3,4,5,6])) #1-2-3-4-5-6==> -19  

#using TERMINATORY FUNCATION---"REDUCE"---higher order function --------------- 

print(reduce(lambda a,b: b if b > a else a, [1,2,3,4,6,-11]))  #6 --> is the answer  

print(reduce(lambda a,b: b if b < a else a, [1,2,3,4,6,-11]))  #11  --->is the  answer
