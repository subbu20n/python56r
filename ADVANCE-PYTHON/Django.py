#----------------------------------DJANGO-------------

Introduction to Django and Web Application Architecture 

what is web application ? 
Web development is about building the websites or web applications  that users interact with throw a browser 
It usually involoves two main sides 
* Frontend(client isde) --> what the users sees(HTML,CSS,JAVASCRIPT) 
* Backend(Serverside)  --> Handles logic data storage and processing(python,Django,Nodejs etc) 

when both frontend and backend are handled using python, we call it python full stack developemnt 

frontend---> Backend--->Database 

#---------3-tier Architecture---------
1. presentation layer(Frontend(UI)) 

      what users sees interface and interact with 
       made with HTML,CSS,JAVASCRIPT 
      ex: BUTTONS,FORMS,TABLES ETC 
in Django this is actually handled by templates (HTML files) or through frontend frameworks(React,Angular,etc).counsuming APIs

2.APPLICATION LAYER(LOGIC LAYER) 

The heart of the application 
Handled logic, validations,request processing 
In Django , this includes  
    * views (business logic) 
    * models (data structures) 
    * Forms , serialisers and middleware  

3.Data layer  

Responsible for interacting with the database  
Django provides ORM(object-Relation mapper)- we write python code instead of sql queries  
supported databases: sql lite, mysql, postgresql, oracle etc 

# APIs-- bridge b/w systems 

API--> Application programming interface is a communication link between two software systems  

It defines how one system can talk to another using structured reequests and responses  

for ex: 
    your frontend react app calls Django API --> Django fetched data from the database --> sends back a json response  

#  Request Response mondel 

      1. client sends request (browser,postman,frontend app) 
      2. server receives request 
      3. server validates & process data 
      4. server fetches data (from DB or logic) 
      5. server sends response (Json, HTML, etc) 
All this communi cation is handled by APIs. 