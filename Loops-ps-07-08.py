#-----------LOOPS PS QUESTIONS--------------- 

#----------ALL NATURAL NUMBERS------------- 

# n = 100 
# for i in range(1, n+1): 
#     if i % 1 == 0: 
#         print(i)  

# start=1 

# while start <= 100: #1 lt = 100 (100 also will print)
#     print(start)  #1

#     start += 1  # start + 1 = 1 + 1 =2 ==> 2 +1 =3  


#---------EVEN NUMBERS WILL PRINT -----------
# start=2 

# while start <= 100: #1 lt = 100 (100 also will print)
#     if start % 2 == 0: # 2 % 2 = 0  -->so it prints 
#       print(start)  # only "even numbers" will print 

#     start += 2  # start + 1 = 1+2 = 3  ==> 2+3=5  3+8= 11 --like that it will iterate   


# n = 57 

# sum = 0 
# for i in range(1, n + 1): 
#        sum + i  # we need to store the value reassignment 
#        sum = sum + i # now it works 
# print(sum) 


# print((n * (n+1)/2)) 


# start =1 
# sum = 0

# while start <= 100: 
#        print(start) 
#        sum = sum + start 
#        start += 1 
# print(sum)        

# write a program that keeps asking the user to enter number until them  enter a negative number  use a while loop 

# while True: 
#     ip_num = float(input('Enter a negative number'))
#     if ip_num <= 0: 
#         break  

#     ip_num = float(input('Enter positive number')) 
#     if ip_num > 0: 
#         ip_num = float(input('Enter a positive number')) 


ip_num = float(input('Enter a positive number')) 
if ip_num <= 0: 
    print ('Negative number entered') 

while ip_num > 0: 
   ip_num = float(input('ENter positive number')) 
   if ip_num <= 0:  
       print('Negative number entered ')   