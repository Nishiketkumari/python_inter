import tkinter as tk

def convert_case():
    text = input_text.get()  
    if var.get() == 1:  
        output_text.set(text.upper())
    else:  
        output_text.set(text.lower())

root = tk.Tk()
root.title("Case Converter")

output_text = tk.StringVar()

label = tk.Label(root, text="Enter text to convert:")
label.pack()

input_text = tk.Entry(root, width=50)
input_text.pack()

var = tk.IntVar()

uppercase_radio = tk.Radiobutton(root, text="To Uppercase", variable=var, value=1)
uppercase_radio.pack()

lowercase_radio = tk.Radiobutton(root, text="To Lowercase", variable=var, value=0)
lowercase_radio.pack()

convert_button = tk.Button(root, text="Convert", command=convert_case)
convert_button.pack()

output_label = tk.Label(root, text="Converted Text:")
output_label.pack()

output_display = tk.Label(root, textvariable=output_text, width=50)
output_display.pack()

root.mainloop()
