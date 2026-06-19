import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime

# Chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm doing great!", "Doing well, thanks!", "All systems operational!"],
    "what is your name": ["I am SmartBot.", "My name is SmartBot."],
    "help": ["I can answer simple questions and chat with you."],
    "thank you": ["You're welcome!", "Happy to help!"]
}

def get_response(message):
    message = message.lower().strip()

    if message == "time":
        return f"Current time is {datetime.now().strftime('%H:%M:%S')}"

    if message == "date":
        return f"Today's date is {datetime.now().strftime('%d-%m-%Y')}"

    if message in responses:
        return random.choice(responses[message])

    return "Sorry, I don't understand that."

def send_message():
    user_message = entry_box.get()

    if not user_message:
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_message}\n")

    bot_reply = get_response(user_message)
    chat_area.insert(tk.END, f"Bot: {bot_reply}\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry_box.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("SmartBot Chat Application")
root.geometry("600x500")

# Heading
heading = tk.Label(
    root,
    text="SmartBot Chat Assistant",
    font=("Arial", 16, "bold")
)
heading.pack(pady=10)

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=70,
    height=20,
    state=tk.DISABLED
)
chat_area.pack(padx=10, pady=10)

# Input Frame
frame = tk.Frame(root)
frame.pack(pady=10)

entry_box = tk.Entry(frame, width=50, font=("Arial", 12))
entry_box.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(
    frame,
    text="Send",
    command=send_message,
    width=10
)
send_button.pack(side=tk.LEFT)

root.mainloop()