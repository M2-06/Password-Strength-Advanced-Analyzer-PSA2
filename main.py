import tkinter as tk
from tkinter import ttk
from Sha256 import txtToSHA256
from Api import check_password_hash
from Score import evaluate_password_strength  # Assuming the above code is in this file

# Function to handle password evaluation and display results
def analyze_password():
    password = password_entry.get()
    if not password:
        score_label.config(text="Enter a password to analyze.")
        return

    # Step 1: Evaluate password and get results
    score, passlen, consecutive, uplow, numbers, symbols, dbleak = evaluate_password_strength(password)
    
    # Step 2: Get SHA256 hash and check against database for exposures
    hashed_password = txtToSHA256(password)
    times_found = check_password_hash(hashed_password)
    
    # Display the results in the UI
    score_label.config(text=f"Password Score: {score}")
    db_check_label.config(text=f"Found {times_found} times in leaked passwords databases.")
    passlen_label.config(text=f"Length: {passlen}")
    consecutive_label.config(text=f"Consecutive Characters: {consecutive}")
    uplow_label.config(text=f"Upper-Lower Mix: {uplow}")
    numbers_label.config(text=f"Numbers: {numbers}")
    symbols_label.config(text=f"Symbols: {symbols}")
    dbleak_label.config(text=f"Leak Status: {dbleak}")

# Main Tkinter window setup
root = tk.Tk()
root.title("Password Analyzer")
root.geometry("750x450")
root.resizable(False, False)

# Title Label
title_label = ttk.Label(root, text="Password Strength Advanced Analyzer by M²", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Input Section
input_frame = ttk.Frame(root)
input_frame.pack(pady=5)

password_label = ttk.Label(input_frame, text="Enter Password:")
password_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
password_entry = ttk.Entry(input_frame, width=30, show="*")
password_entry.grid(row=0, column=1, padx=5, pady=5)
analyze_button = ttk.Button(input_frame, text="Analyze", command=analyze_password)
analyze_button.grid(row=0, column=2, padx=5, pady=5)

# Results Section
# Score Display
score_label = ttk.Label(root, text="Password Score:", font=("Helvetica", 12, "bold"))
score_label.pack(pady=(10, 5))

# Database Check Count Display
db_check_label = ttk.Label(root, text="Found 0 times in leaked passwords databases.", font=("Helvetica", 10))
db_check_label.pack(pady=(0, 10))

# Frame for Recommendations
recommendations_frame = ttk.LabelFrame(root, text="Recommendations", padding=(10, 10))
recommendations_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Recommendation Labels
passlen_label = ttk.Label(recommendations_frame, text="Length:", font=("Helvetica", 10))
passlen_label.pack(anchor="w", pady=2)

consecutive_label = ttk.Label(recommendations_frame, text="Consecutive Characters:", font=("Helvetica", 10))
consecutive_label.pack(anchor="w", pady=2)

uplow_label = ttk.Label(recommendations_frame, text="Upper-Lower Mix:", font=("Helvetica", 10))
uplow_label.pack(anchor="w", pady=2)

numbers_label = ttk.Label(recommendations_frame, text="Numbers:", font=("Helvetica", 10))
numbers_label.pack(anchor="w", pady=2)

symbols_label = ttk.Label(recommendations_frame, text="Symbols:", font=("Helvetica", 10))
symbols_label.pack(anchor="w", pady=2)

dbleak_label = ttk.Label(recommendations_frame, text="Leak Status:", font=("Helvetica", 10))
dbleak_label.pack(anchor="w", pady=2)

# Run the application
root.mainloop()
