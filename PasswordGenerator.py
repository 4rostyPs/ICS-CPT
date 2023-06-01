# Random password generator between 8-10 characters

#import modules
import tkinter as tk
import random
import string

def generator():
    # Create the main root
    root = tk.Tk()
    root.title("Password Generator")

    # Set the root size
    root.geometry("600x500")

    # Displayed text above dialogue
    dialogue_label = tk.Label(root, wraplength=500, font=("Arial", 10), text="A Strong password is random and includes special characters.\n\nOptimal password size: 8-10 characters")
    dialogue_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

    # Create a frame to hold the label and button
    frame = tk.Frame(root)

    # Suggested password label text
    password_label = tk.Label(frame, text="(Click the \"Generate Password\" button below)", font=("Arial", 12, "italic"))
    password_label.pack(pady=5)

    # Pack the frame in the center of the window
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create random password structure
    def generate_password():
        password_characters = random.randint(8, 10)
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_characters)) #creates a password mixed with letters, numbers, and symbols
        password_label.config(font=("Arial", 18, "bold"))
        password_label.config(text="Generated Password:\n" + password)

    # Button to generate password
    generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12, "bold"))
    generate_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Continue button and assigned properties
    continue_button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    continue_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    # Run the main root loop
    root.mainloop()