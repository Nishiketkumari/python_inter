import tkinter as tk
from tkinter import messagebox

def convert_case():
    """Convert lowercase letters to uppercase and vice versa."""
    input_text = input_textbox.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Warning", "Input text is empty!")
        return

    converted_text = input_text.swapcase()
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, converted_text)

root = tk.Tk()
root.title("Case Converter")
root.geometry("500x300")
root.configure(bg="#f0f8ff")

title_label = tk.Label(root, text="Case Converter", font=("Arial", 18, "bold"), bg="#4682b4", fg="white")
title_label.pack(pady=10, fill=tk.X)

input_label = tk.Label(root, text="Enter text:", font=("Arial", 12), bg="#f0f8ff")
input_label.pack(pady=5)
input_textbox = tk.Text(root, height=5, width=50, font=("Arial", 12), bg="#e6f7ff", fg="#333333")
input_textbox.pack(pady=5)

convert_button = tk.Button(root, text="Convert Case", command=convert_case, font=("Arial", 12, "bold"), bg="#32cd32", fg="white", activebackground="#228b22")
convert_button.pack(pady=10)

output_label = tk.Label(root, text="Converted text:", font=("Arial", 12), bg="#f0f8ff")
output_label.pack(pady=5)
output_textbox = tk.Text(root, height=5, width=50, font=("Arial", 12), bg="#fff5ee", fg="#333333")
output_textbox.pack(pady=5)

root.mainloop()
