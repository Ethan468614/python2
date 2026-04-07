import tkinter as tk
from tkinter import messagebox

# 1. Initialize the Window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")
root.configure(bg="#e8f8f5") # Light mint background

# Function to perform the conversion
def convert_inches_to_cm():
    try:
        inches = float(inches_entry.get())
        # Conversion formula: inches * 2.54
        centimeters = inches * 2.54
        # Update the result label
        result_label.config(text=f"{inches} inches = {centimeters:.2f} cm", fg="#117a65")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for inches.")

# --- UI Layout ---

# Title Label
title_label = tk.Label(root, text="Inches to Centimeters", font=("Arial", 16, "bold"), bg="#e8f8f5", fg="#16a085")
title_label.pack(pady=20)

# Instruction Label
instr_label = tk.Label(root, text="Enter length in inches:", bg="#e8f8f5", font=("Arial", 10))
instr_label.pack(pady=5)

# Entry Box for Inches
inches_entry = tk.Entry(root, font=("Arial", 12), justify="center")
inches_entry.pack(pady=10)

# Convert Button
# This is the 'Event' trigger
convert_button = tk.Button(root, text="Convert", command=convert_inches_to_cm, bg="#16a085", fg="white", font=("Arial", 10, "bold"), width=15)
convert_button.pack(pady=20)

# Result Display Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#e8f8f5")
result_label.pack(pady=10)

# Start the application
root.mainloop()