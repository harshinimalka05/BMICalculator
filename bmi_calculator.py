import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        if weight <= 0 or height_cm <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Weight and height must be greater than 0."
            )
            return

        height_m = height_cm / 100

        bmi = weight / (height_m * height_m)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter numeric values only."
        )

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("450x500")
root.configure(bg="#1E1E2F")
root.resizable(False, False)

title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E2F",
    fg="white"
)
title.pack(pady=20)

card = tk.Frame(root, bg="#2B2B3D")
card.pack(padx=30, pady=10, fill="both")

tk.Label(
    card,
    text="Weight (kg)",
    font=("Segoe UI", 12),
    bg="#2B2B3D",
    fg="white"
).pack(pady=(25, 5))

weight_entry = tk.Entry(
    card,
    font=("Segoe UI", 14),
    justify="center"
)
weight_entry.pack()

tk.Label(
    card,
    text="Height (cm)",
    font=("Segoe UI", 12),
    bg="#2B2B3D",
    fg="white"
).pack(pady=(20, 5))

height_entry = tk.Entry(
    card,
    font=("Segoe UI", 14),
    justify="center"
)
height_entry.pack()

tk.Button(
    card,
    text="Calculate BMI",
    font=("Segoe UI", 12, "bold"),
    bg="#4F46E5",
    fg="white",
    relief="flat",
    padx=15,
    pady=10,
    command=calculate_bmi
).pack(pady=25)

result_label = tk.Label(
    card,
    text="Enter your details",
    font=("Segoe UI", 16, "bold"),
    bg="#2B2B3D",
    fg="#00E676"
)
result_label.pack(pady=(10, 30))

root.mainloop()