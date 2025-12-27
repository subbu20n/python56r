#--------------------------------problem solving------------------------------------- 

#EDGE CASES ---> write if-else conditions  
#CODE-QUALITY --> wite always 'naming conventions' 
#Role of inbuilt functions --> not to write in interviews  
# Always use functions  


#------LISTS------------- 

list1 = [1,2,3,4,5,9,-32,-45] 
def find_elem(input_list,input_index): 
    if input_index < -len(input_list) or input_index >= len(input_list): 
         return 'Invalid index' 
    return input_list[input_index] 

index = int(input('Enter the input element')) 

print(find_elem(list1,index)) #list1 lo i enter 3 - in list1 3 rd index is -'4' 


#sum ,max, min --> find in list  max element 

list1 = [1,2,3,4,5,-32,-45] 

def max_elem(input_list): 
     if len(input_list) == 0: 
          return 'empty list' 
     input_list.sort() 
     return input_list[-1] 

max_elem = list1[0] 

for i in list1: 
     if i > max_elem:   #if you want minimum elemnet jus change the "i < max_elem" 
         max_elem = i  #reassigning 25 = 34 --> max_element = 34  --> it rotates like that  
print(max_elem) 

#25 
#34
#44
#56
#68
#76
#88
#90 
#91 

#  to find sum 
max_elem = list[0] 
#min_elem = list[0] #here it gets error 
sum = 0 

for i in list1: 
     sum += i 
     #to find max 
     if i > max_elem: 
          max_elem = i 

print(max_elem)