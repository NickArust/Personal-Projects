import tkinter as tk

window = tk.Tk() #creates window

def increase():
    value = int(lbl_text["text"])
    lbl_text["text"] = f"{value + 1}"  #takes current value of the label and adds one to it

def decrease():
    value = int(lbl_text["text"])
    lbl_text["text"] = f"{value - 1}" #takes current value of the label and subtracts one from it

window.rowconfigure(0, weight = 1, minsize= 50)
window.columnconfigure([0,1,2], weight = 1, minsize = 50) #sets up the geometry of the space


down_button = tk.Button(master = window,text= "-", command= decrease)
up_button = tk.Button(master = window,text= "+", command= increase) # creates the buttons and label
lbl_text = tk.Label(master = window,text="0")
down_button.grid(row = 0, column = 0,sticky = "nsew")
lbl_text.grid(row = 0, column= 1) #instanciates it and puts in the right spot
up_button.grid(row = 0, column = 2,sticky = "nsew")

window.mainloop()