# # ---------------arbitory arguments --------------------- 

# def connect_to_db(*args): 
#      print(args)
# connect_to_db('localhost:3300','2248','3456','0987')   
# print()

# # ---------------keyword arbitary arguments (**kargs)----------------------


# def connect_to_db(**args): 
#      print(args)
# connect_to_db( db_loc ='localhost=3300',db_pool='2248',db_number='3456',db_code='0987')   
# print()

#---------------------RETURN----------------

# def add(num1,num2): 
#      return num1 + num2  #we need to store the value define value 
# add(2,5) 
# res = add(2,5) 
# print(res) #7 
# print(add(4,5)) #9 
# print(res * 5) #35 7x5 =35 

# def add(num1 , num2): #num1=2 num2 = 5 
#      return(num1 + num2) #2+7 return 

# r = add(2,5)  #r=7
# print(r)   #7 
# print( r * 5) #7x5=35 

# print(add(4,5))

# def even_or_odd(num1): 
#      if num1 % 2 == 0: 
#           return 'EVEN '
#      else: 
#           return 'ODD' 
# r1 = even_or_odd(23) 
# print(r1) 
 
# -----#multiple values can be retun in simgle line statement  we can return the values -----
# def simple_calculator(a,b): 
#      return a+b, a-b, a*b 

# r2 = simple_calculator(2,4) 
# print(r2)
# print(type(r2)) #

def subbu(a,b): 
     return a+b, a*b, a-b 
r1 = print(subbu(2,5))

# def simple_calculator(a,b):    # this typr wont work multiple values
#      return a+b         -----> # here it will end the execution  
#      return a-b 
#      return a*b 
# simple_calculator(2,3)

# def even_or_odd(num1): 
#      if num1 % 2 ==  0: 
#           return 'EVEN' 
#      else: 
#           return 'ODD' 

# r1 = even_or_odd(22)  #EVEN 
# r2 = even_or_odd(23) #ODD  

# print(r1) 
# print(r2) 


# def check_ur_knowledge(num1): 
#      for i in range(1,num1): 
#           print(i) 
#           if  i == 9: #1,2,,3,4,5,6,7,8,9 -->condition satisfied Return None 'nothing wrote" 
#                return # didnt wrote so "None" will display ok 
#      return '55'
 
# print(check_ur_knowledge(22))



def check_ur_knowledge(num1): 
     for i in range(1,num1): 
          print(i) 
          if  i == 9: 
               return 
     return '55' #55 

print(check_ur_knowledge(8))
