import tkinter as tk
import Dialogue3


def certificate_dialogue():
    def close_dialogue():
        root.destroy()

    root = tk.Tk()
    root.title("Certificate")


    # Set the window position and dimensions
    root.geometry(f"800x400")


    # Create the top text label
    top_text_label = tk.Label(root, text="Congratulations!", font=("Arial", 24, "bold"))
    top_text_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    # Create the middle text label for username
    top_text_label = tk.Label(root, text="Congrats", font=("Arial", 20, "underline"))
    top_text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Create the bottom text label
    bottom_text_label = tk.Label(root, text="for sucessfully completing this program", font=("Arial", 18))
    bottom_text_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Create the "Close" button
    close_button = tk.Button(root, text="Close", width=10, height=2, font=("Arial", 12), command=close_dialogue)
    close_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
