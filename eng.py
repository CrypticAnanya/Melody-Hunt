from tkinter import *
from turtle import goto

from PIL import Image,ImageTk
from pygame import mixer
from tkinter import messagebox
import os
import mysql.connector
import random
root=Tk()
connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                     port='3306', database='melody')
c = connection.cursor()
root.geometry("700x700")
import time
mixer.init()
im = Image.open("eng2.jpg")
image_resize = im.resize((700,700))
photo = ImageTk.PhotoImage(image_resize)
label1 = Label(image=photo)
label1.image=photo
label1.pack()
def guess():
	data = g.get()
	q = "select songname from engsongs where songname=%s"
	c.execute(q,(data,))
	data2=c.fetchone()
	randsong=random_mp3.split('.')
	if data2:
		if (randsong[0] in data2[0]):
			messagebox.showinfo('success','right answer')
			q="select name,password from login"
			c.execute(q)
			user=c.fetchall()
			user=user[-1]
			q="select score from user where name=%s and password=%s"
			c.execute(q,(user[0],user[1]))
			sc=c.fetchone()
			sc=str(int(sc[0])+1)
			q="update user set score=%s where name=%s and password=%s"
			c.execute(q,(sc,user[0],user[1]))
			connection.commit()
	else:
		messagebox.showinfo('fail','wrong answer')
def play():
	global random_mp3
	folder_path = "./english_songs"
	random_file=[]
	mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]
	random_mp3= random.choice(mp3_files)
	if random_mp3 not in random_file:
		random_file.append(random_mp3)
		mixer.music.load(folder_path+'/'+random_mp3)
		mixer.music.play()
		time.sleep(20)
		mixer.music.stop()
	else :
		play()



def next():
	g.delete(0, 'end')
	q="select c from counts where lang=%s"
	c.execute(q,("eng",))
	coun=c.fetchone()
	coun=str(int(coun[0])+1)
	q="update counts set c=%s where lang=%s"
	c.execute(q,(coun,"eng"))
	connection.commit()
	if(coun=="6"):
		q = "update counts set c=%s where lang=%s"
		c.execute(q,("1","eng",))
		root.destroy()
		os.system('score.py')


play_button = Button(root, text="Play Song", font=("Helvetica", 32),relief=GROOVE, command=play).place(x=250,y=250)
g=Entry(root,font=("Helvetica",25))
g.place(x=180,y=350)

guess=Button(root,text="GUESS",font=("Helvetica",20),command=guess).place(x=300,y=420)
next=Button(root,text="NEXT SONG",font=("Helvetica",20),command=next,fg='white',bg='black').place_configure(x=270,y=500)
root.mainloop()