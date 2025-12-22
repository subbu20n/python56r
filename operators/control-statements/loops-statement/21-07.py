#-----LOOPING STATEMENT---------- 

#----LIST----

list = [10,11,3] 
for n in list: 
     print(n)   


# ---- TUPLE------
t = (1,2,3,4) 
for i in t: 
     print(i, end=",",) 

# ----- SET---- 
s = {10,29,40} 
for i in s: 
     print(i)

#-----DICT--------- 
d = {'k': 'subbu','s': 21} 
for i in d.items(): 
     print(i) 

#---- string---- reverse order 
s = "subbu" 
for i in s[ : : -1]:
     print(i)

#-------characters COUNT ------- 
s = 'subbu' 
count = 0 
for i in s: 
     count += 1 
print(count) 

# ------Formal string ----- f{} --to get 2 -TABLE
n = 2 

for i in range(1,11): 
     print(f'{n} x {i} = {n * i}')

# -----VOWELS 'AEIOU' Print cheyali-------- 
n = "subbarayudu" 
count = 0 
for i in n: 
     if i in 'aeiouAEIOU': 
          print(i) 
          count += 1 
print(count)          
# number ni iterate cheyalemu 
# num = 20 

# for i in num: 
#     print(i) #TypeError: 'int' object is not iterable  

# num = 20 

# for i in range(0 , num+1, 2):
#     print(i)  #0,2,4,8,10,12,14,1,6,18,20 
 
# n = 2 

# for i in range(1 , 11): 
#      print(f'{n}') #  it takes n value 2 will prints 11 times 

# s = 'hello PYTHON' 
# count = 0 
# for i in s: #e o, O vowels 
#       if  i in 'aeiouAEIOU':
#            count+=1 
# print(count) #3 