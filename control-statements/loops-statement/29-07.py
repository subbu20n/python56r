# # --------nested loop ----------- (madam) 

# m = [1,23,1],[3,7,8],[7,9,3] 
# count = 0
# for row in m: 
#      for value in row: 
#           count += value 
#      print(count) 

# n=4 
# for  i in range(1,n +1): 
#      for j in range(1,i +1): 
#           print(j, end='') 
#      print()       

 

# n = 3
# for i in range(1, n +1):
#     for j in range(1, i +1): 
#         print(j , end=' ')        
#     print() 

i = 3 
while  i <= 3: 
      j = 1 
      while j <= 3: 
           print(j, end=' ') 
           j += 1 
      print() 
      i += 1 

i = 'A'
while i <= 'C': 
     j = 'A' 
     while j <= 'C': 
          print(j , end=' ') 
          j += 'A'           
     print()     
     i += 'A'
print()    