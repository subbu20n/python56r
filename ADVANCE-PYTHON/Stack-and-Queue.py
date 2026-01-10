# -------------------------STACK----AND----QUEUE------------------------------- 

# ---------------------------STACK--------------------------------------

#LIFO ---> last in first out  
#FIFO --> first in first out  

# when we 'add elements' it has add to 'last in list '  
 
#---push---pop-----peak() -------------- size-----is_empty()---------

# peak --> peak will see last element in stack  
# pop  --> it will delete last element in stack 
# Push --> it will add in list last  

# already i have a list but i want to implent a stack datastructure  --> in list i havw wanted features and unwanted features also 
# in stack --> we need to insert the element in last -not possible insert in first ok 
# by mistakely you entered a append in the place of you have insert an element then it throw a error  

# so for taht purpose we add around the list soome additional features  
# i will use this list and i will write the stack then i pick what i want the elements remaining wont work  

# we need to decide before writing the function either 'LIFO or FIFO' 
#-----LIFO 
# class Stack: 
#     def __init__(self): 
#         self.inner_list = [] 
#         print('stack is created') 

#     def push(self,elem): 
#         self.inner_list.append(elem) 
#     def size(self): 
#         return len(self.inner_list) 
#     def is_empty(self): 
#         return len(self.inner_list) == 0 
#     def peek(self): 
#         if self.is_empty():     # we decide for this LIFO 
#             raise Exception('No elements in the satck')
#         return self.inner_list[len(self.inner_list)-1]  
#     def pop(self): 
#         if self.is_empty(): 
#             raise Exception('No elements in the stack') 
#         return self.inner_list.pop() 
# s1 = Stack() 
# # s1.insert(5) # satck lo insert mthod not here 
# s1.push(5)
# s1.push('5')
# s1.push('No eleements in the stack') 
# s1.push('555') 
# print(s1.peek()) # peek will show last element in stack 
# s1.push('432')
# s1.push(0)
# print(s1.size()) # size will tell 
# print(s1.is_empty()) # is_ empty it have empty it return true ok 
# print(s1.pop()) # pop() it deletes all 
# print(s1.size()) 


# print(s1.pop()) 
# print(s1.pop()) 
# print(s1.pop()) 
# print(s1.pop()) 
# print(s1.pop()) 
# print(s1.pop()) # here we exceded the stack in emeenets  #     raise Exception('No elements in the stack')
                    #    Exception: No elements in the stack  


#-------------------------------QUEUE--------------------------- 
# in DEVOPS MQDATABSES 'WHATSAPP EXAMPLE' 

#----FIFO--------First In First Out 

# in QUEUE who goes first they will come back to first only  
# whatsapp is there i send msg to another person there is a queue in b/w me and that person 
# if that person is not avaailabe in online - queue will store that msg - and that person comes to online forward that msg to person 

class Queue:
    def __init__(self):
        self.inner_list = []
        print('queue is created')

    def push(self, elem):   # enqueue
        self.inner_list.append(elem)

    def size(self):
        return len(self.inner_list)

    def is_empty(self):
        return len(self.inner_list) == 0

    def peek(self):
        if self.is_empty():
            raise Exception('No elements in the queue')
        return self.inner_list[0]   # FIRST element (FIFO)

    def pop(self):   # dequeue
        if self.is_empty():
            raise Exception('No elements in the queue')
        return self.inner_list.pop(0)   # remove FIRST element


q1 = Queue()
q1.push(5)
q1.push('5')
q1.push('No elements in the queue')
q1.push('555')

print(q1.peek())        # shows first element
q1.push('432')
q1.push(0)

print(q1.size())
print(q1.is_empty())

print(q1.pop())
print(q1.size())

print(q1.pop())
print(q1.pop())
print(q1.pop())
print(q1.pop())
print(q1.pop())


# -------------valid /BALANCED PARENTHESIS----------- 

# ({[ ]})  # these are balanaced parenthesis 

# opening bracket has to match the closing bracket also then it is a balanaced parenthesis  

# ({[ } --> it does not matched so its not a balanced parenthesis  

# ({[ ]}) # here matched then it removed from the stack matched ones 
  
#() ,[], {} --> these are the corresponding values has to match   

