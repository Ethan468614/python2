from tkinter import *
from datetime import date

root = Tk()
root.title("Widgets")
root.geometry('400x300')


lbl = Label(root, text="What is up", fg = "white", bg = "#F60606", height= 1, width = 300)


name_lbl = Label(root, text="Full name", bg = "#0C4FED")
name_entry = Entry()

def display():
    
    name = name_entry.get()
    

    global Message 
    Message = "Welcome To the app! \n todays date is"
    greet = "Hello " + name + "\n"

    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text= "Begin", command=display, height=1, bg = "#17F20C", fg = "white")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()