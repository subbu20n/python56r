#-------------INHERITANCE METHOD OVERRIDING & METHOD OVER RESOLUTION----------------- 

# class Calculator:  
#     company_name = 'CASIO'
#     def add(self, a,b): 
#         print( a + b) 

#     def sub(self, a, b): 
#         print(a - b) 

# #child clas # subclass #derive class 
# class AdvCalculator(Calculator):              
#     def floor_div(self,a): 
#         return a // 2 
    
# adv1 = AdvCalculator() 
# #adv1.add(2,3) 
# print(AdvCalculator.company_name) #class property not only methods variables also accepted  ok 

# #CASIO  

#---------

# class Vehicle: 
#     def drive(self): 
#         print('vehicle in drive mode') 

# class Car(Vehicle): 
#     def brakes(self): 
#         print('car brakes applied') 

# v1 = Vehicle()
# v1.drive() # vehicle in drive mode

# #v1.brakes() # cannot possible to call instnace variable it must want instance variable to call instance method  

# c1 = Car()
# c1.drive() #vehicle in drive mode  # we will call this "METHOD OVER RIDING" 
# c1.brakes() #car brakes applied  
#--------- 

# class Vehicle: 
#     def drive(self): 
#         print('vehicle in drive mode') 

# class Car(Vehicle): 
#     def drive(self): 
#         print('car in drive mode')
#     def brakes(self): 
#         print('car brakes applied')  

# class TeslaCar(Car): 
#     pass 

# elon = TeslaCar()  # we will call this as 'method over riding' 
# elon.drive() # in tesla did not have drive sir --> it checks in next hierarchy means in "car" is there drive  

# #car in drive method  

# v1 = Vehicle()
# v1.drive() # vehicle in drive mode

# #v1.brakes() # cannot possible to call instnace variable it must want instance variable to call instance method  

# c1 = Car()
# c1.drive() #vehicle in drive mode  # we will call this "METHOD OVER RIDING" 
# c1.brakes()  

#------------ 

#multilevel  

# class Vehicle: 
#     def __init__(self,vehicle_id,vehicle_type):  
#         self.vehicle_id = vehicle_id 
#         self.vehicle_type = vehicle_type 
#         print('vehicle constructor') 

#     def drive(self): 
#         print('vehicle in drive mode') 

# class Car(Vehicle): 
#     # def __init__(self): 
#     #     print('car cocnstructor')  #without this it get 'vehicle onstructor'  

#     def drive(self): 
#         print('car in drive mode') 

#     def brakes(self): 
#         print('car brakes applied') 

# #c1 = Car()  # first it checks in local in local have means it check in vehicle   #"car constructor" 
# cl = Car(23,50) #vehicle constructor  
#--- 

#*******-------adding "super().drive"---********

# class Vehicle: 
#     def __init__(self,vehicle_id,vehicle_type):  
#         self.vehicle_id = vehicle_id 
#         self.vehicle_type = vehicle_type 
#         print('vehicle constructor') 

#     def drive(self): 
#         print('vehicle in drive mode') 

# class Car(Vehicle): 
#     # def __init__(self): 
#     #     print('car cocnstructor')  #without this it get 'vehicle onstructor'  

#     def drive(self): 
#         super().drive() # it means it goes to vehicle class and goes to drive method and it runs that method 
#         print('car in drive mode')  # this is method of overriding  

#     def brakes(self): 
#         print('car brakes applied') 

# #c1 = Car()  # first it checks in local in local have means it check in vehicle   #"car constructor" 
# cl = Car(23,50)
# cl.drive()

#------- 
#adding init method  to car  

# class Vehicle: 
#     def __init__(self,vehicle_id,vehicle_type):  
#         self.vehicle_id = vehicle_id 
#         self.vehicle_type = vehicle_type 
#         print('vehicle constructor') 

#     def drive(self): 
#         print('vehicle in drive mode') 

# class Car(Vehicle): 
#     def __init__(self,vehicle_id,vehicle_type): 
#         super().__init__(vehicle_id,vehicle_type)
#         self.car_type = 'petrol' 
#         print('car cocnstructor')  #without this it get 'vehicle onstructor'  

#     def drive(self): 
#         super().drive() # it means it goes to vehicle class and goes to drive method and it runs that method 
#         print('car in drive mode')  # this is method of overriding  

#     def brakes(self): 
#         print('car brakes applied') 

# #c1 = Car()  # first it checks in local in local have means it check in vehicle   #"car constructor" 
# cl = Car(23,50)
# cl.drive()


#---
#----------------------METHOD RESOLUTION ORDER--------(MRO)------------------------ 
#example for explanation 
#MRO:  -- it checks preference in sequence  

class Lion: 
    def roar(self): 
        print('Balayya is roaring') 

class Tiger: 
    def hunt(self): 
        print('NTR is hunting') 

    # def roar(self): 
    #     print('Ntr is roaring')    
class Liger(Tiger,Lion): 
    pass 

lg1 = Liger()
lg1.roar() # in Tiger is roar method not there so it check in lion' is there then its print "balayya is roaring" 

print(Liger.mro())
print(Liger.__mro__()) 