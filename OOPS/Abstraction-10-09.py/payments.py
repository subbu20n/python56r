from flask import Flask return jsonify 

from abc import ABC, abstractmethod 

app = Flask(__name__) 
#Abstract method payment classes (from your example) 

class Payment(ABC): 
    @abstractmethod 
    def authenticate(self): 
        pass 
    @abstractmethod 
    def pay(self,amount): 
        pass 
    def check(self): 
        print('just simple') 

class UPI(payment): 
    def authenticate(self): 
        print("upi Auth") 
    def pay(self,amount): 
        print(f"paid {amount} via credit upi") 

class CreditCard(payment): 
    def authenticate(self): 
        print("upi Auth") 
    def pay(self,amount): 
        print(f"paid {amount} via credit creditcard") 
class PayPal(payment): 
    def authenticate(self): 
        print("upi Auth") 
    def pay(self,amount): 
        print(f"paid {amount} via credit paypal")  

#class NetBanking(): 

#mapping from string -->class 
payment_classes = {
    "UPI"=UPI,
    "CreditCard"=CreditCard,
    "PayPal"=Paypal
}