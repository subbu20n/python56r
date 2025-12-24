#--------------******------------DECORATORS---*************---------

#DECORATOR: is also a function 

#decorators: these function adding extra functionality to existing function 

# ------------example cheptanu -----------(oops) concept  bayataku veltunnamu  ippudu----------------

#----Functions----- 

# def printer():  
#     print('printing the required documents') 

# printer()  #calling the function 

#checking requirements   #idi paina ravali 
# printing the required documents  # when i run the 'printer function()' i  need to get the values like this center has to come this one  
# Thank you    # idi kinda ravali 

# def example_decorator(func): # we need to pass the 'func' as parameter   
#        def wrapper():  #directly it  first runs directly wrapper function   
#              print('check requirements') 
#              func() # printer function will pass argument type and here runs 'printer function 
#              print('Thank you') 

#        return wrapper 
# @example_decorator   # "this is decorator using advantage"- adding extra functionality to existing function 
# def printer(): 
#       print('print the required documents') 

# printer()    # i called printer function but there o/p came from 'wrapper function in decorators usnig'  

# check requirements
# print the required documents  #o/ps came like this 
# Thank you


# def second_function(): 
#     print('check requiremnts') 
#     print('print the required documents')
#     print('Thank you')

# second_function() #here i called directly secong with writed normall type function  

# @example_decorator 
# def fax(): 
#       print('fax in process') 

# fax()   

#O/P'S
# check requirements
# fax in process
# Thank you

#-----------LETS GO BACK TO "OOPS-CONCEPT"------------------- 


#------**********------4-Main pillars of OOPS"------********-------------------- 

#                      1.Inheritance 
#                      2.polymorphism 
#                      3.Encapsualation 
#                      4.Abstraction 

#---------------------INHERITANCE----------------------------------------- 

#Inheritance:  grandparent-->parent--------->son  (inheritance only one way)  

#Inheritance: we can reuse the code ---"code reusability"
 
class Calculator:   #parent class, #super class, Base class 
      def add(self,a,b): 
            print(a + b) 

      def sub(self,a,b): 
            print(a - b) 

#child class, #sub class, # derived class 

class AdvCalculator(Calculator): # brings from "parent class to properties to child class" 
      pass 

class ScientificCalc(AdvCalculator): 
      pass 


clc1 = Calculator() 
clc1.floor_div()
adv1 = AdvCalculator() 
adv1.add(2,3) 

