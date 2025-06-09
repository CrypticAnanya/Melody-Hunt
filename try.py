# importing required module
from playsound import playsound
from tkinter import *
from pygame import mixer
from PIL import Image,ImageTk
import time
mixer.init()
root = Tk()
root.title('Melody Hunt') #giving the title for our window
root.geometry("500x400")
#im = Image.open("bg.jpg")
# making function
def play():
	mixer.music.load('heer.mp3')
	mixer.music.play()
	time.sleep(25)
	mixer.music.stop()
# title on the screen you can modify it
title=Label(root,text="WELCOME TO MELODY HUNT",bd=9,relief=GROOVE,
			font=("ALGERIAN",30,"bold"),bg="white",fg="green")
title.pack(side=TOP,fill=X)

# making a button which trigger the function so sound can be playeed
play_button = Button(root, text="Play Song", font=("Helvetica", 32),
					relief=GROOVE, command=play)
play_button.pack(pady=20)

info=Label(root,text="Click on the button above to play song ",
		font=("times new roman",10,"bold")).pack(pady=20)
root.mainloop()
