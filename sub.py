import pyrebase


from tkinter import messagebox

config = {
    "apiKey": "AIzaSyAnMrfMYGc3CnP4ewvl7Xh9EZVQ5fYQoYk",
    "authDomain": "playingwithfire-e13b9.firebaseapp.com",
    "databaseURL":"https://playingwithfire-e13b9-default-rtdb.firebaseio.com/",
    "projectId": "playingwithfire-e13b9",
    "storageBucket": "playingwithfire-e13b9.appspot.com",
    "messagingSenderId": "534396764381",
    "appId": "1:534396764381:web:05ec7c8275ac7003ea1b34",
    "measurementId": "G-HGTC7962LB"
    
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
try:
    node_list = [x.key() for x in db.get()]
except:
    node_list = []

def add_type(name,bol):
    try:
        node_list = [x.key() for x in db.get()]
    except:
        node_list = []
    if name == "" or bol == "":
        pass
        
    else:
        
        
        
        if name in node_list:
            messagebox.showinfo("Waste Info","{} already exists".format(name))
        else:    
            data = {
                
                "recycle" : True if bol == "y" else False,
                "amount" : 0
            }
            db.child(name).set(data)
            messagebox.showinfo("Waste Info","{} created successfully".format(name))

    
    

def del_type(name):
    try:
        node_list = [x.key() for x in db.get()]
    except:
        node_list = []
    if name in node_list:
        db.child(name).remove()
        messagebox.showinfo("Waste Info","{} deleted".format(name))
    else:
        messagebox.showinfo("Waste Info","no such waste type")

    

def add_amt(name,amount):
    try:
        node_list = [x.key() for x in db.get()]
    except:
        node_list = []
    if name == "" or amount == "":
        pass
        
    else:
        amount= int(amount)
         
        
        if name in node_list:
            
            ini_amt = db.child(name).get().val()["amount"]
            db.child(name).update({"amount" : amount+ini_amt})
            messagebox.showinfo("Waste Info","{} amount of {} added".format(amount,name))
        else:
            pass

def del_amt(name, amount):
    try:
        node_list = [x.key() for x in db.get()] 
    except:
        node_list = []
    if name == "" or amount == "":
        pass
        
    else:
          
        pf = {
            True:"recycling", 
            False:"treating"
        }    
        if name in node_list:
            
            ini_amt = temp = db.child(name).get().val()["amount"]  
            amount = int(amount)
            if ini_amt>amount:

                db.child(name).update({"amount" : ini_amt-amount})
                vff = ini_amt-amount
                messagebox.showinfo("Waste Info","{} of {} sent for {}. {} left".format(amount , name, pf[db.child(name).get().val()["recycle"]], vff))
                
            elif ini_amt<amount:
                db.child(name).update({"amount" : 0})
                vff = 0
                messagebox.showinfo("Waste Info","{} of {} sent for {}. {} left".format(amount , name, pf[db.child(name).get().val()["recycle"]], vff))
            else:
                db.child(name).update({"amount" : 0})
                vff = 0
                messagebox.showinfo("Waste Info","{} of {} sent for {}. {} left".format(amount , name, pf[db.child(name).get().val()["recycle"]], vff))




 

