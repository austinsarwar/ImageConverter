from PIL import Image
import tkinter as tk
from tkinter import Button, Label, filedialog
import os

# Create the main window
root = tk.Tk()
root.geometry("300x200")
root.title("Image converter")

# Initialize the filepath variable
filepath = ""

# Define the select_file function
def select_file():
    global filepath
    filepath = filedialog.askopenfilename()

# Define the file_convert function
def file_convert(filepath):
    try:
        # Open the image and convert it to RGB
        im = Image.open(filepath)
        im = im.convert('RGB')
        
        # Create the new filepath and save the image
        new_filepath = os.path.splitext(filepath)[0] + '.jpg'
        im.save(new_filepath, format='JPEG', quality=95)
        
        # Display the success message
        success = Label(root, text="Conversion success")
        success.grid(row=2,column=0,sticky=tk.NSEW)
    except FileNotFoundError:
        # Display the file not found message
        not_found = Label(root, text="File not found")
        not_found.grid(row=1,column=1,sticky=tk.NSEW)
    except OSError:
        # Display the invalid image message
        error = Label(root, text="The selected file is not a valid image.")
        error.grid(row=2,column=0,sticky=tk.NSEW)

# Create the select file button
select_button = Button(root, text="Select File", command=lambda: select_file())
select_button.grid(row=0, column=0,sticky=tk.NSEW)
select_button.config(font=("Arial",20))

# Create the convert file button
convert_button = Button(root, text="Convert File", command=lambda: file_convert(filepath))
convert_button.grid(row=1, column=0,sticky=tk.NSEW)
convert_button.config(font=("Arial",20))

# Start the main event loop
root.mainloop()
