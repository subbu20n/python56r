#-----------------------ENCAPSULATION-----------------------------

#ENCAPSULATION: security for variables who have access they only access it  
# variables bind with methods 

#when users gave read permisiion it takes indirectly write permission access also
#you cannot contorl the access, you cannot control the data hanges he can chage the data by his wish 

# class User: 
#     def __init__(self,username,password'): 
#         self.username = username 
#         self.password = password 
#         

# us1 = User('subbu','arun') 
# print(us1.username)     #---> variables  
# us1.username = 'ramesh'  # he can take write access also using variable -he can reassign 
# us1.password = -6000 

# Now i wont share variable name -- "i will share method it will return you the variable name" 

# class User: 
#     def __init__(self,username,password): 
#         self.username = username 
#         self.password = password 
    

#     def get_username(self): 
#         return self.username  
    
# us1 =  User('subbu','chetan') 
# username = print(us1.get_username()) #subbu  #here we passed the 'method"  


# class User: 
#     def __init__(self,username,password,balance): 
#         self.username = username  
#         self.password = password 
#         self.balance = balance   
#     def get_username(self): 
#         return self.username 
    
#     def get_balance(self): 
#         return self.balance 
    
#     def set_balance(self,new_value): 
#         if new_value < -5000: 
#              return 'invalid balance' 
#         self.balance = new_value      
    

# us1 = User('subbu','chetan',-5000)
# username = (us1.get_username()) 
# print(us1.username)
# print(us1.set_balance(6000)) 

#we never share variables name directly  
# we never use variables name directly 

#---------------------ACCESS SPECIFIERS---------(prevent  secure some more)-------------------- 
#Access Specifiers: one variable where it can access is defines declare by "access specifiers" 

# there are 3-types of ACCESS SPECIFIERS 
# 1.public --> you can access one object  anywhere  so it becomes public variable  (self.username=username)
# 2.private  ---> it access only "Inside class definition" outside class definition it wont access (__password=password) if u want access u need to write methods  
# 3.protected  --> protected variables same as public variables (_balance=balance) 

# class User: 
#     def __init__(self,username,password,balance): 
#         self.username = username  
#         self.__password = password 
#         self._balance = balance  
    
#     def get_username(self): 
#         return self.username  
    
#     def get_balance(self): 
#         return self.balance 
#     def set_balance(self,new_value): 
#         if new_value < -5000: 
#             return 'Invalid balance' 
#         self.balance = new_value 
#     def get_password(self):
#         return self.__password    

# us1 = User('mahesh','subbu',20) 
# username = us1.get_username() 

# print(us1.username) #public 
# print(us1.get_password()) #private #subbu # without methods we cannot access private variable outside of class 
# print(us1._balance) #20 


#-----------------------------DESTRUCTOR------------------------------------------

#constructor : while creating the object 
#Destructor : while deleting the object  

#destructor: (garbage collector) -- when we complete the execution our code will automatically delete the object 
 
# class User: 
#     def __init__(self,username,password,balance): 
#         self.username = username  
#         self.__password = password  
#         self._balance = balance 
#         print('object is created') 

#     def __del__(self): 
#         print('object is deleted') 

# us1 = User('k','p',10) 

# #del us1 
# us2 = User('k','p',10)
# us3 = User('k','p',10)
# us4 = User('k','p',10) # so praogram has executed successfully while execution completes object is deleted  

#--------------------------------DUNDER METHODS---------------------------------

# dunder methods / double underscore methods / magic methods 
   
# __init__
# __add__     
# __del__ 
# dunder methods : will helps python inbuilt methods or python inbuilt operations mi ooka customize objects paina work avvadaniki help chestayi 
# (m1 + m2)  --> it wont works (m1.__add__(m2)) --> it works  

# class User: 
#     def __init__(self,username,password,balance): 
#         self.username = username  
#         self.__password = password 
#         self._balance = balance 
#         print('object is printed') 

#     def __del__(self): 
#         print('object is deleted') 

#     def __str__(self): 
#         #return self.username,self._balance #it comes tuple  
#         return self.username + str(self._balance) #k500
  
#     def __len__(self): 
#         return 50 
    
# us1 = User('k','p','500') 
# us2 = User('k','p','500') 
# print(us2)   

# print(len(us1)) #50 


class AcadClass:
    def __init__(self):
        self.students_list = []
        print('acad class is created')

    def add_students(self, name):
        self.students_list.append(name)

    def __len__(self):
        return len(self.students_list)

    def __getitem__(self, index):
        return self.students_list[index]


clc1 = AcadClass()
clc1.add_students('subbu')
clc1.add_students('ram')
clc1.add_students('raju')

print(clc1.students_list) 
print(len(clc1))

print(clc1[0]) #indexing 
print(clc1[2]) #indexing 