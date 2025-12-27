from flask import flask , request , jsonify 

from payments import payment_classes 
app= Flask(__name__) 

@aap.route("/pay",methods=["post"]) 
def pay():
    data=request.json 
    method= data.get("method") #UPI 
    amount=data.get("amount") 
#select the correct class 
PaymentClass=payment_classes.get("method") 
if not PaymentClass: 
    return jsonify {"msg": "Invalid payment method"} 

payment_obj = PaymentClass()
payment_obj.pay(amount) 
return jsonify ({"msg": f"paid {amount} using {method}"}) 