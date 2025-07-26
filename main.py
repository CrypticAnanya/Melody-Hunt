from tkinter import *
from PIL import Image,ImageTk
import os
root=Tk()

root.title("Welcome")
root.geometry("1000x1000")

im = Image.open("bg.jpg")
image_resize = im.resize((1000,1000))
photo = ImageTk.PhotoImage(image_resize)
label1 = Label(image=photo)
label1.image=photo
label1.pack()
def signup():
    root.destroy()
    os.system('signup.py')
def login():
    root.destroy()
    os.system('login.py')
l=Label(root,text="Welcome To ",font=("Rockwell bold",50)).place(x=300,y=20)
l=Label(root,text="MELODY HUNT ",font=("Rockwell bold",60),bg='black',fg='white').place(x=180,y=120)
b1=Button(root,text="SIGN UP",command=signup,font=('Helvetica',20)).place(x=200,y=500)

b1=Button(root,text="LOGIN",command=login,font=('Helvetica',20)).place(x=600,y=500)
root.mainloop()
