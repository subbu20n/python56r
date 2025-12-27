#--------------------------------Binary Search----------------------------------
# Binary search : It works on only sorted data [ordered list]  [10,20,30,45,77,91,102] 
# Rndomly opened dictionary one page --> igot 'N-Page' but i need  'k-page' i can move back right (high-1) 
# Rndomly opened dictionary one page --> igot 'c-Page' but i need  'G-page' i can move back forward (low+1) 

# same reference --> i need in list1 '77' 

# len(list1)-1 // 2 --> 6%2 = 3 ==> index=3 0,1,2,3 '45' is mid value   here i didnt find my element  

#list1 = [10,20,30,45,77,91,102] 

# i will update the index of low  = mid+1 ==> 3 +1 = 4 

# low = mid+1   ==> low = 4 and high = 6 ==> 4+6 = 10 // 2 = 5 --> mid value '91' mid value 

# again i didnt find that my element so i "mid-1 = 4"  5-1=4 "77" ---> i found my element   

# list1 = [-3,-300,10,23,45,100,700].sort() # when we did sort means it returns new value becomes "none"
# print(list1)

list1 = [-3,-300,10,23,45,100,700] 
list1.sort()
print(list1) #[-300, -3, 10, 23, 45, 100, 700] 

search_element = -300 

low , high = 0 , len(list1) -1 
flag = True  

while low <= high: 
        
        mid = (low + high) // 2  #low = mid+1   ==> low = 4 and high = 6 ==> 4+6 = 10 // 2 = 5  (line14) 
        if list1[mid] == search_element: 
            print(mid, 'Element_found') 
            flag = False 
            break 

        elif list1[mid] > search_element:  
            high = mid - 1 
        else: 
            low = mid + 1 
if flag == True: 
    print('Not found')           