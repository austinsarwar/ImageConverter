from PIL import Image  # Python Image Library - Image Processing
import glob
import tkinter as tk
from tkinter import Button, filedialog
import os
root = tk.Tk()
root.geometry("300x200")
root.title("Image converter")
select_button = Button(root,text="Select File")
select_button.pack()
select_button.config(font=("Arial",20))
convert_button = Button(root, text="Convert File")
convert_button.config(font=("Arial",20))
convert_button.pack()


def file_convert(file):
     for file in glob.glob("*.png"):
          im = Image.open(file)
          rgb_im = im.convert('RGB')
          rgb_im.save(file.replace("png", "jpg"), quality=95)



root.mainloop()