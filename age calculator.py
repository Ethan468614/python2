import tkinter as tk
from tkinter import messagebox
from datetime import date

# 1. Initialize the Window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="#f0f0f0") # Light gray background

# Function to calculate age
def calculate_age():
    name = name_entry.get()
    try:
        birth_day = int(day_entry.get())
        birth_month = int(month_entry.get())
        birth_year = int(year_entry.get())
        
        today = date.today()
        age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
        
        # 5. Display personalized message
        result_label.config(text=f"Hello {name}!\nYou are {age} years old.", fg="#2c3e50")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for date, month, and year.")

# --- UI Layout using Grid Geometry Manager ---

# Title Label
title_label = tk.Label(root, text="Age Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Name Input
tk.Label(root, text="Name:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# Date Input
tk.Label(root, text="Day (DD):", bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5, sticky="e")
day_entry = tk.Entry(root)
day_entry.grid(row=2, column=1, padx=10, pady=5)

# Month Input
tk.Label(root, text="Month (MM):", bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="e")
month_entry = tk.Entry(root)
month_entry.grid(row=3, column=1, padx=10, pady=5)

# Year Input
tk.Label(root, text="Year (YYYY):", bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=5, sticky="e")
year_entry = tk.Entry(root)
year_entry.grid(row=4, column=1, padx=10, pady=5)

# Calculate Button
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
calc_button.grid(row=5, column=0, columnspan=2, pady=20)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#f0f0f0")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()