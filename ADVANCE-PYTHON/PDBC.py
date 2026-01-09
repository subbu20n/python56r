# -----------------------------PDBC--------------------------- 

# python has to connect database  
# after connecting to database then 'query' and execute  

# we know to insert delete update  the data  in tables  

#  --------INSTALL PYTHON CONNECTOR FOR MYSQL -----

# >>> pip install mysql-connector-python   #module  

# Database connection 

# import mysql.connector

# conn = mysql.connector.connect(
#     host = "locallost", 
#     user = "root", 
#     password = "your_password" 
#     database  = "56r"  #database name   
# )

# cursor.conn.cursor() 
# cursor.execute()  
 
# cursor -- will help to execute queries 

# keyword/Method              Meaning 
#------------------------------------------------------------------------
# connect()           establish connection with the mysql database  
# cursor()            creates a object to execute sql queries 
# execute()           runs a sql query (INSERT,UPDATE,SELECT) 
# fetchone()          fetches the next singleline row of result set  
# fetchall()          fetch all remaining  rows of result set  
# commit()            save changes permanently  to the database  
# roll back()         cancels uncommit changes  
# close()             close the cursor or connection  


#python -m pip install mysql-connector-python

# import mysql.connector   
# conn = mysql.connector.connect(
#     host = 'localhost', 
#     user = 'root' ,
#     password = 'Subbu@2003' ,
#     database = '56r' ,
#     port  = "3306" ,
#     autocommit = False
# )    
# print(conn.is_connected())

# cur = conn.cursor() 
# cur.execute('SHOW TABLES') 
# # #cur.execute('select * from emp')
# # cur.fetchall() 
# # cur.fetchone()
# # conn.close() 

# for i in cur.fetchall(): 
#     print(i)


# cur.execute(''' 
#         INSERT INTO ceo (regno,name) 
#          values (4,'subbu')  # inserting statically inputs values 
            
# ''' )
# conn.commit() 
# # print(cur.fetchall())  
# conn.close()

# create Database Table  
# ------------------------- 

# cursor.execute("create database if not exists my_database") 
# create_table = """
# CREATE TABLE IF NOT EXISTS students1(
#         id int Auto_increment PRIMARY KEY,  
#         name varchar(100), 
#         email varchar(100) unique, 
#         course varchar(100), 
#         joined_date DATE 

# )
# """

# cursor.execute(create_table)


# INSERT RECORDS 
#----------------

# single record 

# Query = """ INSERT INTO STUDENTS(name,email,course,joined_date)values(%s,%s,%s,%s)"""
# cursor.execute(query,('subbu','subbu@gmail.com','ifs','2025-03-28'))
# conn.commit() 

#        INSERT INTO ceo (regno,name) 
#          values (%s,%s)
            
# ''',(5,'sriya'))  # we can pass dynamically   

import mysql.connector   
conn = mysql.connector.connect(
    host = 'localhost', 
    user = 'root' ,
    password = 'Subbu@2003' ,
    database = '56r' ,
    port  = "3306" ,
    autocommit = False
)    
print(conn.is_connected())

cur = conn.cursor() 
cur.execute('SHOW TABLES') 
# #cur.execute('select * from emp')
# cur.fetchall() 
# cur.fetchone()
# conn.close() 

for i in cur.fetchall(): 
    print(i)

# (%s,%s) #parameterize queries will do 
cur.execute(''' 
        INSERT INTO ceo (regno,name) 
         values (%s,%s) #parameterize qur
            
''',(5,'sriya')) 
conn.commit() 
# print(cur.fetchall())  
conn.close() 

# id=25 
# name = 'pk' 
# INSERT INTO ceo VALUES(' +id+ ', ' +name)  # we can concatinate but always use 'parametrize queries'

#   ------------SQL INJECTION --------------------
# select from users 
# where username = ' ' and password = ' ' 
# 'select from users where username = +username+' and password=''+ ' '
# or '1' = '1'  # i will give wrong username  

# select * from users where username = '' OR '1' = '1' AND Password=' '  # qury satisfies alwasys here they can hack it or 1 = 1 right 
# so we have use always parameterize queries only ok 

# name=''
# if name =='subbu' or 1 ==1:  # here always executes and satisfies ok 
#     print('hi') 

#  Multiply Records 
# --------------------- 

# data = [ 
#     ('john','subbu@gmail.com','jfs','2025-02-03')
#     ('john','subbu@gmail.com','jfs','2025-02-03')
#     ('john','subbu@gmail.com','jfs','2025-02-03')
# ]
# cursor.execute(query,data) 
# conn.commit()

# Read/Fetch Records 
#--------------------------- 
# fetch all 
# cursor.execute('select * from students') 
# for row in cursor.fetchall(): 
#     print(row)

# Fetch Limited
#---------------
# cursor.execute('select * from students limit2') 
# print(cursor.fetchall()) 

#Fetch ordered
# ------------------
# cursor.execute('select * from students ordered by name ASC') 
# print(cur.fetchall()) 

# Fetch spefic columns 
#-------------------------- 
# cursor.execute('select name,course from students') 
# for row in cursor.fetchall(): 
#     print(row) 

# Fetch with condition  
#---------------------------- 
# cursor.execute('select * from students where course=%S, ('os')') 
# for row in cursor.fetchall(): 
#     print(row)

# update records in(U in CRUD)
# ---------------------------------- 
# update a students course by Email 

# update_query = 'UPDATE' students set course=%s where email=%s" 
# cursor.execute(update_query,('datascience',subbu@gmail.com)) 
# conn.commit() 


# update multiple columns 
#-----------------------------
# update_query = """ update students 
#         set name = %s, course= %s where id =%s
# """

# cursor.excute(update_query,('nandu','devops')) 
# conn.commits()

#Update based on condition 
# -------------------------------

# cursor.execute('update students set course=%s where course=%s',('devops','datascience')) 
# conn.commit() 

# Delete records (D in CRUD) 
#---------------------------------
# delete by id 

# cursor.execute('delete from students where id = %s,(3)')
# conn.commit() 

# delete by email 
# ----------------------
# cursor.execute('delete from students where email=%s',('john@gmail.com',)) 
# conn.commit()  

# Delete All records (Dangerous)
# ---------------------------------
# cursor.execute('TRUNCATE TABLE STUDENTS') 
# conn.commit() 

# Good Practices
# ------------------------- 
# 1 . Always use parameterized queries (%s) tp prevent sql injection 
# 2 . Always call conn.commits() after INSERT/UPDATE/DELETE 
# 3 . Always close connections 
#      a. cursor.close() 
#      b. conn.close()


try: 
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Subbu@2003',
        database = '56r',
        port = '3306',
        autocommit = False 
    )
    cur = conn.cursor() 
    cur.execute (''' 
                   
        INSERT INTO CEO (regno, name)
         values(%s,%s)  

    ''',(6,'arun'))  
except: 
    if conn and conn.is_connected(): 
        conn.rollback()  
else: 
    conn.commit() 
finally: 
    if conn and conn.is_connected(): 
        cur.close() 
        conn.close()             # we connect to databases and it will reflect all changes in databases automatically ok 


        