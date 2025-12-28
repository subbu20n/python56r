#----------LIST-MATRIX----------SRAVAN SIR--------PS-------------

# #Q. find sum of 2 largest elements among 3 [wipro] 
# a,b,c = 55,2,98 
# #o/p - a+c = 153 
# a,b,c = map(int,input('enter').split())
# if a > b and a > c: 
#     if b > c: 
#         print(a+b)  
#     else: 
#         print(a+c) 
# elif b > c and b > a: 
#     if a > c: print(a+b) 
#     else: print(b+c) 

# else: 
#     if a > b: print(c+a) 
#     else: print(c+b)      


#q.----------- i/p rotation of matrix -------------     8.8lpa 
#m = [[1,2,3],[4,5,6],[7,8,9]]  

m = [[1,2,3],
     [4,5,6],
     [7,8,9]]  
for i in range(len(m)): 
    for j in range(len(m)-1,-1,-1): 
        print(m[j][i], end=' ') 
    print()      