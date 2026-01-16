import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = entry_length.get()

    if not length.isdigit():
        messagebox.showerror("Error", "Please enter a valid number")
        return

    length = int(length)

    characters = ""

    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_numbers.get():
        characters += string.digits
    if var_symbols.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one option")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    entry_output.delete(0, tk.END)
    entry_output.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(entry_output.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x350")
root.resizable(False, False)

# Heading
tk.Label(root, text="PASSWORD GENERATOR", font=("Arial", 14, "bold")).pack(pady=10)

# Length
tk.Label(root, text="Password Length").pack()
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Checkboxes
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor="w", padx=50)

# Generate Button
tk.Button(root, text="Generate Password", bg="green", fg="white",
          command=generate_password).pack(pady=10)

# Output
entry_output = tk.Entry(root, width=30)
entry_output.pack(pady=5)

# Copy Button
tk.Button(root, text="Copy Password", bg="blue", fg="white",
          command=copy_password).pack(pady=5)

root.mainloop()
