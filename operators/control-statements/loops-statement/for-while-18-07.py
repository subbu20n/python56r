# --------LOOPS for and while -------

#  loops
#  advntages of loops
#----Iterable----: list,set,dict,string,tuple,range  


# ------for and while---------- 

# ------------FOR--------------  

for i in range(0, 10): 
    print('hi') 
    print('hello subbu')    
print('subbu')   
                    
for i in range(0,10): 
    print(i)  # it also show you iteration times 
    print('hi') 
    print('Good morning') 
print('sun')                         

n=40 
for i in range(n):   #by default it takes-0  (0,40)--like this
    print(i)

# --------i want even numbers----------- 
n = 20 
for i in range(n): 
    if i % 2 == 0: 
        print(i)


# # ---i want even numbers -----above also same  
# n = 40 
# for i in range(0,n,2):
#     if i % 2 == 0: 
#         print(i) 


# ------------WHILE LOOP---------------------[condition based]
# --> while loop is based on condition  "till upto condition satisfied its continously looping"  
# i = 5 
# while i > 3 : #satisfied so unstoppable printing (python) till we manualy stops 
#     print('python') 

# # i = 5 

# # while i > 3: #3 - 3 = 0 
# #     print('python')  
# #     i = i-1  #5-1 =4 , 4=4-1=3 , 

# # is_vishwa_alive=True 

# # while is_vishwa_alive: 
# #     print('subu') 
# #     is_vishwa_alive=False 

is_akhanda_success = True 

while is_akhanda_success: 
    print('Success') 
    is_akhanda_success = False 

# num1 = 1 
# while num1 > 10: #here num1 is greater than 1 ayite print(num1) we gave 
#     print(num1) 
#     num1 += 1 

# num1 = 11 
# while num1 > 10: #11 gt 10 satisfied 
#     print(num1) #num1=11 
#     num1 += 1 # 11 +1 =12 --> then again iterate "unstoppable" 

# num1 = 9 

# while 9 < 10: #9 lt 10 --satified 
#     print(num1) #9 
#     num1 -= 1  #9-1 = 8 --> again iterate and until "unstoppable"9876543210-1-2-3-4-5-6-... 

# num1 = 9 

# while num1 < 10 and num1 >= 0:  # here 2 conditions has to satify and then it prints 
#     print(num1) 
#     num1 -= 1      #9-1 =8 --> it will iterates again until 0 it when unsatisfied then only we go 


# ------ASCII VALUES -------------

print('@' > '5')
print('A' > 'a')

