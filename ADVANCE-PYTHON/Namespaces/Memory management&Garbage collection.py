#---------Namespaces ---/Memory management and Garbage Collection ------------------ 

#-----------------------------Namespaces-------------------------------

# Namespace is more like a conatainer --> in this you are actually storing variables 
# num1 = 10 
# num2 = 10 

# num1 we will keep in 'namspaces' 
# num1 - value will not keep in namespaces 

# Name spaces are dictionaries  
#  {
#     num1:  10  
#     num2: also 10 refering to 10 only  'keys wont be the same right '  
#  } 

# Local , Global, Enclosed , and Builtin scopes discussed  already  

# num1 = 10 
# num2 = 20 

#Local, Global, Enclosed and Builtin 

# local scope will have different namespace  
# global scope will have differnet namespace 
# enclosed scops will have different namespace  
# builtin scope will have different namespace 

def example(): 
    num1 = 20 

# globals ==> {'num1': 10} 
# locals  ==> {'num1': 10} 
# enclosed ==> {'num1': 10}   # we can write like this because we have different namespaces  right 

# scope ==> Area in which you can acces a variable 
# namespace ==> are the actual containers with stores your varibale names and their corresponding names references 

#LEGB ---> PREFERENCES OF SCOPE 


num1 = 10 
num2 = 10 
#Local, Global, Enclosed and Builtin 
# LEBG --> preference order 

# def example (): 
#     num1 = 20 
#     print(globals())
#     print(locals())  # it has to search in local namespace 
#     print(num1) # {'num1': 20}local scope preference so it prints #20 (i will move to local namespace and num1 variable points to there i will get address) 

#     def example2(): 
#         print(num1) #20 
# example()         

# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x000002128CFC60F0>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'c:\\Users\\HP\\OneDrive\\Desktop\\56R_python\\ADVANCE-PYTHON\\Namespaces\\Memory management&Garbage collection.py', '__cached__': None, 'example': <function example at 0x000002128D263740>, 'num1': 10, 'num2': 10}
# {'num1': 20}
# 20

# -------------------MEMORY MANAGEMENT IN PYTHON ------------------ 

# 1. how programs store and use memory during execution prevent memory leaks, improves efficiency, helps in debugging 

#    1. stack memory : fast access directory managed by cpu , function calls, local variables refereneces, and their return addresses are stored here 
#    2 . Heap : what is a heap? 
#        a. All python objects and data structures here 
#        b. access is slower because of more complexity
#    3. object representation: Every python object in the heap contains a header with metadata including 
#       a. referenece count ==> sys.getrefcount(obj) 
#       b. TYpe 
#       c. Value 
#    4. Garbage collector: Automatically reclaims memory from objects that are no longer in use 
#         a. if an object reference count drops to zero , its memory is immediately deallocated 
#         b. circular references will be automatically deleted by GC 

# objects divided into 3 geberations
#-------------------------------------------
# 1. Gen 0: new objects 
# 2. Gen 1: long lived objects 
# 3. Gen 2: Long Living objects 

# GC checks younger generations more often (since most objects die young) 

# Best practices 
# 1. used del to delete unnecessary references 
# 2. prefer local variable (get cleaned faster) 
# 3. use generators/iterators instead of creating lists 
# 4. avoid large objects staying in global scope 

# in python execution time there is a two types of memory 
# stack memory and --> in this only functions calls will store remainng all in heap memory this is fast 
# heap memory ---> this is slow (actual data will have in heap only) inside heap will have 'namespaces' 

# in stack f1,f2,f3 are stored 

# f1 will local namespace reference  , f2 will have local namespace will have , f3 will have local namespace 


# stack - will have limited space (so thats why we did not kept namespaces here in stack) 
# Heap - will have more memory  

# object repesentation 

# refernce count will decide the how many variables are pointing  

# ----------------------------Grabage Collector-------------------------------

# memory - inside memory unwnated data will removes by garbage collector only   and free up the memory 

import sys 
list1 = [1,2,3] 

print(sys.getrefcount(list1)) #2 here this getrefcount() also one function it also counts so thats whys it gets2 

import sys 
list1 = [1,2,3] 
list2 = list1
print(sys.getrefcount(list1)) 


import sys 
list1 = 1 
l2 = list1 
print(sys.getrefcount(list1))


