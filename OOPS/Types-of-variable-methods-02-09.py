#----------TYPES OF VARIABLES AND TYPES OF METHODS--------------------- 

# CONSTRUCTOR---> automatically adding variables  
# constructor - is also a type of method   
# constructor - is a special method which runs every time to create a object  

# class Calculator: 
#     def __init__(self):
#         print('object is created') 
#     def add(self, a,b): 
#         print(a+b) 

# clc1 = Calculator()  #object is created
# clc2 = Calculator()    #object is created         
# print(clc1.add(2,3)) #5  




# class Calculator: 
#     def __init__(self, id1, mfg_date1, mrp1): 
#         self.id = id1 
#         self.mfg_date = mfg_date1 
#         self.mrp = mrp1 
#         print('object is created') 
#     def add(self, a,b): 
#         print(a+b) 

# clc1 = Calculator(1,'02-sept',300)   
# clc2 = Calculator(2,'02-sept',400)             
# print(clc1.add(2,3)) #5 


# class Calculator: 
#     def __init__(self, id1, manf_date1, mrp1): 
#         self.id = id1 
#         self.manf_date = manf_date1 
#         self.mrp = mrp1 
#         print('object is created') 

#     def add(self, a, b):
#        print(a + b)  

#     def introduce(self): 
#         print(self.id,self.manf_date,self.mrp) 

# clc1 = Calculator(1,'02-sept',200) 
# clc2 = Calculator(2,'02-sept',300) 

# clc1.introduce() 
# clc2.introduce() 

# clc1.expiry_date = '03-sept'  # adding manually to clc1 


#-----------------TYPES OF VARIABLES-------------------------- 

#               1.Instance Varaibles  
#               2.class/static variables   ---> in this class&static same  

#----------------TYPES OF METHODS------------------------------ 

#                  1.Instance 
#                  2.Class 
#                  3.static   #in methods static is different and class is different  


#--------------------------Types of Variables---------------------------  

#INSTANCE VARIABLES--> are those variables whose values depends on object 

#CLASS/STATIC --> never depends on instance variable value will be same for all class objects those will call CLASS/STATIC  only depend on class object 

# when we want to accept the instance variable -- instance must be available  
# wwe never call with "class name with instance" 
# we can call with "instance with class variable" 
# we can call with"class variable with class name"  



class Calculator: 

    company_name = 'CASIO' #class /static variable 

    def __init__(self, id1, manf_date1, mrp1): 
        self.id = id1 
        self.manf_date = manf_date1 
        self.mrp = mrp1 
        print('object is created') 

    def add(self, a, b):
       print(a + b)  

    def introduce(self): 
        print(self.id,self.manf_date,self.mrp) 

clc1 = Calculator(1,'02-sept',200) 
clc2 = Calculator(2,'02-sept',300) 

clc1.introduce()  #object is created
clc2.introduce()  #object is created


#print(clc1.id) 
#print(Calculator.id)   #AttributeError: type object 'Calculator' has no attribute 'id'
print(clc1.company_name) #CASIO 
print(Calculator.company_name) #CASIO 


#----------------------------TYPES OF METHODS------------------------------------  

# we will classify this "types of methods based on types of variables" 

# INSTANCE METHOD--> in any method which has Instance variable it we can directly call it as "instance method" 
# CLASS METHOD --> Any method in which you use only class/static variables -atleast on instance variables also wont use in this method then it call it as a 'class method"  
# STATIC-METHOD --> in this any relevant "class variable and static varible never use in this" 

class Calculator: 

    company_name = 'CASIO' #class /static variable 

    def __init__(self, id1, manf_date1, mrp1): 
        self.id = id1 
        self.manf_date = manf_date1 
        self.mrp = mrp1 
        print('object is created') 

    def add(self, a, b):
       print(a + b)  

    def introduce(self): 
        print(self.id,self.manf_date,self.mrp) 

    @classmethod 
    def change_company_name(cls,new_name): # in this atleast 1 instance variable also i didnt used so it class mthod  
        cls.company_name = new_name      

    @staticmethod 
    def describe_company(): # in this no need to write here "self", "cls" 
        num1 = 100 
        print('50 years') 
        print('100 years') # in these variables didnt have in "class and instance variables" also ok 


clc1 = Calculator(1,'02-sept',200) 
clc2 = Calculator(2,'02-sept',300) 

clc1.introduce()  #object is created
clc2.introduce()  #object is created

clc1.describe_company() # we can call by using "instance with method" 

clc1.change_company_name('NEW CASIO')# here no need to pass "cls" -class definition -it passes automatically  

print(clc1.company_name)

Calculator.introduce() # here we need to pass the variables  
Calculator.introduce(clc1) # we can call like this only we pass the "object" here definitely 
 
#print(clc1.id) 
#print(Calculator.id)   #AttributeError: type object 'Calculator' has no attribute 'id'
print(clc1.company_name) #CASIO 
print(Calculator.company_name) #CASIO   
