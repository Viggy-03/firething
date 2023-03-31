import sub
import pyrebase
from tkinter import *

window = Tk()

window.geometry("500x500")
window.title("Waste Management")
window.resizable(False,False)





def main():
    
    frame = Frame(window, width = 500, height = 500,bg = "light green")
    frame.place(x=0,y=0)

    add_waste_type = Button(
        text = "Add Waste Type",
        width = 15,
        height = 4,
        command = add_waste_type_screen

    )
    add_waste_type.place(x=100,y=100)

    delete_waste_type = Button(
        text = "Delete Waste Type",
        width = 15,
        height = 4,
        command = del_waste_type_screen
        

    )
    delete_waste_type.place(x=100,y=300)



    add_waste_amt = Button(
        text = "Add Waste Amount",
        width = 15,
        height = 4,
        command = add_waste_amt_screen

    )
    add_waste_amt.place(x=300,y=100)

    delete_waste_amt = Button(
        text = "Delete Waste Amount",
        width = 17,
        height = 4,
        command= del_waste_amt_screen

    )
    delete_waste_amt.place(x=300,y=300)
    display_but = Button(
        text = "Display",
        width = 15,
        height = 4,
        command = display_screen

    )
    display_but.place(x=200,y=200)

    exit_button = Button(
        text ="Close",
        command = window.destroy,
        width = 15,
        height = 4,
        
    )
    exit_button.place(x=200,y=400)


def add_waste_type_screen():
     
    frame = Frame(window, width = 500, height = 500,bg = "light green")
    frame.place(x=0,y=0)

    label1 = Label(
        text = "Enter waste type:",
        bg = "light green"
    )
    label1.place(x=50, y=50)

    name_entry = Entry(frame, width= 50)
    name_entry.place(x=50,y=80)

    v = StringVar()
    values = {
        "Yes": "y",
        "No": "n"
    }
    count = 0
    for(text, value) in values.items():
        Radiobutton(frame, text = text, variable = v, value = value, bg = "light green").place(x=100,y=180+count)
        count+=30
    label2 = Label(
        text = "Is it recycleable",
        bg = "light green"
    )
    label2.place(x=50, y=140)
    
    back_but = Button(
        text = "Back",
        width = 15,
        height = 4,
        command = main

    )
    back_but.place(x=50,y=400)
    ok_but = Button(
        text = "OK",
        width = 15,
        height = 4,
        command = lambda: sub.add_type(name_entry.get(),v.get())

    )
    ok_but.place(x=350,y=400)

def add_waste_amt_screen():
    
    
    frame = Frame(window, width = 500, height = 500,bg = "light green")
    frame.place(x=0,y=0)

    back_but = Button(
        text = "Back",
        width = 15,
        height = 4,
        command = main

    )
    back_but.place(x=50,y=400)

    ok_but = Button(
        text = "OK",
        width = 15,
        height = 4,
        command = lambda: sub.add_amt(name_entry.get(), amt_entry.get())

    )
    ok_but.place(x=350,y=400)

    name_entry = Entry(frame, width= 50)
    name_entry.place(x=100,y=80)

    label1 = Label(
        text = "Select waste type: ",
        bg = "light green"
    )
    label1.place(x=50, y=50)
    
    amt_entry = Entry(frame, width= 50)
    amt_entry.place(x=100,y=230)

    label2 = Label(
        text = "Enter amount of waste:",
        bg = "light green"
    )
    label2.place(x=50, y=180)

def del_waste_amt_screen():
    
    
    frame = Frame(window, width = 500, height = 500,bg = "light green")
    frame.place(x=0,y=0)

    back_but = Button(
        text = "Back",
        width = 15,
        height = 4,
        command = main

    )
    back_but.place(x=50,y=400)

    
    
    name_entry = Entry(frame, width= 50)
    name_entry.place(x=100,y=80)
    

    label1 = Label(
        text = "Select waste type: ",
        bg = "light green"
    )
    label1.place(x=50, y=50)
    
    amt_entry = Entry(frame, width= 50)
    amt_entry.place(x=100,y=230)

    label2 = Label(
        text = "Enter amount of waste:",
        bg = "light green"
    )
    label2.place(x=50, y=180)

    ok_but = Button(
        text = "OK",
        width = 15,
        height = 4,
        command = lambda: sub.del_amt(name_entry.get(), amt_entry.get())

    )
    ok_but.place(x=350,y=400)


def del_waste_type_screen():
    
    frame = Frame(window, width = 500, height = 500,bg = "light green")
    frame.place(x=0,y=0)

    label1 = Label(
        text = "Enter waste type to be deleted:",
        bg = "light green"
    )
    label1.place(x=50, y=50)

    name_entry = Entry(frame, width= 50)
    name_entry.place(x=50,y=80)

    
   
    
    
    
    back_but = Button(
        text = "Back",
        width = 15,
        height = 4,
        command = main

    )
    back_but.place(x=50,y=400)
    ok_but = Button(
        text = "OK",
        width = 15,
        height = 4,
        command = lambda: sub.del_type(name_entry.get()))

    
    ok_but.place(x=350,y=400)

def display_screen():
    frame = Frame(window, width = 500, height = 500,bg = "light green")
    frame.place(x=0,y=0)

    back_but = Button(
        text = "Back",
        width = 15,
        height = 4,
        command = main

    )
    back_but.place(x=50,y=400)

    
    count = 30
    try:
        for x in sub.db.get():
            Label(text = "{} = {}".format(x.key(), x.val())).place(x=50,y=count+30)
            count+=30
    except:
        pass
    
    





    










main()


    









window.mainloop()