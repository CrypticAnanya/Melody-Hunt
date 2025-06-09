from tkinter import *
import tkinter as tk
import mysql.connector
import os
from tkinter import messagebox
root=Tk()
root.title("Signup")
connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                     port='3306', database='melody')
c = connection.cursor()
bkg = "#FF0000"
def data():
    name=entry_name.get()
    pswd=entry_pswd.get()
    get_query="select name from user"
    c.execute(get_query)
    datac=c.fetchall()
    found=0
    for i in datac:
        if (i==(name,)):
            found=1
    if found==0:
        insert_query="insert into user values(%s,%s,%s)"
        data=(name,pswd,0)
        c.execute(insert_query,data)
        messagebox.showinfo("Success", "Registration Successfully")
        connection.commit()
    else:
        messagebox.showinfo("Fail", "Registration name already exists try again!")

def welcome():
    root.destroy()
    os.system("welcome.py")

frame = tk.Frame(root, bg=bkg)
name = tk.Label(frame, text="NAME: ", font=('verdana BOLD',12), bg=bkg)
entry_name = tk.Entry(frame, font=('verdana',12))

pswd = tk.Label(frame, text="PASSWORD: ", font=('verdana BOLD',12), bg=bkg)
entry_pswd = tk.Entry(frame, font=('verdana',12))

name.grid(row=0, column=0)
entry_name.grid(row=0, column=1, pady=10, padx=10)

pswd.grid(row=1, column=0)
entry_pswd.grid(row=1, column=1, pady=10, padx=10)
submit=tk.Button(frame,text="Submit",font=('verdana',12),command=data)
back=tk.Button(frame,text="Back",font=('verdana',12),command=welcome)
frame.grid(row=0, column=0)
submit.grid(row=2,column=2)
back.grid(row=2,column=0)
root.mainloop()