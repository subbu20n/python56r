#-------------------------ABSTRACTION CLASS AND ABSTARCT METHOD-------------------------------

#ABSTRACT METHOD--> a method does not have any implementation is called abstarct method  
#ABSTRACT CLASS --> class which 'abstract methods' are called Abstract method  

from abc import ABC, abstractmethod 


class ATM(ABC): 
    pass 
    
    @abstractmethod #decorator os using abstract method 
    def debit_money(self,amount): 
        pass 
#you cannot create an object for abstract classes  
    @abstractmethod 
    def credit_money(self,amount):   
        pass 

    def show_details(): 
        print('This atm details are ....') 

class SBI_ATM(ATM):
     
     def credit_money(self,amount): 
          return 'money is created' 
     def  debit_money(self,amount): 
          return 'money is debited'   
     
class HDFC_ATM(ATM): 
        def credit_money(self,amount): 
           return 'money is created' 
        def  debit_money(self,amount): 
           return 'money is debited'  
        
sbil = SBI_ATM() 
print(sbil)