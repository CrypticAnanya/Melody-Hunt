from tkinter import *
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import os
root=Tk()
root.title("login")
connection = mysql.connector.connect(host='localhost', user='root', password='admin',
                                     port='3306', database='melody')
c = connection.cursor()
bkg = "#fff600"

def data():
    name1=entry_name.get()
    pswd1=entry_pswd.get()
    query="select name,password from user "
    c.execute(query)
    d2=c.fetchall()
    q="insert into login values(%s,%s)"
    data=(name1,pswd1)
    c.execute(q,data)
    connection.commit()
    q="update user set score=0"
    c.execute(q)
    connection.commit()
    check=0
    for i,j in d2:
        if(name1==i and pswd1==j):
            check=1
            messagebox.showinfo("Success", "Login Successfull")
            root.destroy()
            os.system('lang.py')
    if(check==1):
        q = "update counts set c=%s where lang=%s"
        c.execute(q, (1, "hin"))
        connection.commit()
        q = "update counts set c=%s where lang=%s"
        c.execute(q, (1, "eng"))
        connection.commit()
        q = "update counts set c=%s where lang=%s"
        c.execute(q, (1, "pun"))
        connection.commit()

    else:
        messagebox.showinfo("Sorry", "Invalid Name or Password")
frame = tk.Frame(root, bg=bkg)
name = tk.Label(frame, text="NAME: ", font=('verdana BOLD',12), bg=bkg)
entry_name = tk.Entry(frame, font=('verdana',12))

pswd = tk.Label(frame, text="PASSWORD: ", font=('verdana BOLD',12), bg=bkg)
entry_pswd = tk.Entry(frame, font=('verdana',12),show="*")

name.grid(row=0, column=0)
entry_name.grid(row=0, column=1, pady=10, padx=10)

pswd.grid(row=1, column=0)
entry_pswd.grid(row=1, column=1, pady=10, padx=10)
submit=tk.Button(frame,text="Login",font=('verdana',12),command=data)
submit.grid(row=2, column=0)
frame.grid(row=0, column=0)
root.mainloop()