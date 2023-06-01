# Dialoge 10: Email comparisons

#import modules
import tkinter as tk
from PIL import ImageTk, Image

def dialogue10():

    root = tk.Tk()
    root.title("Dialogue Box")

    # Set the window position and dimensions
    root.geometry("1000x700")

    # Load and size the images
    image1 = Image.open("H:\pyzo\CPT Dialogues\images\email1.png")
    image1 = image1.resize((475, 350), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("H:\pyzo\CPT Dialogues\images\email2.jpg")
    image2 = image2.resize((400, 450), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)

    # Create labels for the images
    label1 = tk.Label(root, image=image1)
    label1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

    label2 = tk.Label(root, image=image2)
    label2.place(relx=0.75, rely=0.33, anchor=tk.CENTER)

    # Create text labels below the images
    top_text = "We can tell a E-mail is legit by checking\nthe email address and the format of the email\n For example:"
    top_text = tk.Label(root, font=("Arial", 14, "bold"), text=top_text)
    top_text.place(relx=0.3, rely=0.07, anchor=tk.CENTER)

    text1 = "This E-mail seems FAKE because the sender's email address doesn't belong to Costco, the logo is inaccurate, and the email is not associated with their company/website."
    text_label1 = tk.Label(root, font=("Arial", 12,), wraplength=450, text=text1)
    text_label1.place(relx=0.3, rely=0.7, anchor=tk.CENTER)

    text2 = "This email seems LEGIT as it has a more neat and professional email format, and the sender's email address is linked to their official website. (as seen near the bottom)\n\n It's important to be careful and check if the email is genuine before doing anything it asks you to do."
    text_label2 = tk.Label(root, font=("Arial", 12,), wraplength=400, text=text2)
    text_label2.place(relx=0.75, rely=0.75, anchor=tk.CENTER)

    # Continue button command
    def continue_clicked():
        root.destroy()
    # Create the "Continue" button
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
