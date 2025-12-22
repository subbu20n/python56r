# -----------------------OOPS-------(Object oriented programming skills)--------------------------

#    --------- oops-advantages -------

#       1.Data security 
#       2 . code readability 
#       3. code maintainability 
#       4. code reusability 
#       5. customazability 
#       5. code scalability .......

# till now we wrote ("procedural programming ") 
#-----------------procedural programming (disadvantages)-(issues)--------------------- 
#             1.code mainatainability 
#             2. code security (data security) 
#             3. code reusability 
#             4. code scalability 

# -------so we came to "OOPS" to overcome those disadvantages of procedural programming  
# 
# in companies we write "oops" syntax only not 'procedural programming' 

#---------*******----CLASS AND OBJECT------********---------------------

# CLASS ---> blue print  
# OBJECT ---> actual instance which are going to build  

# class Calculator: 
#     pass 

# clc1 = Calculator() 

# clc2 = Calculator()
# clc3 = Calculator() 
# clc4 = Calculator()

#----------------******--VARIABLES AND METHODS ---******---------------
#VARIABLES : with the help of variables we use variables to store calculator data (we wont store data in variables) 
#MEthods : methods are nothing but functions only "but here in class" we write inside the class that is called method in procedural function we need to write userdefined everything we have to write 

# methods- inside class writing functions are methods , outside ones are normal functions  
# object --> we can call it as "instance"
# variable - data 
# METHODS - behavoral 

# class Calculator: 
#     def add(self, a,b): 
#         print(a+b) 

# clc1 = Calculator()
# clc2 = Calculator()
# clc3 = Calculator() 
# clc4 = Calculator()

# clc1.add(2,3) # (5) self is automatically will pass it no need to mention  

# "self"  ---> no need to pass 

class Calculator: 
    def add(self, a,b): 
        print(a+b) 
    def sub(selff, a,b): 
        print(a-b) 
    def describe(self): 
        print(self.id,self.manf_date)         
    def dummy(self): 
        print('jai balayya') 


clc1 = Calculator()
clc2 = Calculator()
clc3 = Calculator()  # we can call multiple functions  so i wrote no . of functions  ok 
clc4 = Calculator()

clc3.add(2,3) #its work 
#add(2,3) ----> it does not work 

#MANUALLY adding data  
clc1.id = 1234 
clc1.manf_date = '01-sept' 
clc1.mrp = 400 
clc2.id = 1345 

#print(clc1.id)# 1234 #
print(clc2.id) # error not declared 'id'
clc1.describe() #1234,01-sept 
#clc2.describe() #AttributeError: 'Calculator' object has no attribute 'manf_date' 
clc4.dummy()

 
