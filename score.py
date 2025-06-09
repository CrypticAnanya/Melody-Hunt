from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
import os
root=Tk()
root.title('Game Over')
root.geometry("700x700")
connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                     port='3306', database='melody')
c = connection.cursor()

def playagain():
    root.destroy()
    os.system("lang.py")
def homepage():
    root.destroy()
    os.system("welcome.py")
im = Image.open("game.jpg")
image_resize = im.resize((700,700))
photo = ImageTk.PhotoImage(image_resize)
label1 = Label(image=photo)
label1.image=photo
label1.pack()

l=Label(root,text="SCOREBOARD",font=("algerian bold",30)).place(x=200,y=100)

q="select name from login"
c.execute(q)
user=c.fetchall()
user=user[-1]
l=Label(root,text="HERE IS YOUR SCORE~",font=("helvetica",25)).place(x=170,y=200)
l=Label(root,text=user[0].upper(),font=("helvetica bold",25)).place(x=300,y=300)
q="select score from user where name=%s"
c.execute(q,(user[0],))
sc=c.fetchone()
l=Label(root,text=sc,font=("helvetica bold",30),fg='white',bg='black').place(x=350,y=400)
b1=Button(root,text="Play Again",font=("Elephant",30),command=playagain,bg="black",fg="white").place(x=200,y=500)
b2=Button(root,text="Home Page",font=("Elephant",30),command=homepage,bg="black",fg="white").place(x=500,y=500)
root.mainloop()