# Username entry

# Import module used for dialogue boxes
import tkinter as tk

def dialogue3():

    # Create the main window & setting up tkinter program descriptions
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position
    root.geometry("600x500")

    username = ""

    # Display text
    dialogue_text = "But before we continue...\n Please enter your username:"

    # Creating the dialogue text & properties
    dialogue_label = tk.Label(root, wraplength=580, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Create the entry box for username
    username_entry = tk.Entry(root, width=40, font=("Arial", 12))
    username_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    #~~~~~~~~~~~~~~Creating continue button to close dialogue so it can continue next~~~~~~~~~~~~~~#
    def close_dialogue():
        global username
        username = username_entry.get()
        root.destroy()
    # Create the continue button after every dialogue
    continue_button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=close_dialogue)
    continue_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    root.mainloop()

    # Displays username in console
    print(f"Username: {username}")

    usernametest = "Adwaittest"


    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''