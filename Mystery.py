import tkinter as tk
import mysql.connector
from tkinter import *
from tkhtmlview import HTMLLabel


def logintodb():
    mydb = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="mydb")
    cursor = mydb.cursor()
    savequery = "insert into players(username,password) values(%s,%s)"
    val=(Username.get(),password.get())
    try:
        cursor.execute(savequery,val)
        mydb.commit()
        label1=HTMLLabel(root,html="""<h1>Welcome</h1> <a href="firstPage.html">Play</a>""")
        label1.pack(fill="both",expand=True)
    except:
        mydb.rollback()
        print("Error occurred")


root = tk.Tk()
root.geometry("950x500")
root.title("Login to play")


# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -" )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login",
					bg ='blue', command = logintodb)
submitbtn.place(x = 150, y = 135, width = 55)

root.mainloop()
 