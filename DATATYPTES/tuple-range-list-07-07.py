# --LIST---  (mutable) 

list1 = ['1','2','str',['1','3','4'],'44','4','3+2j'] 
print(list1)
print(len(list1)) 

print((list1[3][2]))  

print(list1[-3][-2]) #3 

print(list1[8:])  #slcing out of characters #[]-empty list 

print(list1[ : : -1]) #reverse order  

print(list1)

list1[2] = 'subbu' 
print(list1)  



#  ---TUPLE---    (Immutable) -reassignment posible  (heterogeneous) 

tuple1 = (1,2,3,4,'string',5) 
tuple1 = (5,6,7)  #--> reassignment  
print(tuple1)
#print(tuple1[4]) #index out of range 


#   ---RANGE---- 
print(range(0,10)) #here wont get values 
print(list(range(0,10)))  #we need to "convert to list" then we get the values ok 

print(list(range(10,0,-2))) #10,8,6,4,2 

print(list(range(1,51,2))) #first 25 odd numbers will print ok 


#---DICTONARY ---- (Mutable) 

dict = {
    'a': 'subbu',
    2: 'sai',  
    3: 'sai',
    3: 'hindu',   #latest one (downside) one will pick if u give 2 keys same) values you van give same 
    'a': 'hima',
    5: 'sai'  #values are accept same but keys wont accept  
}
print(dict)

dict[2] = 'charan' 
print(dict)
