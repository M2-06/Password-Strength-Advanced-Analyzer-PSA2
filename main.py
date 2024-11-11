import tkinter as tk
from tkinter import ttk
from Sha256 import txtToSHA256
from Api import check_password_hash
from Score import evaluate_password_strength
import time

# Function for typing effect
def type_effect(label, text, delay=50):
    label.config(text="")
    for i in range(len(text)):
        label.config(text=label.cget("text") + text[i])
        label.update()
        time.sleep(delay / 1000)

# Function to handle password evaluation and display results
def analyze_password():
    password = password_entry.get()
    if not password:
        type_effect(score_label, "Enter a password to analyze.")
        return

    # Step 1: Evaluate password and get results
    score, passlen, consecutive, uplow, numbers, symbols, dbleak = evaluate_password_strength(password)
    
    # Step 2: Get SHA256 hash and check against database for exposures
    hashed_password = txtToSHA256(password)
    times_found = check_password_hash(hashed_password)
    
    # Display the results with typing animation , ( post analyze )
    type_effect(score_label, f"Password Score: {score}")
    passlen_label.config(text=f"Length: {passlen}")
    consecutive_label.config(text=f"Consecutive Characters: {consecutive}")
    uplow_label.config(text=f"Upper-Lower Mix: {uplow}")
    numbers_label.config(text=f"Numbers: {numbers}")
    symbols_label.config(text=f"Symbols: {symbols}")
    dbleak_label.config(text=f"Password Commonality: {dbleak}")
    db_check_label.config(text=f"Found {times_found} times in leaked passwords databases.")

# Hover effect functions for button
def on_enter(e):
    analyze_button.config(bg="darkgreen", fg="lime")

def on_leave(e):
    analyze_button.config(bg="black", fg="lime")

# Function to update wraplength based on window width
def update_wraplength(event):
    new_width = recommendations_frame.winfo_width() - 20
    passlen_label.config(wraplength=new_width)
    consecutive_label.config(wraplength=new_width)
    uplow_label.config(wraplength=new_width)
    numbers_label.config(wraplength=new_width)
    symbols_label.config(wraplength=new_width)
    dbleak_label.config(wraplength=new_width)

# Main Tkinter window setup
root = tk.Tk()
root.title("PSA2 - M²")
root.geometry("700x550")
root.configure(bg="black")

# Title Label with typing effect
title_label = tk.Label(root, text="", font=("Courier", 18, "bold"), fg="lime", bg="black")
title_label.pack(pady=10)
root.after(500, lambda: type_effect(title_label, "Password Strength Advanced Analyzer", delay=100))

# Input Section
input_frame = ttk.Frame(root)
input_frame.pack(pady=5)
input_frame.configure(style="Custom.TFrame")

password_label = tk.Label(input_frame, text="Enter Password:", font=("Courier", 10), fg="lime", bg="black")
password_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

password_entry = tk.Entry(input_frame, width=30, show="*", font=("Courier", 10), bg="black", fg="lime", insertbackground="lime")
password_entry.grid(row=0, column=1, padx=5, pady=5)

# Custom hacking-themed Analyze button
analyze_button = tk.Button(
    input_frame,
    text="Analyze",
    font=("Courier", 12, "bold"),
    bg="black",      # Black background for hacking theme
    fg="lime",       # Bright green text color
    activebackground="darkgreen",  # Dark green when clicked
    activeforeground="lime",       # Lime green text when clicked
    relief="ridge",  # Slight 3D effect
    borderwidth=3,   # Thicker border for emphasis
    command=analyze_password
)

# Bind hover effects to the button
analyze_button.bind("<Enter>", on_enter)
analyze_button.bind("<Leave>", on_leave)

# Position the button in the input frame
analyze_button.grid(row=0, column=2, padx=5, pady=5)

# Results Section with hacking-style labels
score_label = tk.Label(root, text="Password Score:", font=("Courier", 12, "bold"), fg="lime", bg="black")
score_label.pack(pady=(10, 5))

db_check_label = tk.Label(root, text="Found 0 times in leaked passwords databases.", font=("Courier", 12), fg="lime", bg="black")
db_check_label.pack(pady=(0, 10))

# Frame for Recommendations with hacking theme
recommendations_frame = tk.LabelFrame(root, text="Recommendations", font=("Courier", 12), fg="lime", bg="black", bd=3, labelanchor="n")
recommendations_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Recommendation Labels with dynamic wrap length ( pre analyze )
passlen_label = tk.Label(recommendations_frame, text="Length :", font=("Courier", 10,"bold"), fg="lime", bg="black", wraplength=700)
passlen_label.pack(anchor="w", pady=2)

consecutive_label = tk.Label(recommendations_frame, text="Consecutive Characters :", font=("Courier", 10,"bold"), fg="lime", bg="black", wraplength=700)
consecutive_label.pack(anchor="w", pady=2)

uplow_label = tk.Label(recommendations_frame, text="Upper-Lower Mix :", font=("Courier", 10,"bold"), fg="lime", bg="black", wraplength=700)
uplow_label.pack(anchor="w", pady=2)

numbers_label = tk.Label(recommendations_frame, text="Numbers :", font=("Courier", 10,"bold"), fg="lime", bg="black", wraplength=700)
numbers_label.pack(anchor="w", pady=2)

symbols_label = tk.Label(recommendations_frame, text="Symbols :", font=("Courier", 10,"bold"), fg="lime", bg="black", wraplength=700)
symbols_label.pack(anchor="w", pady=2)

dbleak_label = tk.Label(recommendations_frame, text="Password Commonality :", font=("Courier", 10, "bold"), fg="lime", bg="black", wraplength=700)
dbleak_label.pack(anchor="w", pady=2)

# Bind the window resizing event to update wraplength dynamically
recommendations_frame.bind("<Configure>", update_wraplength)

# Run the application
root.mainloop()
