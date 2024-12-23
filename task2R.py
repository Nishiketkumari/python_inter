import tkinter as tk

def button_click(value):
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "Cut":
        current_text = entry.get()
        if current_text:
            entry.delete(0, tk.END)
            entry.insert(0, current_text[:-1])
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", ""],
    ["C", "Cut"]
]

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        button = tk.Button(root, text=button_text, font=("Arial", 18), command=lambda val=button_text: button_click(val))
        button.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(len(buttons) + 1):
    root.grid_rowconfigure(i, weight=1)
root.mainloop()
