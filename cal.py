from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination calculator")
root.configure(bg="lightblue")
root.geometry("650x400")

upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)


label = Label(root, image=image, bg="lightblue")
label.place(x=180, y=20)

label1 = Label(root, text="hello Welcome to the denomination calculator", bg="lightblue")
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msg_box = messagebox.showinfo("Alert!", "Do you want to calculate the denomination count?")

    if Msg_box == "ok":
        topwin()


button1 = Button(root, text="Let's start", command=msg, bg = "brown", fg = "white")         

button1.place(x=260, y=360)