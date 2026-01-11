#-------------------------MATPLOTLIB-----------------------

# For graphs and visualisations of data analysis, reports and scientific posts 

import matplotlib.pyplot as plt  #matplotlib is package and pyplot is module 
x = [1,2,3,4] 
y = [2,4,6,8]
# gives you a line plot 
plt.plot(x,y) 
plt.show() 


import matplotlib.pyplot as plt 
x = [1,2,3,4] 
y = [2*i + 3 for i in x]  #2*1+3 = 5 
# [5,7,9,11,13] 
plt.plot(x,y)
plt.show() 

import matplotlib.pyplot as plt 
x = [1,2,3,4,5] 
y = [-5,8,9,0,3] 
z = [-3,5,6,7,8] 
plt.plot(x,y, color='red',marker='o', linestyle=":") 
plt.plot(x,z) 
plt.title('linerar serach') 
plt.plot(x,z) 
plt.show() 

#plt.plot(x,y color='red' , linestyle='--', marker='o') 
#color==> red,purple,yellow,#ff5788 

# ------------MARKER------ 
       'o' - circle 
       's' - square 
       '^' - triangle up 
       'v' - triangle down 
       '*' - star 
       '+' - plus 
       'x' - cross 
       'id'- diamond 
       'p' - pentagon 

#linestyles ==> '-' solid (by default it haves) 
#           ==> '--' dashed 
#           ==> '-.' dashdot  
#           ==> ':' dotted 

# -------shortcut----------------- 
plt.plot(x,y, 'ro--') # red color, o-circle marker and -- dashed line 


# Multiply plots on same graph 
#-----------------------------------
plot(x,y1) 
plot(x,y2) 
show()

plt.plot(x, np.sin(x), label='sine') 
plt.plot(x, np.cos(x), label='cosine') 
plt.legend(loc='upper right') 

import matplotlib.pyplot as plt 
import numpy as np 
x_values = np.linspace(1,10,100) 
y_values = np.sin(x_values) 
z_values = np.cos(x_values)  

plt.plot(x_values,y_values,z_values, label='x is 10cm') 
plt.legend(loc='upper right') 
plt.title('linear search') 
plt.xlabel('No of items') 
plt.ylabel('Total cost') 
plt.show()


import matplotlib.pyplot as plt 
import numpy as np 
x_values = np.linspace(-5, 5, 100) 
y_values = [i**2 +5*i +3 for i in x_values] 
plt.plot(x_values,y_values) 
plt.show() 

# -------------------BAR---,SCATTER---,PIE------------------

.bar(x,y,color='green') 
.scatter(x,y) 

pie ==> see how it works  

sizes = [25,30,20,25] 
sectors = ['A','B','C','D'] 

plt.pie(x=sizes,labels=sectors, start angle=90) 
plt.show() 
autopct='%1.1f%%' # after . only one digit will allows in float 1.1
#plt.figure(figsize=(8,5))
plt.savefig('myplot.png') # graph will save 


import matplotlib.pyplot as plt 
import numpy as np 
x_values = np.linspace(-55,5,10) 
y_values = [i**2+5*i+3 for i in x_values] 
z_values = [i**3+5*i +3 for i in y_values]

plt.scatter(x_values,y_values, label='x is 10 cm') 
plt.scatter(x_values, y_vlues, label='x is 15cm') 
plt.legend(loc='upper left') 
plt.show() 

#------------------------BARgarph------------------
import matplotlib.pyplot as plt 
# Data for the bargraph 
categories = ['sachin','virat','r.p','dhoni'] 
values = [100,81,73,7] 
plt.bar(categories,values) 
plt.title('simple bar graph') 
plt.xlabel('categories') 
plt.ylabel('values') 
plt.show() 

# ------29-11-2025 --------------

# ---------------------subplot------------------ 

fig, axis=plt.subplots(1,2) 
fig is the conatiner 
axs --> array of 2 axes objects 
axs[0].plot(x,y) 
axs[1].set-title('Linear') 
axs[1].bar(x,y2) 
axs[1].set.title('quadrantic') 

# how to apply, x-axis, y-axis, title to each one of these see 

plt.show() 
fig, axs=plt.subplots(2,2, figsize(8,6)) 
axs[0,0].plot(x,y) 
axs[0][0].set_title('Line') 

#-----Adjusts-------------

plt.tight_layout() 
plt.grid(visible=True, linestyle='--',alpha=0.6)

plt.style.use('seaborn-v0-8-darkgrid') 
['classic','ggplot','solarize_light2','seaborn-vo-8-paper','dark_background','fast','bmh','grayscale'] 

plt.text(3,10 'This point is important',fontsize=10, color='red') 
plt.annotate('peak', xy=(5,25),xytest=(3,20),arrowprops=dict(facecolor='black') arrowstyle='->')


#----------------------------PIECHART--------------

import matplotlib.pyplot as plt 
# in y should have percentage of students in each class 
x_labels =['class 1','class 2','class 3','class 4', 'class 5'] 

values=[40,10,30,12,8] 
plt.pie(x=values, labels=x_labels, autopct='%1.1f%%') #30.0 allows autopct -30.02 means not alllowed  
plt.savfig('my_plot.png') 
plt.show() 

# -------------------------subplot-------------------

import matplotlib.pyplot as plt 
x= [1,2,3,4,5] 
y = [6,7,8,9,10]
labels =['class 1','class 2','class 3','class 4', 'class 5'] 

values=[40,10,30,12,8] 
fig,axis=plt.subplots(1,2) 
axis[0].plot(x,y) 
axis[1].bar(labels,x) 
plt.show() 


import matplotlib.pyplot as plt 
x= [1,2,3,4,5] 
y = [6,7,8,9,10]
labels =['class 1','class 2','class 3','class 4', 'class 5'] 

 
fig,axis=plt.subplots(2,2, figuresize=(10,10))  
axis[0][0].plot(x,y) 
axis[0][0].set_title['first graph']
axis[0][1].plot(x,y) 
axis[0][1].set_title['second graph']
axis[1][0].bar(labels,x) 
axis[1][0].set_title['third graph']
axis[1][1].scatter(labels,x) 
axis[1][1].set_title['fourth graph']
plt.show() 


#----------------GRID----------------------
x = [1,2,3,4,5]
y = [6,7,8,9,10] 
plt.plot(x,y) 
plt.grid(visible=True, linestyle='-',alpha=0) 
plt.show() 

# ------------styles----------------

plt.style.use('dark-background') 
x = [1,2,3,4,5]
y = [6,7,8,9,10] 
plt.plot(x,y) 
plt.grid(visible=True, linestyle='-',alpha=0) 
plt.show() 

# ---------------------TEXT------------------------
x = [1,2,3,4,5]
y = [6,7,8,9,10] 
plt.plot(x,y) 
plt.grid(visible=True, linestyle='-',alpha=0) 
plt.text(3,8, 'Mid point') 
plt.show() 

#----------------------Annotate--------------------

x = [1,2,3,4,5]
y = [6,7,8,9,10] 
plt.plot(x,y) 
plt.grid(visible=True, linestyle='-',alpha=0) 
plt.annotate('Midpoint', xy=(3,8),xytext=(5,8),arrowprops=dict()) 
plt.show() 

# ------------date time module ---------
# i will send pdf learn by that its very easy 
# in this also most important topic is 'time data' we use this in Django 
