#-------------------Fibonacci series----------------------------- 

#"f{n} = f(n-1) + f{n-2}" ---> we need to add 1st and 2nd number to get -'3rd number' this is 'fibonacci series' 
# (present value and previous value) we need to add   --> ok 

num1, num2 = 0,1 

n = 10 

for i in range(0,n):
    print(num1)#0,1,1
    third_num = num1 + num2  #0+1= 1 ,1+1=2 
    num1 = num2  
    num2 = third_num 



#-------This is corect way------------------- to get fibonacci 
# python first calculates  -right side 


num1 = 2 
num2  = 3  

n = 10 

for i in range(0,n): 
    print(num1) #---> here new value will print ok 
    num1, num2 = num2 , num1 + num2   # here python calculates first right side part num1 =num2= 2+3 =5 

