#Dialogue 4: introduction to reward programs & risks

# Import module used for dialogue boxes
import tkinter as tk

def dialogue4():

    # Defining what happens when user clicks the continue button
    def continue_clicked():
        root.destroy()

    # Setting descriptions of Tkinter program
    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("600x500")

    # Display text
    dialogue_text = "Rewards Programs offer great benefits, but they also come with many risks...\n\nHackers and scammers target accounts, selling them or stealing untraceable reward points. They use data breaches or send fake emails posing as the program.\n\nSo let's learn to protect ourselves, to stay informed, and to stay safe!"

    # Text properties
    dialogue_label = tk.Label(root, wraplength=530, font=("Arial", 14), text=dialogue_text)
    dialogue_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    #Create button and assign properties
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    root.mainloop()





    '''
    NOTES:
    relx = x-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    rely = y-coordinate ranging from 0.0 to 1.0 (so that means 0.5 is middle)
    anchor options: n, ne, e, se, s, sw, w, nw, or center
    '''