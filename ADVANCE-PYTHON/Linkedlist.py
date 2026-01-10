#-------------------------------LINKED LIST------------------------

# Data we have continous we know how to read  
# Data will have fragmented way we dont know the issue  in which fragment we have to read  

# Head --> in head will have 'next node address' 
# we cannot use indexing on linked list  

# we can only travels(move) in one way  traffic will moves in one direction in linkedlist  

# ------------------------Double Linkedlist ---------------------- 
# Double linkedlist --> will have 'previous node address' and 'data' and 'next node aderess' also 

# ---linkedlist (custom class node) writng 

class Node: 
    def __init__(self,data): 
        self.data=data 
        self.next=None  


n1 = Node(5)        
n2 = Node(-4)

n1.next=n2 
n3=Node(10) 
n2.next=n3  

# head is nothing but'n1' 
head = Node(5) 
n2 = Node(-4) 
head.next=n2 
n3= Node(10) 
n2.next=n3 

print(n1) 

def print_ll(head): 
    if head == None: 
        return 
    temp = head 
    while temp != None: 
        print(temp.data) 
        temp=temp.next 
print_ll(head)        

#o/ps 

#5 
# -4
# 10 
 
# INSERT a Node at the FIRST (already i have linkedlist) 

def add_node_start(head, new_node_data): 
    new_node = Node(new_node_data) 
    new_node.next = head 
    head = new_node 
    return head 
head = add_node_start(head,25) 
print_ll(head)

# o/ps
# 25
# 5
# -4
# 10 

# INSERT a NODE at last (node will add actually in last) 

def add_node_last(head, new_node_data): 
    if head == None:  # edge case if head = none is there then add new node to head and return the head only 
        new_node = Node(new_node_data) 
        head = new_node 
        return head 
     
    temp = head  
    while temp.next != None: 
        temp = temp.next 

    new_node = Node(new_node_data)
    temp.next = new_node 
    return head  

head2 = add_node_last(head,60)
print_ll(head)

#o/ps
# 25
# 5
# -4
# 10
# 60 

# How to delete a 2nd element data 

# def delete(head,del_data): 
#     temp = head 
#     prev = None 
#     while temp != None: 
#         if temp.data == del_data: 
#             prev.next == temp.next 
#         prev = temp 
#         temp = temp.next 

def delete(head,del_data): 
    if head == None: 
        return 

    if head.data == del_data: 
        head  = head.next 
        return 
    temp = head 
    prev = None 
    while temp != None : 
        if temp.data == del_data: 
            prev.next = temp.next 
    prev = temp 
    temp = temp.next 
    return head 
res = delete(head,-4)
print_ll(res)
            

# def delete(head, del_data):
#     # If list is empty
#     if head is None:
#         return head

#     # If head node itself holds the data
#     if head.data == del_data:
#         return head.next

#     temp = head
#     prev = None

#     while temp is not None:
#         if temp.data == del_data:
#             prev.next = temp.next
#             return head
#         prev = temp
#         temp = temp.next

#     return head
