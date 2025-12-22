
#---------    3.JUMP STATEMENTS  --------------- 

#------------BREAK --------------------  

# for i in range(1,31): 
#           print(i) #--5 iterations happened  1,2,3,4,5 
#           if i == 5: 
#              break 
#           print(i)# only 1,2,3,4 iteration happened  

# for i in range(1,21): 
#      if i < 5: 
#            print(i) 
#      elif i == 5: 
#            print(i) 
                 

# for i in range(1,31):  
#      if i < 5:  
#        print(i) 
#        print(i)  

#      elif i == 0 :  
#          print(i)  
          
# for i in range(1,31): 
#     if i < i * (-1): #  i > i *(-1)  --> this condition never satisfied 
#         break 
#     print(i ** 2) 

 


# for i in range(0,31): 
#     if i < i * (-1) or i % 5 == 0: #0%5=0 satisfied break (wont print anything)
#         break 
#     print(i ** 2)   


# ---------------CONTINUE ------------------- 


# for i in range(1,20): 
#     print(i) 
#     print(i) 
#     if i == 5: 
#         continue  # continue effect only that iteration satisfied only  it wont effect all 
#     print(i)

# for i in range(1,31): 
#     print(i) 
#     print(i) 
#     if 1 == 5 or i == 6: 
#         continue 
#     print(i)    

# for i in range(1,45):  
#     continue 

# i = 5  

# while i < 25: 
#     print(i) 

#     i -= 1  # negative numbers also will work here 5,4,3,2,1,0,-1 -2 -3  

#     if i % 5 == 0: 
#         break 

# i = 10 
# while i < 25: 
#     print(i) 
#     i -= 1 
#     if i % 5 == 0:  
#         break 
#     print(i)     

# for class_no in range(1,11): 
#     for roll_no in range(1,31): 
#         if roll_no == 5:   #every class print rollno 1,2,3,4 only then break 
#             break    
#         print('class' , class_no , 'roll_no', roll_no)
         


# for class_no in range(1,11): 
#     if class_no == 4:
#         continue 
#     for roll_no in range(1,31): 
#         if roll_no == 5:  
#             break    
#         print('class' , class_no , 'roll_no', roll_no)
         

# for class_no in range(1,11): 
#     if class_no == 4:
#         continue 
#     for roll_no in range(1,31): 
#         if roll_no == 5: 
#             continue    
#         print('class' , class_no , 'roll_no', roll_no)
                  

#-----pass------ 

# num1 = 9 

# if num1 > 10:  #odd number (9)
#     pass 
# else: 
#     print('odd number')

# num1= 15

# if num1 > 10: 
#     pass
# else: 
#     print('odd number')     




for class_no in range(1,11): 
    for roll_no in range(1,31): 
        if class_no % 5 == 0 or roll_no < 15:  
            break  
        print('class', class_no , 'roll' , roll_no)
 

for class_no in range(1,11): 
    for roll_no in range(1,31): 
        if class_no % 5 == 0 or roll_no < 15:  
            break  
        print('class', class_no , 'roll' , roll_no)
 