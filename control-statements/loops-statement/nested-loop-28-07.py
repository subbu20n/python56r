#NESTED LOOPS

#class 1 roll 1
#class 2 roll 1 
# for roll_no in range(1,31): 
#     print('class1',"roll","roll_no")

# for roll_no in range(0,31): 
# #     print('class2','roll',roll_no)  

# count = 0 
# for  class_no in range(1,5):
#     #print(class_no) 
#     for roll_no in range(1,11):
#         count += 1 
#         print('class',class_no,'roll',roll_no)
# print(count)        

# print(count)        
 
# count=0 
# for class_no in range(1,5): 
#     for roll_no in range(1,15): 
#         count += 1  
#         print('class',class_no,'roll',roll_no) 
# print(count)         


# ------I need to get TABLES form 1 - 20 tables ------------ 


# for j in range(1,11): 
#     for i in range(1,21):
#        print(j,'x', i , '=' ,j * i) 
 

# #----------- all classes i need even roll numbers  ----------
for class_no in range(1,4): 
    for roll_no in range(1,10): 
        if roll_no % 2 == 0:  
            print(roll_no)
        
# # all classes i need even class numbers 
# for class_no in range(1,11): 
#     for roll_no in range(1,31): 
#         if class_no % 2 == 0:  # (here it checks 300 times "slower" here)
#             print('class', class_no, 'roll', roll_no)               


# # all classes i need even class numbers 
# for class_no in range(1,11): 
#       if class_no % 2 == 0: # (here it checks only 10 times its "faster" here) 
#          for roll_no in range(1,31): 
#             print('class', class_no, 'roll', roll_no)                

#30-07.py#  

# for class_no in range(1,11): 
#     roll_no = 1
#     while roll_no < 31: 
#         print('class',class_no, 'roll', roll_no)
#         roll_no += 1  

#3.JUMP STATEMENTS 

#BREAK 

# for i in range(1,31): 
#     print(i) 
#     if i == 5: 
#         break
#     print(i)        

# for i in range(1,31): 
#      if i < 5: 
#        print(i) 
#        print(i) 

#      elif i == 0 :  
#          print(i)  

# for i in range(i, 2678): 
#     print(i * 2678) 
#     break      
# print( i *  2678)                                     

# for i in range(1,31): 
#     if i < i * (-1): #
#         break 
#     print(i ** 2)


# for i in range(0,31): 
#     if i < i * (-1) or i % 5 == 0: #0%5=0 satisfied break wont print anything 
#         break 
#     print(i ** 2)  

# #CONTINUE     

# for i in range(1,31):
#     print(i) 
#     print(i) 
#     if i == 5: 
#         continue 
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

# for class_no in range(1,11): 
#     for roll_no in range(1,31): 
#         if roll_no == 5: 
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
                  


# num1= 15

# if num1 > 10: 
#     pass
# else: 
#     print('odd number')     


# for class_no in range(1,11): 
#     for roll_no in range(1,31): 
#         if class_no % 5 == 0 or roll_no < 15: 
#             break 
#         print('class', class_no , 'roll' , roll_no)
