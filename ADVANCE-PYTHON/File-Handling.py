# --------------------------FILE HANDLING---------------

# FILE HANDLING: Allows us to read CRUD operations 
 
# 1 . file = open('file_path', 'mode') 
# 2 . read  ==> read.Error if file does not exist 
# 3 . write ==> creates file if file not exists 
# 4 . a(append) ==> creates file if not exists 
# 5 . x(create) ==> error if already exists 
# 6 . b(binary mode) 
# 7 . t(text mode - default) 
# 8 . r+, w+, a+  

# Reading a file 

# f.read() # it comes in string format 
# f.read(10) 
# f.readline() # it comes like 'string' format (cursor it reads where cursor is the and end of the line )
# f.readlines()  # it comes like 'list'
# f.close()  # file it closes the file   

# f.read(5) 
# f.tell() # it tells us in which cursor is have  
# f.seek() # it goes back to in which line u want you can mention ok 
# f.read(5) 

# ----------------------READ-------------------------

# f = open('subbu.py', 'r') 
# print(f.read()) 
# print(type(f.read())) 
# print(f.read(10))   

# f = open('subbu.py','r') 
# print(f.read(20)) # here read 20 characters and then down side reads where 'cursor is there there to will print   
# print(f.read(20)) 
# print(f.readline()) # it reads where our cursor is there from there to end of the line  

# print(f.readline()) 
# print(f.readlines()) # it reads all lines of the file 


# f = open('subbu.py', 'r') 
# print(f.read(20)) # it reads 20 characters  
# print(f.tell()) # it tells where cursor have  
# print(f.read(20)) 


# f = open('subbu.py', 'r') 
# print(f.read(20)) 
# print(f.tell()) 
# print(f.seek(0)) 
# print(f.read(20))  


# f = open('arun.py','r')  # leni file ni read cheyalani chooste error vastundi 
# print(f.read(20))   


# f = open('absolutepath','r') 
# print(f.read(10))
 
# f = open('absolutepath','r')   #'\n' means it comes in new line  
# print(f.read(10))

# f = open(r'absolutepath', 'r') # dont check escapes '\' give 'r=rostring'  it skips 
# print(f.read(20))

# -------------WRITE--------------------- 

# f = open('subbu.py', 'w')  # it remove the content in that file it adds 'hi' 
# print(f.write('hi'))   # if wont have this 'subbu.py'  file it creates and and write the 'hi' 

# f = open('subbu.py','w')
# print(f.write('hi subbu'))


# f = open('subbu.py','w') 
# print(f.write('hi')) 
# print(f.write('hi')) # it adds besides 'hihi' like this 
# print(f.write('hi\n')) # '\n'  comes in new line  
# print(f.write('hi\t'))  # '\t'  comes space _ 

# -----WRITE MODE ----- 

# f.write('Hello \n') 
# f.writelines(['A \n' , 'B \n']) 


# with open('example.txt','r') 
#   print(f.read()) 
# you can iterate this file using loop for each line 

# with open('image.png','rb') as f:   'rb'- read-binary 
#   data = f.read() 

# with open('copy.png','wb') as f:   'wb- write binary' 
#    f.write(data) 

# APPEND- WHEN WE APPEND CURSOR WILL BE LAST IN FILE  
# WRITE - WHEN WE WRITE THE PREVIOUS CONTENT WILL REMOVE AND ADDS NEW ONE WHAT WE WROTE  
# READ - WHEN WE READ CURSOR WILL BE STARTING THE FILE   

# f  = open(r'subbu.py','x') # 'x' it creates the file 

# f = open('subbu.py','rt') 
# print(f.write('hi')) 

# f = open('subbu.py','a+')  # a+ = append to previous contnent  
# print(f.read(20))  # aada at te last of file and read the file cursor  

# # -------------------13-11-2025---------------- 

# f = open(r'subbu.py','r+') 
# f.write('hi\n')  # previous will remove and replace the data  
# print(f.read()) 

# f  = open(r'subbu.py','w+')
# f.write('Hi')  # previous one will remove 
# print(f.read(10))  # here empty untundi 

# ----now you can open file in 2-modes ----------------

# b(bibary mode) -- to read 'documents,images,pdfs' we use this binary mode we can do 'crud' operations also here   
# t(text mode default) it haves the by default text mode  we can do 'crud' operations also here  



# with open(r'c:\Users\HP\Downloads\kerala.jpg','rb') as file: 
#     data = file.read() 

# with open('copy.jpg','wb') as file: 
#     file.write(data)      


# ----------------- WORKING with "JSON" files -------------------- 

# import json , json dump(data,file), json.load(f) 

# json.dump() write directly to a file 
# json.dumps() - return a json string 
# json.load() - reads from file  
# json.loads() - reads from a string 

# json.dump --> with us we have 'content file' will take keep it in 'json format' 
# json.load --> we have already json content it returns for us 'dictionary format' 
# json.dump,json.load --> will do operations on files 

#in a file there is a content in json format 'we call it as 'json-file'

# actually it is used for frontend to backend communication '/api/  


import json 
# dict1 = {
#     "k1": "v1",
#     "k2": "v2",
#     "k3": "v3"
# }
# f = open('dict_json.json','w')  # here it did not have it cretaes and write inthat file 
# json.dump(dict1,f) 


# f = open('dict_json.json','r')  # we have already json content file 
# dict1 = json.load(f)  #'json.load' -- it gives in the 'dictonary format'
# print(type(dict1))  #{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'} 

# f = open('dict_json.json','r')
# dict1 = f.read() # here 'f.read()' -- it gives the in 'string format'
# print(type(dict1)) #<class 'str'>
 
# file.dumps(), file.loads()-- we cant use in file handling purpose we use in web developemnt purpose 

# json.dumps - returns a JSON string 
# json.loads() - reads from a string 

#"content ni string cheyali , string ni json/dictionary cheyali in that case we use "dumps(), loads()""

#'json.loads()' --> will use in 'Django" 

# ---------------------------OS MODULE-------------------------

# os.name ==> posix(LINUX/MAC) , 'nt' for(windows) 
# os.getlogin() 
# os.cpu_count() 

# # RUNNING METHODS 
# os.system('python --version') 
# os.system('python script.py') # it runs 'that file 'script.py' 

# # Current working directories 

# os.getcwd() 
# os.chdir('/path/to/folder') # change directory 
# os.listdir(path=".") 

# #Creating directories 
# os.mkdir(path) 
# os.makedirs(path) --> folder in a folder create  
# os.rmdir(path) -> Removes a single empty directory 
# os.removeddirs(path) --> Remove nested empty directory 
# os.rename(src,dest)  -->old name, new name 
# os.remove(path) --> deletes a file  

# # for an non empty directory 

# import shutil 
# shutil.rmtree("my_non_empty_folder") 

# # File Metadata 

# info = os.stat('file.txt') --> it comes an file metadata  
# #st_size = sy_mtime  

# from datetime import datetime 
# datetime.fromtimestamp(info.st_mtime) 


# #os.path,join(a,b)  
# os.path.exists(path) 
# os.path.isfile(path) 
# os.path.isdir(path) 
# os.path.dirname(path) 
# os.path.basename(path)  --> base name -filename 
# os.path.abspath(path)

import os 
print(os.name) 
print(os.getlogin) 
print(os.cpu_count)
os.system('python --version') 
os.system('python subbu.py')
print(os.getcwd) 
print(os.chdir()) 

print(os.listdir(path=".")) 
# os.mkdir("text-files") 
# os.makedirs('subbu/user-subbu') 
info=os.stat('copy.jpg') 
print(info)