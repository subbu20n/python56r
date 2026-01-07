#------------------------------ADVANCE PYTHON------------------------------------

# python advance concepts 

# 1. Generators and Iterators  
# 1a. Exception handling 
# 1b. File Handling 
# 1e. Memory management and Garbage collection (circular reference) 
# 1f. Python Namespaces (similar to scopes) 
# 1c. Multi Threading and MultiProcessing and AsyncIo 
# 1d. Serialisation (removed here introduced in requests) 
# 1g. Decorator 
# 1h. DateTime Module 
# 2. NUMPY, PANDAS, MATPLOTLIB, MATH Modules 
# 8. PDBC 
# 12. Logging 
# 13. Tkinter 
# 15. requests module 
# 16. REgex 

# __name__='__main__' 

# 17. Comprehensions 

#-----------------------------EXceptional Handling -------------------------

# you can call every exceptional as error 
# your error will not become an exception   

# when we start to run the code at that time comes run times  raises the 'exception' 
# before running the code comes an 'error' 

# a = int(input('enter num1')) 
# b = int(input('enter num2')) 

# print(5/0) # this is an exception   #ZeroDivisionError: division by zero

# -------TRY ,EXCEPT, ELSE,  Finally --------------

#TRY : if try block comes error then only move to except block and except will handles the error 
# except: will handle the error 
# ELSE: else and except are any one has to be placed either except or else  
#Else : else will run when 'Try' runs correctly the code then only runs the 'else'
# finally: always clean the tasks   (finally and try will runs will definitely)

# other programming languages will 'catch=except' 

# try: 
#     a = int(input('enter num1')) 
#     b = int(input('enter num2'))  
#     print(a/b)
# except: 
#     print('some exception occured')   #some exception occured

#-----------
# try: 
#     a = int(input('enter num1')) 
#     b = int(input('enter num2'))

#     print(a/b) 

#     # conect to database  
# except Exception as e:  # error stired in 'e' 
#     print(e)    #invalid literal for int() with base 10: 'abc'
          
# else: 
#      print() 
#      print 

# finally: 
#     print() 
#     #cleaned tasks 

#------------------


# try: 
#     a = int(input('enter num1')) 
#     b = int(input('enter num2')) 
#     print(a/b) 

# except ZeroDivisionError as e: 
#     print(e) 
#     print('go back to 2nd class and learn and come') 

# else: 
#     print() 
#     print
# finally: 
#     print()    


# division by zero
# go back to 2nd class and learn and come 

try: 
    a = int(input('enter num1')) 
    b = int(input('enter num2')) 
    print(a/b) 

except ZeroDivisionError as e:  # specific should keep in first 
    print(e) 
    print('go back to 2nd class and learn') 

except ValueError as e: 
    print(e) 

except Exception as e:  # generic should be keep in last 
    print(e) 
else: 
    print('') 
    print

finally: 
    print('finally')


#-------------------Exceptions--------------

# 1.Errors ==> syntax error;           Exceptions (runtime) 
# 2. Built in Exceptions  

#         ZeroDivisionError
#         ValueError   EG: type conversion 
#         IndexError
#         KeyError
#         TypeError
#         AttributeError
#         FileNotFoundError
#         ImportError: while importing a non existing module 
#         MemoryError: eg: a=[0] * (10**10) 
#         OverflowError 
#         StopIteration
#         KeyboardInterrupt
#         Exception 
# 3.Multiple exceptions eg: except(ValueError,TypeError) 
# 4.try except else finally 
# 5.you can raise an exception also  
# 6.custom exception


try: 
    a = int(input('enter num1'))
    b = int(input('enter num2')) 

    if b<0:  
        raise ValueError ("b cannot be negative")  # manually raising the exception 
except Exception as e: 
    #logging 
    print('ValueError:' ,e)          
      