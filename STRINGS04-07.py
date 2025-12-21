# '' 
# " "
# str1 = "subbu "
# print(str1) 
# print(len(str1))#6 

# str1 = '' 
# print(str1) 
# st = len(str1) 
# print(st)


# str1 = '   ' 
# print(str1) # empty string will print 
# st = len(str1) 
# print(st)#3 

# # ---INDEXING----

# str1 = "devops with aws cloud" 
# print(str1[5]) #5 


# str1 = "devops with aws cloud" 
# print(str1[5])
# print(str1[4]) 
# print(str1[9]) 
# print(len(str1)-1) #21-1 = 20 

# print(str1[-1]) 
# print(str1[-2])

# print(str1[-len(str1)])  #d -will get  

# print(str1[30]) # leni index iste #string index out of range 

# ---SLICING---- 
str1 = 'devops with awscloud' 
print(str1[5:9])

str1 = 'devops with awscloud' 
print(str1[5:5]) #empty string 


str1 = 'devops with awscloud' 
print(str1[5:9:2]) #2 - is the jump statement  

str1 = 'devops with awscloud' 
print(str1[15:5]) # slicing has to move "left to right always" --> "reverse [-1] add in jump statement"


str1 = 'devops with awscloud' 
print(str1[15:9:-1]) #till before 9 will print in reverse 'h' till h varaku print avutundi 

str1 = 'devops with awscloud' 
print(str1[15:9:-2]) # skip the position in reveres 

str1 = 'subbu' 
print(str1[-2:-5]) #emptystring 
print(str1[-5:-2]) # (sub) -it works becoz from "left to right" possible positions 
print(str1[-2:-5:-1]) #bbu 

print(str1[ : ]) #subbu -->total string print avutundi  
print(str1[ : : -1]) #ubbus --> reverse order it print 

print(str1[5: ]) #empty string 'character levu' 

#string is immutable --> we can "reassign" 