import tkinter as tk
from tkinter import messagebox
import openai

# Set your OpenAI API key here
openai.api_key = "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"

def get_chatbot_response():
    """Get a response from the chatbot using OpenAI's API."""
    user_input = input_textbox.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Warning", "Input text is empty!")
        return

    try:
        # Call the OpenAI API to get a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        chatbot_reply = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        chatbot_reply = f"Error: {e}"

    # Display the response in the output textbox
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, chatbot_reply)

# Create the main window
root = tk.Tk()
root.title("Chatbot")
root.geometry("500x500")
root.configure(bg="#f0f8ff")

# Add title label
title_label = tk.Label(root, text="Chatbot", font=("Arial", 18, "bold"), bg="#4682b4", fg="white")
title_label.pack(pady=10, fill=tk.X)

# Add input text label and textbox
input_label = tk.Label(root, text="Your message:", font=("Arial", 12), bg="#f0f8ff")
input_label.pack(pady=5)
input_textbox = tk.Text(root, height=5, width=50, font=("Arial", 12), bg="#e6f7ff", fg="#333333")
input_textbox.pack(pady=5)

# Add send button
send_button = tk.Button(root, text="Send", command=get_chatbot_response, font=("Arial", 12, "bold"), bg="#32cd32", fg="white", activebackground="#228b22")
send_button.pack(pady=10)

# Add output text label and textbox
output_label = tk.Label(root, text="Chatbot reply:", font=("Arial", 12), bg="#f0f8ff")
output_label.pack(pady=5)
output_textbox = tk.Text(root, height=10, width=50, font=("Arial", 12), bg="#fff5ee", fg="#333333")
output_textbox.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
