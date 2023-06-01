import tkinter as tk
from PIL import ImageTk, Image

def dialogue9():

    root = tk.Tk()
    root.title("Dialogue Box")

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the center coordinates of the screen
    center_x = int((screen_width - 800) / 2)
    center_y = int((screen_height - 600) / 2)

    # Set the window position and dimensions
    root.geometry(f"800x600")

    # Load and resize the images
    image1 = Image.open("H:\pyzo\CPT Dialogues\email1.png")
    image1 = image1.resize((300, 400), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("H:\pyzo\CPT Dialogues\email2.jpg")
    image2 = image2.resize((300, 400), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(image2)

    # Create labels for the images
    label1 = tk.Label(root, image=image1)
    label1.place(relx=0.25, rely=0.3, anchor=tk.CENTER)

    label2 = tk.Label(root, image=image2)
    label2.place(relx=0.75, rely=0.3, anchor=tk.CENTER)

    # Create text labels below the images
    text1 = "Image 1 description"
    text_label1 = tk.Label(root, text=text1)
    text_label1.place(relx=0.25, rely=0.6, anchor=tk.CENTER)

    text2 = "Image 2 description"
    text_label2 = tk.Label(root, text=text2)
    text_label2.place(relx=0.75, rely=0.6, anchor=tk.CENTER)


    def continue_clicked():
        root.destroy()
    # Create the "Continue" button
    button = tk.Button(root, text="Continue", width=10, height=2, font=("Arial", 12), command=continue_clicked)
    button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    root.mainloop()
