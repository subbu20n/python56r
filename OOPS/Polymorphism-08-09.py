#------------------polymorphism-------------------------------- 

#polymorphism ---> depending the places or menbers cahnging the behavior  

#polymorphism --> similarly in oops also different situations will change like that so it called polymorphism 

#------------polymorphism------------------------- 

#           1.method over loading 
#           2. method over riding  
#           3. operator overloading 
 
#method overriding ---> in parent class and child class -we write same method it calls methos over riding 
# method over riding --> based on the object it changes its implementation 

# ---method over loading------------------ 

# method over loading --> in python method over loading not possible 
# with same name 2 or more functions at in one place it dippefers based on function  

# def add(a,b):    # in python latest one will pick 
#     return a + b 

# def add(a,b,c):  # in other programming languages it can with same name 2 functions also in python not possible latesone will pick it 
#     return a + b+ c  

#----why "METHOD OVER LOADING" included in polymorphism ----------------

def add(*a):  #arbitary argument  -all goes to a only  right so its possible in python liek this  
    return sum(a) # in python indirectly we can use "arbitary arguments" 

add(2) 
add(2,3) #without seeing function definition what u think he is calling four functions  like that  
add() 
add(2,3,4,5)  


#--------------------OPERATOR OVER LOADING-------------------------------- 

# you are giving "+" operator giving differnet works  

2 + 3  
'2' + '3' # like this doing different works"+"  opearion is same doing different works "string,list,integer"
[1,2] + [3,4]  # idi work avvali ante (__add___)  --method unte work avutundi lekunte work avadu 


# ----why OPERATOR OVER LOADING - included in polyorphism-------------- 

# if you give 'string' it works on 'string operands' 
# if you give 'list' it works on 'list operands' 

#""when we are creating a object finally it has to convert to method. --> if method dont have means it throw a error"
# class Marks: 
#     def __init__(self, so_marks,math_marks):
#         self.so_marks = so_marks 
#         self.math_marks = math_marks 

# m1 = Marks(90, 32) 
# m2  = Marks(35,92) 

# m1 + m2  #TypeError: unsupported operand type(s) for +: 'Marks' and 'Marks'--> "for this mtehod not have"

class Marks: 
    def __init__(self,so_marks,math_marks): 
        self.so_marks = so_marks 
        self.math_marks = math_marks 

    def __add__(self, other): 
        print('Nenu add chesanu') 
        print(self.so_marks + other.so_marks) #125
        print(self.math_marks + other.math_marks)  #124  
m1 = Marks(90,32) 
m2 = Marks(35,92) 

# m1 + m2 #125,124 
# #m1.__add__(m2)


class Marks2: 
    def __init__(self,so_marks,math_marks,sc_marks):  
        self.so_marks = so_marks 
        self.math_marks = math_marks 
        self.sc_marks = sc_marks 
mark2_obj = Marks2(10,20,30) 

m1 + mark2_obj  # this is "DUCK TYPE" in polymorphism ----in Advance python comes this duck type ok 

