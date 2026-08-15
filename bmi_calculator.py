import tkinter as tk
from tkinter import messagebox


# =========================
# CALCULATE BMI
# =========================
def calculate_bmi():

    name = name_entry.get().strip()
    height_input = height_entry.get().strip()
    weight_input = weight_entry.get().strip()

    if name == "" or height_input == "" or weight_input == "":
        messagebox.showerror("Error", "Please enter all details.")
        return

    try:
        height_cm = float(height_input)
        weight_kg = float(weight_input)
    except ValueError:
        messagebox.showerror(
            "Error",
            "Height and Weight must be numbers."
        )
        return

    if height_cm <= 0 or weight_kg <= 0:
        messagebox.showerror(
            "Error",
            "Height and Weight must be greater than zero."
        )
        return

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)

    bmi = round(bmi, 2)

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        "================================\n"
        "          BMI RESULT\n"
        "================================\n\n"
        f"Name      : {name}\n"
        f"Height    : {height_cm} cm\n"
        f"Weight    : {weight_kg} kg\n\n"
        f"BMI       : {bmi:.2f}\n"
        f"Category  : {category}\n"
    )


# =========================
# CLEAR
# =========================
def clear_all():

    name_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

    result_box.delete("1.0", tk.END)

    result_box.insert(
        tk.END,
        "Enter your details\n"
        "and click Calculate BMI"
    )


# =========================
# MAIN WINDOW
# =========================
root = tk.Tk()

root.title("BMI Calculator")
root.geometry("500x650")
root.resizable(True, True)

root.configure(bg="#E8F4F2")


# =========================
# TITLE
# =========================
title = tk.Label(
    root,
    text="BMI CALCULATOR",
    font=("Arial", 24, "bold"),
    bg="#E8F4F2",
    fg="#355C5A"
)

title.pack(pady=25)


# =========================
# INPUT FRAME
# =========================
input_frame = tk.Frame(
    root,
    bg="white",
    padx=30,
    pady=25
)

input_frame.pack(
    padx=30,
    fill="x"
)


# =========================
# NAME
# =========================
tk.Label(
    input_frame,
    text="Name",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(anchor="w")

name_entry = tk.Entry(
    input_frame,
    font=("Arial", 13)
)

name_entry.pack(
    fill="x",
    pady=(5, 15),
    ipady=6
)


# =========================
# HEIGHT
# =========================
tk.Label(
    input_frame,
    text="Height (cm)",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(anchor="w")

height_entry = tk.Entry(
    input_frame,
    font=("Arial", 13)
)

height_entry.pack(
    fill="x",
    pady=(5, 15),
    ipady=6
)


# =========================
# WEIGHT
# =========================
tk.Label(
    input_frame,
    text="Weight (kg)",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(anchor="w")

weight_entry = tk.Entry(
    input_frame,
    font=("Arial", 13)
)

weight_entry.pack(
    fill="x",
    pady=(5, 20),
    ipady=6
)


# =========================
# BUTTON FRAME
# =========================
button_frame = tk.Frame(
    input_frame,
    bg="white"
)

button_frame.pack(fill="x")


# =========================
# CALCULATE BUTTON
# =========================
calculate_button = tk.Button(
    button_frame,
    text="CALCULATE BMI",
    font=("Arial", 11, "bold"),
    bg="#A8DADC",
    fg="#1D3557",
    command=calculate_bmi
)

calculate_button.pack(
    side="left",
    expand=True,
    fill="x",
    padx=(0, 5),
    ipady=10
)


# =========================
# CLEAR BUTTON
# =========================
clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 11, "bold"),
    bg="#F4C2C2",
    fg="#6D3131",
    command=clear_all
)

clear_button.pack(
    side="right",
    expand=True,
    fill="x",
    padx=(5, 0),
    ipady=10
)


# =========================
# RESULT FRAME
# =========================
result_frame = tk.Frame(
    root,
    bg="#F1FAEE",
    padx=20,
    pady=20
)

result_frame.pack(
    padx=30,
    pady=25,
    fill="both",
    expand=True
)


tk.Label(
    result_frame,
    text="RESULT",
    font=("Arial", 17, "bold"),
    bg="#F1FAEE",
    fg="#355C5A"
).pack(pady=(0, 10))


# =========================
# RESULT TEXT BOX
# ONLY SIZE CHANGED HERE
# =========================
result_box = tk.Text(
    result_frame,
    height=14,
    width=40,
    font=("Arial", 13),
    bg="#F1FAEE",
    fg="#354F52",
    bd=0,
    highlightthickness=0
)

result_box.pack(
    fill="both",
    expand=True
)


result_box.insert(
    tk.END,
    "Enter your details\n"
    "and click Calculate BMI"
)


# =========================
# START PROGRAM
# =========================
root.mainloop()
