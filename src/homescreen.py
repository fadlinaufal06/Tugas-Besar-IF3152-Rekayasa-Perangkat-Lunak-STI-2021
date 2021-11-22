# Penanggung jawab: Rahmat Fabhian Aminuddin 18219055
import sys

if "tkinter" not in sys.modules:
    from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os
import mysql.connector as mysql
import mariadb

def homescreen():
    global screenhome
    screenhome = Tk()
    screenhome.title("MONITROS")
    screenhome.geometry("1270x690")
    screenhome.config(bg = "white")
    screenhome.bg_img = ImageTk.PhotoImage(file="img/main.jpg")
    background = Label(screenhome, image = screenhome.bg_img).place(x = 0, y = 0, relwidth = 1, relheight = 1)

    #button To-do List
    TodoBut = Image.open('img\initodohome.png')
    TodoBut.load()
    TodoBut = TodoBut.resize((250,250),Image.ANTIALIAS)
    TodoButPI = ImageTk.PhotoImage(TodoBut)
    TodoButton = Button(screenhome, image=TodoButPI).place(x=550,y=300,width=250,height=250)

    #button Menu 
    MenuBut = Image.open('img\menuhome.png')
    MenuBut.load()
    MenuBut = MenuBut.resize((250,250),Image.ANTIALIAS)
    MenuButPI = ImageTk.PhotoImage(MenuBut)
    MenuButton = Button(screenhome, image=MenuButPI).place(x=150,y=300,width=250,height=250)

    #button Peralatan 
    PeralatanBut = Image.open('img\peralatanhome.png')
    PeralatanBut.load()
    PeralatanBut = PeralatanBut.resize((250,250),Image.ANTIALIAS)
    PeralatanButPI = ImageTk.PhotoImage(PeralatanBut)
    PeralatanButton = Button(screenhome, image=PeralatanButPI).place(x=950,y=300,width=250,height=250)

    #button LogOut 
    LogOut = Image.open('img\logout.png')
    LogOut.load()
    LogOut = LogOut.resize((100,100), Image.ANTIALIAS)
    LogOutPI = ImageTk.PhotoImage(LogOut)
    LogOutPicture = Button(screenhome, image=LogOutPI,bg='red').place(x=1060,y=20,width=100,height=100)

    screenhome.mainloop()

homescreen()