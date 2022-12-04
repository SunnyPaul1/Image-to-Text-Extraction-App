import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

def upload_file():
    global img
    f_types = [('Files', '*')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(filename)
    img_resized = img.resize((300,200))
    img_resized.save('sample.png')

    try:
        text= pytesseract.image_to_string(img_resized, lang="eng")
        char_remove = "!()@-*'<>+/,|$#%&^_~.:;`´'"
        new_string = text
        for char in char_remove:
            new_string=new_string.replace(char, "")
    except IOError as e:
        new_string = "Error"

    b2 = tk.Button(my_w, text=new_string)
    b2.grid(row=3, column=1)

## From here create GUI interface

my_w = tk.Tk()
my_w.geometry("400x400")
my_w.title("Image to Text")
my_font1 = ("times", 18, "bold")
l1 = tk.Label(my_w, text='Add an Image to Extract Text', width=30, font=my_font1)
l1.grid(row=1, column=1)

b1=tk.Button(my_w, text='Upload File', width=20, command=lambda:upload_file())
b1.grid(row=2, column=1)


my_w.mainloop()

# Ref:plus2net.com/python/tkinter-filedialog-upload-display.php