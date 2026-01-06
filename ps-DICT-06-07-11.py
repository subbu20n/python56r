# # -----------------------------------DICTIONARY-------------------------------------

# #Q given a list of numbers, count the occurence of each number and return a dictionary 

# l = [1,2,3,1,2,4,5,3,7,5,0,0,0,9,7] 
# d = {} 

# for i in l: 
#     c = 0 
#     for j in l: 
#         if i == j : 
#             c+=1 
#         d[i] = c  
# print(d)           # {1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 7: 2, 0: 3, 9: 1} 

#--using count method same  

# l = [1,2,3,1,2,4,5,3,7,5,0,0,0,9,7] 
# d = {} 

# for i in l:  
#     d[i] = l.count(i) 
# print(d)    # {1: 2, 2: 2, 3: 2, 4: 1, 5: 2, 7: 2, 0: 3, 9: 1} 

#------ 

#Q Given a list of words return a dictionary where the keys are words and values are their lengths  

# l = ['subbu','prasad','arun','ramu'] 
# d = {} 

# for i in l: 
#     d[i] = len(i) 
# print(d)      #{'subbu': 5, 'prasad': 6, 'arun': 4, 'ramu': 4} 

# #   using count method same  
# l = ['subbu','prasad','arun','ramu'] 
# d = {} 

# for i in l: 
#     c = 0 
#     for j in i: 
#         c = c +1 
#         d[i] = c  
# print(d)         #{'subbu': 5, 'prasad': 6, 'arun': 4, 'ramu': 4} 

#-----

#Q Given a string return a dictinary where keys are characters and values are their occurence  

# s = 'hello how are you' 
# d = {} 

# for i in s: 
#     d[i] = s.count(i) 
# print(d)     #{'h': 2, 'e': 2, 'l': 2, 'o': 3, ' ': 3, 'w': 1, 'a': 1, 'r': 1, 'y': 1, 'u': 1}

# # -----  same  -----
# s = 'hello how are you' 
# d = {} 
# for i in s: 
#     c = 0 
#     for j in s: 
#         if i == j: 
#             c+=1 
#         d[i] = c 
# print(d)       #{'h': 2, 'e': 2, 'l': 2, 'o': 3, ' ': 3, 'w': 1, 'a': 1, 'r': 1, 'y': 1, 'u': 1}

#------

#Q Given two lists of equal lengths create a dictionary where one list contains keys and the other contains values  

# l = [1,2,3,4,5,6] 
# l1 = [11,22,33,44,55,66] 
# d = {} 
# for i in range(len(l1)): 
#     d[l[i]] = l1[i] 
# print(d)     #{1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66} 

# l = [1,2,3,4,5,6] 
# l1 = [11,22,33,44,55,66]  
# d = {} 

# for i in range(len(l)): 
#     for j in range(len(l1)): 
#         d[l[i]] = l1[i]  #1:11, 2:22
# print(d)             #{1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66} 

#---

#Q Swap keys and values of a dictionary store keys in a list 

# d = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66} 
# d1 = {}

# for i,j in d.items(): 
#     d1[j] = i
#     # 66:6  
# print(d)     #{1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66} 

# #----single line answer 


# d = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66} 
# d1 = {v:k for k,v in d.items()}   #k-keys,v=values 
# print(d)   #{1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66}

# #  --same  


# d = {1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66} 
# d1 = {}
# k = [] 
# v = [] 

# for i in d.keys(): 
#     k.append(i) 
# for j in d.values(): 
#     v.append(i) 
# for k1 in range(len(k)): 
#     d1[v[k1]] = k[k1] 
# print(d)    #{1: 11, 2: 22, 3: 33, 4: 44, 5: 55, 6: 66} 


#----------------07-11-2025----------------------

# s = 'hello how are you'

# l = []
# s1 = ''  # empty string
# for i in s:
#     if i == ' ':
#         l.append(s1)
#         s1 = ''  # reset s1 after appending  # again i amdoing s1 empty here 
#     else:
#         s1 = s1 + i

# # append the last word (after loop)
# l.append(s1)

# print(l)


# b=0 
# for i in l: 
#     c = 0 
#     for j in i: 
#         c = c + 1 
#     if b < c: 
#         b = c 
# print(b)            

# for i in l:  #max element      
#     if b == len(i): 
#         print(i) 


# # -----

# s = 'bahubali' 
# s1 = 'uba' 
# if s1 in s : 
#     print(s.index(s1)) 
# else: 
#     print('not a sub string')    

#q Given a dictionary find the keyy  with the Highest value  

# d = {'a':10,'b':12,'c':45,'d':18,'e': 7} 
# b = 0 
# s='' 
# for i in d: 
#     if b<d[i]:  
#         b=d[i] 
#         s=i  
# print(s)           

#Q Given a list of numbers return a dictionary of elements that appear more than once along with their counts  

l = [1,1,2,1,3,2,3,4,5,6,0,0,0,0,0] 
d = {} 
for i in l: 
    c = 0 
    for j in l: 
        if i == j: 
            c = c + 1 
        if c > 1:   # count one time kante yekkuva unte add chey  
            d[i] = c  

print(d)               #{1: 3, 2: 2, 3: 2, 0: 5}

d = {'a': 34,'b':90,'c': 45,'d': 8}
d1 = {'c':93,'d':5,'e':10,'f': 23} 

for i in d.keys(): 
    if i in d1.keys(): 
        d1[i] = d[i] + d1[i]   #'same keys unte add it both' in dict-  if it have diff key just normal add to dict 
        #
    else: 
        d1[i] = d[i] 
print(d1)            #{'c': 138, 'd': 13, 'e': 10, 'f': 23, 'a': 34, 'b': 90}