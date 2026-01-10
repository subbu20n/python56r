# -----------------------------TKinter--------------------------
# in python we use graphical interface  [GUI] 

# import tkinter as tk 

# root = tk.Tk 
# # root.mainloop() # what does this main.loop do? 
# # keeps the window open 
# # waits for button clicks,typing,resizing 
# # updates the UI continously 
# # without main.loop(), your window will open and close friendly 

# root.title('First App') 
# root.geometry('300x500')  # we can do size increasing  
# tk.label(root,text='Hello Tkinter',font=('Arial',16)).pack(pady=20) # for text and styles purpose we use this  


# # BUTTON 

# tk.button(root, text='click me', command=sayhello).pack() 

# # ENTRY 
# tk.Entry(root) 
# tk.Entry(root,show='*') 
# tk.Text() 
# var=tk.IntVar() # here we get from tkinter 'int value' 
# # .get and .set for values  
# tk.Checkbutton(root, text='I agree',variable=Var,command=sayhello)

# choice=tk.stringVar() 
# tk.Radiobutton(root, text='OPTION A',variable=var,value='A',command=sayhello).grid() # radiation button will select only one  

# listbox = tk.Listbox(root) 
# listbox.insert(1,'python') 
# listbox.insert(2,'java') 
# listbox.insert(3,'c++')
# listbox.pack() 

# # From Tkinter import messagebox 
# #----------------------------------------

# def show_msg(): 
#     messagebox.showinfo('INFO', "this is an info message") 
#     messagebox.showwarning('WARNING', "this is an warning message")
#     messagebox.showcritical('CRITICAL', "this is an critical message")

# grid(row=0, column=0, padX=10, padY=5) 

# # username password application ---> this is task for you 

# frame=tk.frame(root, bd=5, height=250, width=300, relief='solid') 
# frame.pack() 

# tk.label(frame, text='Inside frame').pack() 
# tk.Button(frame, text='click').pack() 

# pack,grid and place 
# tk.label(root,text='Hello',place=(x=50,y=100)) 

# #-----------GRID
# grid==>  column width ==> 


# from tkinter import filedialog 
# def open_file():
    #  file = filedialog,askopenfilename(title='select a file') 
    #  print("se;ect File:", file) 

#file_input = tk.Button(root, text='open file'  command=open_file).grid() 
# print(file_input) 
# root.mainloop() 

# import tkinter  as tk 
# def say_hello(): 
#     print('Button clicked') 
#     Messagebox.showinfo('INFO','This is info message') 
#     Messagebox.showwarning('warning','This is warning') 
#     Messagebox.showerror('Error','oops', 'something went wrong')

# def check_box_clicked(): 
#     print(var.get())    
#     if var.get() == 1: 
#         print('Thank you for accepting T & C without reading them') 
#     else: 
#         print('you can leave') 
# def check_box_clicked(): 
#     print(var.get(1))
#     if var.get()== 1: 
#         print('Thank you for accepting T & c without reading them') 
#     else: 
#         print('you can leave') 

# root=tk.Tk() 
# root.title('My First GUI') 
# root.geometry('500x500') 
# tk.Label(root,text='Hi from App', font=('Arial', 16)).pack(pady=50)
# tk.Button(root,text='click me', command=say_hello).pack() 

# tk.Entry(root).pack() 
# #tk.Text().pack() 

# var=tk.IntVar()
# tk.Checkbutton(root, text='I agree', variable=var, command=check_box_clicked)

# choice=tk.StringVar() 
# tk.Radiobutton(root, text="OPTION A", variable=choice, value='A', command=check_box_clicked).pack() 
# tk.Radiobutton(root, text="OPTION B", variable=choice, value='A', command=check_box_clicked).pack() 

# listbox=tk.Listbox(root) 
# listbox.insert('1','python')
# listbox.insert('2','java') 
# listbox.insert('3','c++') 
# listbox.pack() 

# frame= tk.Frame(root,bd=5, height=250, width=300, relief='solid') 
# frame.pack(row=3, column=0) 

# tk.Label(frame, text='Inside Frame').pack() 
# tk.Button(frame, text='click').pack() 
# root.mainloop() 

import tkinter as tk
from tkinter import messagebox

def say_hello():
    print('Button clicked')
    messagebox.showinfo('INFO', 'This is info message')
    messagebox.showwarning('Warning', 'This is warning')
    messagebox.showerror('Error', 'Something went wrong')

def check_box_clicked():
    print(var.get())
    if var.get() == 1:
        print('Thank you for accepting T & C without reading them')
    else:
        print('You can leave')

root = tk.Tk()
root.title('My First GUI')
root.geometry('500x500')

tk.Label(root, text='Hi from App', font=('Arial', 16)).grid(row=0,column=0)
tk.Label(root, text='Hi from App', font=('Arial', 16)).pack(pady=50)

tk.Button(root, text='Click Me', command=say_hello).grid(row=0,column=1)
tk.Button(root, text='Click Me', command=say_hello).pack()

tk.Entry(root).grid(row=1,column=0)
tk.Entry(root).pack()

var = tk.IntVar()
tk.Checkbutton(root, text='I agree', variable=var, command=check_box_clicked).grid(row=1,column=1)
tk.Checkbutton(root, text='I agree', variable=var, command=check_box_clicked).pack()

choice = tk.StringVar()
tk.Radiobutton(root, text="OPTION A", variable=choice, value='A').grid(row=2,column=0)
tk.Radiobutton(root, text="OPTION B", variable=choice, value='B').grid(row=2,column=1)
tk.Radiobutton(root, text="OPTION A", variable=choice, value='A').pack()
tk.Radiobutton(root, text="OPTION B", variable=choice, value='B').pack()

listbox = tk.Listbox(root)
listbox.insert(1, 'Python')
listbox.insert(2, 'Java')
listbox.insert(3, 'C++')
listbox.grid(row=2,column=2)
listbox.pack()

frame = tk.Frame(root, bd=5, height=250, width=300, relief='solid')
#frame.pack(pady=20)
frame.grid(row=3,column=0)

tk.Label(frame, text='Inside Frame').pack()
tk.Button(frame, text='Click').pack()

root.mainloop()
