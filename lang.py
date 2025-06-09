from tkinter import *
from PIL import Image,ImageTk
import os
root=Tk()
root.title('language')
root.geometry("700x700")

im = Image.open("lang2.jpg")
image_resize = im.resize((700,700))
photo = ImageTk.PhotoImage(image_resize)
label1 = Label(image=photo)
label1.image=photo
label1.pack()
def eng():
    root.destroy()
    os.system('eng.py')
def hin():
    root.destroy()
    os.system('hin.py')
def pun():
    root.destroy()
    os.system('pun.py')
l=Label(root,text="Choose the language :",font=('algerian',27)).place(x=150,y=120)
e=Button(root,text="ENGLISH",font=('Elephant bold',18),command=eng).place(x=300,y=250)
e=Button(root,text="HINDI",font=('Elephant bold',18),command=hin).place(x=320,y=350)
e=Button(root,text="PUNJABI",font=('Elephant bold',18),command=pun).place(x=300,y=450)
root.mainloop()