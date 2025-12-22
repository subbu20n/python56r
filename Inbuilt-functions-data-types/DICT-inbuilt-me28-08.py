#-----------------------DICT----INBUILT FUNCTIONS--------------------- (indexing)-not possible (mutable) 

#DICT and its inbuilt functions: which consists of key  and value pair 

#d = {key=value, key=value}  

#--------------------INBUILD FUNCTIONS----------------------- 
#                1. d.get(key) 
#                2. d.key() 
#                3. d.values() 
#                4. d.items() 
#                5. d.update({}) 
#                6. d.pop({})
#                7. d.clear() 
#                8. d.copy() 
#                9. zip(keys,value) 
#                10. From keys[], similar value

#-------------------1. d.get(key)-------------------------------- 
# d.get(key): it is used to display particular values of  key 

# dict = {'name': 'subbu','gender': 'male','age': '22'} 

# print(dict.get('name')) #subbu
# print(dict.get('age'))  #22
# print(dict.get('gender')) #male  

# print(dict.get('DOB', 'N/A')) #N/A
 

# # for avoe one code 

# d = {'name': 'subbu','gender': 'male','age': '22'} 
# for i in d: 
#      if i == 'name': 
#           print(i) 
#           break 
#      if "name" not in d: 
#           print('none') 
#           break  

#----------------------2.d.key()--------------------------------------
# d.key()--> it is used to get all keys of a dict  

# d = {'name': 'subbu','gender': 'male','age': '22'} 
# print(d.keys())  #dict_keys(['name', 'gender', 'age'])  

# print(list(d.keys()))  #['name', 'gender', 'age']  

# print(set(d.keys())) #{'name', 'age', 'gender'}
# print(tuple(d.keys())) #('name', 'gender', 'age')


#---------------------------3.d.values()--------------------------------- 
# d.values()----> it is used to get all values 

# d = {'name': 'subbu','gender': 'male','age': '22'}
# print(d.values())  #dict_values(['subbu', 'male', '22'])


#------------------------4.d.items()------------------------------- 
#d.items()--> it is used to get all "key and values"

# d = {'name': 'subbu','gender': 'male','age': '22'}
# print(d.items())      #dict_items([('name', 'subbu'), ('gender', 'male'), ('age', '22')])

# for i in d.items():   #d.items ---> is used to all "key and values"
#     print(i)  
# d.items()  #('name', 'subbu')
#             #('gender', 'male')
             # ('age', '22') 
 
#-------------------------------- 

#----------------------------------5.d.update({})---------------------------------------
#d.update({}) ----> it is used to modify existing key value pair and or to create new key value pair  

# d = {'name': 'subbu','gender': 'male','age': '22'} 
# d.update({'name':'sanju'})
# print(d)  #{'name': 'sanju', 'gender': 'male', 'age': '22'}  

# d.update({'Secondname':'sree'}) # it will adds in last  
# print(d)         #{'name': 'sanju', 'gender': 'male', 'age': '22', 'Secondname': 'sree'}  

# n = input("enter")  
# d = { 'I':1,'II': 2,'III': 3,'IV': 4,'V': 5, 'VI': 6,'VII': 7,'VIII': 8,'IX': 9,'X': 10} 
# print(d.get(n))  #ENTER:V - '5' 

#same method of above one  

# n = input() 
# d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
# sum = 0 

# for i in range(len(n)): 
#     if i < len(n-1) and d[n[i]] > d  [n[i+1]] : 
#         sum -= d[n[i]]  #if number have bigger one i am reducing the number 
#     else: 
#         sum += d[n[i]]  # if number have smaller one and i am increasing it  


# -----------------------------d.pop()--------------------------------- 
#d.pop(key) ----> it used to remove unwanted key value pair by using its key 

d = {'name': 'subbu','gender': 'male','age': '22'}  
d.pop('gender')  
print(d)  #{'name': 'subbu', 'age': '22'} --> removed  
#d.pop('id')  #we did not have key of 'id' so it gets error 
print(d.pop('id' ,'N/A')) 
