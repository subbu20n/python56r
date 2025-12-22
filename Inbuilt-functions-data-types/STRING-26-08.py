# --------------------STRINGS-------------------INBUIT FUNCTIONS---- 

# string is a sequence of characters  (indexing,slicing) will happens  

#immuatbles --->cant change values ---->reassignment possible 

# str1 = 'subbu' 
# str1 = 'hi' # reassignment  
# print(str1) #hi 

#--------------ACCESSING STRING ELEMEMNTS---------------- 

#---------------------INDEXING--------------------------- 

# s = 'python' 
# print(s[0]) #p
# print(s[-1]) #n 


#--------------------slicing----------------- 

# s = 'python' 
# print(s[0:3]) #pyt
# print(s[3:])#hon
# print(s[:3])#pyt 
# print(s[-3:]) #hon 
# print(s[:]) #python 

# #-----------------------CONCATENATING---------(ADDING)----------- 

# str1 = "hello" 
# str2 = "subbu" 
# print(str1+" "+str2) #hello subbu 


# # ----------------REPETITION------------------------(multiply)  
# str1 = "hi" 
# print(str1 * 3)  #hihihi 



#************------------------------INBUILD METHODS-------------------[STRING]------------************

#----------------------------strip()----------------------------------

#strip() : -- will removes spaces 

# text = ' hello subbu ' 
# print(text.strip())  #hello subbu 

# print(text) # ' hello subbu '  

#----------------------------lower()---------------------------------

# str1 = 'bAD Morning !23' 

# print(str1.lower()) #'bAD Morning !23' 
# print(str1) #'bAD Morning !  

#---------------------------upper()------------------------------

# str1 = 'good morning' 

# print(str1.upper()) #GOOD MORNING
# print(str1) #'good morning'  

#------------------------SWAPCASE--------------------------- 
# upper case becomes lower case  

# str1 = 'Good MORning' 

# print(str1.swapcase()) # gOOD morNING
# print(str1)       #Good MORning  


#-----------------------------FIND-----------------------------  

# str1 = 'good morning' 
# str1.find('ning') 
# str1.find('bad') 
# print(str1.find('morn' .upper()))  
# #print(str1.find()) 

# print(str1.find('o'))#1 
# print(str1.find('o',5,10)) #6 it finds index in that string 


#----------------------------REPLACE------------------------------- 

# str1 = "good morning" 
# print(str1.replace('good', 'bad')) #bad morning 
# print(str1) #good morning 

# #-------------------------------STARTSWith---------------------- 

# text = "hello" 
# print(text.startswith('he')) #true  

# print(text.startswith('ee'))  #false  

# # --------------------------------ENDSWITH------------------------ 

# text = "hello" 
# print(text.endswith('eh')) #false 

# print(text.endswith('lo')) #True 
# print(text.endswith(' lo'.strip())) #.strip() will remove spaces 

# #-----------------------------------count------------------------- 

# str1 = 'goodgoodmorning' 
# print(str1.count('g')) #3
# print(str1.count('G')) # 0 

#----------------------split--------------------------------[imp] 
# split[delimeter]  [coma seperated values] (csv) 

#splits a string into a list  

# text = "a,b,c" 
# print(text.split(','))  #['a', 'b', 'c'] 

# s1 = 'a,b,c,,d' 
# print(s1.split(',')) #['a', 'b', 'c', '', 'd'] 

# s1 = 'a,b,c,,ce' 
# print(s1.split('c')) # here c is used as 'coma(,)'  #['a,b,', ',,', 'e']

# s1 = 'a,c,b,d' 
# print(s1.split()) # ['a,c,b,d']  # you didnt give anything it gives same  


# s1 = 'a,b,c,,c e' 
# print(s1.split())  #['a,b,c,,c', 'e']

# str1 = input()  # for this we can at a time 'csv' formant  coma seperated values will give for us 
# str1 = input() 
# str1 = input()  #like this we give means "lateset one will pick" --> this one 
#----- 

# same above one we can give like this  

# input_strs = input('Enter all 3 nums in csv ').split(',')  #inputs 10,20,30 
# print(input_strs) #['10', '20', '30']


#-------------------------------JOINS------------------------------------------- 
l  = ['s','u','b','b','u'] 
s = " "
for i in  l: 
    s = s +"-"+ i 
print(s)  #-s-u-b-b-u 

l  = ['s','u','b','b','u']  
s = "-" .join(l) 
print(s)  #s-u-b-b-u