from tkinter import *

window = Tk()
window.title("tesy")
window.geometry("400x300")

label = Label(window, text="In this program, we will ask the user for 2 numbers and return the product using python tkinter")
label.pack()
entry1 = Entry(window)
entry1.pack()
entry2 = Entry(window)
entry2.pack()
def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    product = num1 * num2
    result_label.config(text=f"The product is: {product}")
button = Button(window, text="Calculate Product", command=calculate_product)
button.pack()
result_label = Label(window, text="")
result_label.pack()
window.mainloop()
