#---------------------------------------PANDAS-------------------------

# numerical operations we use 'numpy' 
# data analysis purpose we use 'pandas'

#   installation and basics 
# install 

pip install pandas

python data analytics library(pandas) 
built on numpy (pandas build on numpy )-numpy build on 'c' 


# About Pandas 

python data analytics library(pandas) 
built on numpy (pandas build on numpy )-numpy build on 'c' 

# Core Data Analysis
   1. series(1D ,Homogeneous)  # same type has to be 
   2. DATA FRAME(2D, Heterogeneous) # any string, int, .... 

#key Features 

Data cleaning (handle invalid/missing values) 
Data manipulation 
Data analysis 
Easy import/export from files & databases 

# ------------------core pandas objects-----------------
#--------2. SERIES(1D)------------------------

one dimesional labelled array 
Homogeneous 
pd.series([10,20,30],index=['a','b','c'])   # key value pair (dictionary) 

import pandas pd 
s1 = pd.seris([10,20,30]) 
print(s1) 
print(s1[10]) 

import pandas as pd 
s1 = pd.series([10,20,30], index=['a','b','c']) 
s1.marks='Marks' 
print(s1) 
print(s1[0]) 
print(s1.name) 
print(s1.values) 
print(s1.index) 
print(s1>20) 
print(s1[s1>20]) 

# -------------------1D-SERIES ----------------
# HOMOGENEOUS 
pd.series([10,20,30],index=['a','b','c']) 
df.values; df.index; df.type; 
df.index=gave list (you can also specify indexes later) 
first check df > 15 
conditional selection here  
df[df>15] 
df[(df>15) & (df<30)] 
~ for not operation 

data = {
    'name': ['alice','bob','charlie'] 
    'age': [25,30,35] 
}

# -----------------------DATA FRAME- 2D ------------------- 
data = {
    'name': ['alice','bob','charlie'] ,
    'age': [25,30,35] 
}

df.DataFrame(data, name='students') # optinal name atribute  
we will import the data from csv or excel sheet - wont take from dictionary data  

# ----------------------3.IMPORT & EXPORT DATA -------------------------------

#--------------------- Read-------------------
pd.read_csv('file.csv') 

#---------------------write------------------ 
df.to_csv('out.csv',index=false) 

data = {
    'id': [1,2,3,10] ,
    'name': ['mahesh','subbu','arun','rahul'] 
}
df = pd.DataFrame(data)  # we are converting the data to dataframe  
print(df)    

# create one 'csv-file' write data in it and save the save the file ok keep it in or upload file in (vscode)

#  Read  

df = pd.read_csv('csvfilename') 
print(df) 

#  write 
df.to_csv 

# ------------------------Data Exploration -------------------------
we will do basic operation on dataframes 
 
#             df.head() 
#             df.tail(3) 
#             df.info() 
#             df.shape #(rows,columns)
#             df.subscribe()   #summary statistics 
#             df.dftypes 
#             df.columns 
#             df.indexes        # row labels 
#             df.values         #underlying numpy array 


df = pd.read_csv('csv.filename') 
print(df.head()) 
print(df.tail(3))
print(df.info()) 
print(df.describe()) 
print(df.columns())
print(df.values) 
print(df.dftypes) 
print(df.index) 
print(df.values) 

#----------------5.Indexing , Selection and Slicing---------------------------

#     ------column selection-------
# df['col'] 
# df[['col1','col2']]  

df = pd.read_csv('csv.filename') 
print((df['Name'])) 

print(df[['Name','Age']]) 
print(type(df[['Name','Age']]))  # dataframe type  

# ---------------Row  and cell selection ----------------------
df.loc[2,'Name'] 
df.loc[1:3,['Age','Department']]   # label-based-inclusive  

# -----------------position-based selection -----------------

df.loc[0,1]  # row - number 
df.loc[0:3]   # column - name 

df = pd.read_csv('csv_filename') 
print(df.loc[2,'Age']) 
print(df.loc[2,['Age','cabin']]) 
print(df.loc[2:10,['Age','cabin']]) 
print(df.loc[2;10,[1,2]])  # loc -- numbering undali ( we get here 10 also)
print(df.iloc[2;10,[1,2]])  # iloc - name undali  (we get here upto '9' only) 


# ------------condition seletion-----------

df[df > 15] # it works here 'series'  # eleemmnt wise condition 
df[(df>15) & [df < 30]]  
df[df['age'] > 30]  # works here 'DATAFRAME' 
df.query('age'> 30) 
~ df['age'] > 30 #NOT 

# NOTE: 
loc - slicing is inclusive (stop value included)
iloc- is exclusive 

df = pd.read_csv('csv_filename')
print(df['AGE']>30) 
print(df[df['Age']>30]) 
print(df[df['Age']>30]['Name']) 
print(df[~(df['Age']>30)]) 

#----------------6.Manipulating columns-------------------
# New column
df['new'] = df['age'] + 10 

# Modify Existng column 
df['Age'] = df['age'] = 10 # broadcasting 

# Drop column/ Row 
df.drop('col',axis=1) 

# meaning of axis 
axis=0 --> operate down the rows (affects columns) 
axis =1 --. operate across columns (affects rows) 

df=pd.read-csv('csv-filename') 
df['current_age'] = df['Age'] + 25 # create new column 
df['Age'] = df['Age'] + 15 # modify 

# ----------------Rename columns ---------------syntax
df.rename(columns={'age':'weight'},inplace=True)

# ---------------sorting----------
df.sort_values('age',ascending=False) 

#-------02-01-2025----

# --------------7.Missing Values Handling------------------

#-------- Fill missing values --------syntax 
df.fillna(0) --> keep the zero 
df['age'].fillna(df['age'].mean(),inplace=True)
df.fillna(0),inplace=True  # when we keep 'inplace=true' changes reflects on original file  

df['age'].fillna(method='ffill') # ffill -forward fill 

# ------------drop Missing values--------------- 

df.dropna() 
# by default df.dropna(how='any') 
df.dropna(axis=1)   # drops columns with Nan 
df.dropna(how='all')    # drop only if all values in row  
are NaN   

# -----------Detects Missing Values ---------------
df.isnull.sum() 
df[df.isna().any(axis=1)] 
df[df.isnull().any(axis=1)] 
df[df.notna().all(axis=1)]  

pd.read_csv('csv_filename') 
print(df.isnull().sum()) 
print(df[df.isna().any(axis=1)])  

#-------------------Duplicates------------------ 
df.duplicated() 
df[df.duplicated(keep='first')]
df.drop_duplicates()   # best used reassignment  
df=df.drop_duplicates()  # duplicate all will delete  

df = pd.read-csv('csv_filename') 
print(df.duplicate())
print(df[df.duplicate()]) 
df1 = df.drop_duplicates() 
print(df.info()) 

#--------------------9.APPLY & REPLACE-----------------------

# -----------using apply-----
df['promoted-salary']=df['promoted_salary'].apply(
    lambda x:x / 10 if x> 60000 else x 
)  

# --------------Replace Values -------------------
df['name'].replace('cahrlie'.'Rose') 

# prefer reassignment unless using inplace =true 

#------------------------10. AGGREGIATIONS AND GROUP OPERATIONS ------------
#----------basic Aggregations -------------
df['age'].mean()  
df['age'].sum() 
df['dept'].value_counts() 
df['dept'].unique  

#----Group By---------
df.groupby('gender')['age'].mean()  #M,F  

#-------------11.STRING OPERATIONS ----------------

split column into multiple columns 
df[['f_name','l_name']] = df['name'].str.split('-',expand=True) 

#--------------12.Joins and Concatenations---------------
#---------CONCATENATE--------------

pd.concat([[df1,df2]]) 
pd.concat([df1,df2],axis=1)  

# in concatenate -we add and attach data to previous to simailar data 
# vertical stack -- in verical columns will be same  
# Horizontal stack --- in horizontal columns will not be the same  

#----------------MERGE/Join------------------
pd.merge(df1,df2, on='DEPT') 


#------------------13.-WHen to use 'inplace=True'-----------------
use inplace=True for operations that modify the dataframe directly such as 
df.rename(...)
df.drop(...)
df.fillna(.....)
df.repllace(....) 
df.sort_values(.....) 

Avoid inplace=True when: 
    you want to chain operators  
    you need original Dataframe preserved  


