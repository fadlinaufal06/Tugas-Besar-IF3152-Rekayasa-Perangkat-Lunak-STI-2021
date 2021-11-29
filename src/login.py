# Penanggung jawab: Rahmat Fabhian Aminuddin 18219055
import sys
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os
import mysql.connector as mysql
import mariadb
from homescreen import homescreen

def home(layar):
  global screen
  layar.destroy()
  screen = Tk()
  screen.title("MONITROS")
  screen.geometry("1270x690")
  screen.config(bg = "white")
  screen.bg_img = ImageTk.PhotoImage(file="img/login.jpg")
  background = Label(screen, image = screen.bg_img).place(x = 0, y = 0, relwidth = 1, relheight = 1)

  def registrasi():
    register(screen)

  global Username_verify
  global Passwords_verify
  
  Username_verify = StringVar()
  Passwords_verify = StringVar()

  global Username_login
  global Passwords_login
  
  #field Username
  Label(screen, text = "Username", font = ("Helvetica", 15, "bold"), bg="white").place(x = 850, y = 220)
  Username_login = Entry(screen, textvariable = Username_verify, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Username_login.place(x = 850, y = 250, width = 300, height = 30)

  #field Passwords
  Label(screen, text = "Password", font = ("Helvetica", 15, "bold"), bg="white").place(x = 850, y = 320)
  Passwords_login = Entry(screen, textvariable = Passwords_verify, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Passwords_login.place(x = 850, y = 350, width = 300, height = 30)

  #button login
  Button(screen, text = "LOGIN", font = ("Helvetica", 15, "bold"), bg="cyan", width = 10, height = 1, command = login_verify).place(x = 940, y = 420)

  #register
  Label(screen, text = "Belum punya akun? ", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 570)
  Button(text = "DAFTAR DISINI!", font=("Helvetica", 15, "bold"), bg = "red", fg = "white", command =registrasi).place(x = 700, y = 570, height = 30, width = 160)

  screen.mainloop()

def register(screen):
  global screen1
  screen.destroy()
  screen1 = Tk()
  screen1.title("MONITROS")
  screen1.geometry("1270x690")
  screen1.config(bg = "white")
  screen1.bg_img = ImageTk.PhotoImage(file="img/register.jpg")
  background = Label(screen1, image = screen1.bg_img).place(x = 0, y = 0, relwidth = 1, relheight = 1)

  def registrasiuser():
    register_user(screen1)

  global Username
  global Passwords
  global Nama_lengkap
  global Nomor_HP
  global Alamat
  global Role

  Username = StringVar()
  Passwords = StringVar()
  Nama_lengkap = StringVar()
  Nomor_HP = StringVar()
  Alamat = StringVar()
  Role = StringVar()

  global Username_register
  global Passwords_register
  global Nama_lengkap_register
  global Nomor_HP_register
  global Alamat_register
  global Role_register

  #field Username
  Label(screen1, text = "Username", font = ("Helvetica", 15, "bold"), bg="white").place(x = 50, y = 200)
  Username_register = Entry(screen1, textvariable = Username, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Username_register.place(x = 50, y = 230, width = 300, height = 30)

  #field Passwords
  Label(screen1, text = "Password", font = ("Helvetica", 15, "bold"), bg="white").place(x = 450, y = 400)
  Passwords_register = Entry(screen1, textvariable = Passwords, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Passwords_register.place(x = 450, y = 430, width = 300, height = 30)

  #field nama
  Label(screen1, text = "Nama Lengkap", font = ("Helvetica", 15, "bold"), bg="white").place(x = 50, y = 300)
  Nama_lengkap_register = Entry(screen1, textvariable = Nama_lengkap, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Nama_lengkap_register.place(x = 50, y = 330, width = 300, height = 30)

  #field nomor hp
  Label(screen1, text = "Nomor HP", font = ("Helvetica", 15, "bold"), bg="white").place(x = 50, y = 400)
  Nomor_HP_register = Entry(screen1, textvariable = Nomor_HP, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Nomor_HP_register.place(x = 50, y = 430, width = 300, height = 30)

  #field Alamat
  Label(screen1, text = "Alamat", font = ("Helvetica", 15, "bold"), bg="white").place(x = 450, y = 200)
  Alamat_register = Entry(screen1, textvariable = Alamat, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Alamat_register.place(x = 450, y = 230, width = 300, height = 30)

  #field role
  Label(screen1, text = "Role", font = ("Helvetica", 15, "bold"), bg="white").place(x = 450, y = 300)
  Role_register = Entry(screen1, textvariable = Role, font=("Helvetica", 15), bg = "light grey", fg = "black")
  Role_register.place(x = 450, y = 330, width = 300, height = 30)

  #button register
  Button(screen1, text = "DAFTAR", font=("Helvetica", 15, "bold"), bg = "cyan", fg = "black", command = registrasiuser).place(x = 900, y = 315, height = 50, width = 160)

#fungsi actionzzzz
def register_user(screen):
  # Connect to Mariadb
  try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="monitros"
    )
  except mariadb.Error as e:
      print(f"Error connecting to MariaDB Platform: {e}")
      sys.exit(1)
  
  # Get Cursor
  cur = conn.cursor()
  Query = "INSERT INTO data_user VALUES (%s,%s,%s,%d,%s,%s)"
  data = (Username.get(),Passwords.get(),Nama_lengkap.get(),Nomor_HP.get(),Alamat.get(),Role.get())
  cur.execute(Query, data)
  if Username.get() == "" and Passwords.get() == "" and Nama_lengkap.get() == "" and Nomor_HP.get() == "" and Alamat.get() == "" and Role.get() == "":
      all_woy()
  elif Passwords.get() == "":
      password_isi_woy()
  elif Nama_lengkap.get() == "":
      naleng_isi_woy()
  elif Nomor_HP.get() == "":
      phone_isi_woy()
  elif Alamat.get() == "":
      alamat_isi_woy()
  elif Role.get() == "":
      role_isi_woy()
  elif Username.get() == "":
      username_isi_woy()
  else:
    conn.commit()
    Label(screen1, text = "Berhasil terdaftar!", fg = "green" ,font = ("Helvetica", 11)).pack()
    home(screen)

def login_verify():
  # Connect to Mariadb
  try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="localhost",
        port=3306,
        database="monitros"
    )
  except mariadb.Error as e:
      print(f"Error connecting to MariaDB Platform: {e}")
      sys.exit(1)

  # Get Cursor
  cur = conn.cursor()
  cur.execute("select * from data_user where Username=%s and Password=%s",(Username_login.get(),Passwords_login.get()))
  row=cur.fetchone()
  if row == None:
      pengguna_salah()
  else:
      berhasil_login()
  conn.commit()

#the ifs buat register
def username_isi_woy():
  Label(screen1, text = "Username harus diisi!", fg = "red", font = ("Helvetica", 13)).pack()

def password_isi_woy():
  Label(screen1, text = "Password harus diisi!", fg = "red", font = ("Helvetica", 13)).pack()

def naleng_isi_woy():
  Label(screen1, text = "Nama lengkap harus diisi!", fg = "red", font = ("Helvetica", 13)).pack()

def phone_isi_woy():
  Label(screen1, text = "Nomor HP harus diisi!", fg = "red", font = ("Helvetica", 13)).pack()

def alamat_isi_woy():
  Label(screen1, text = "Alamat harus diisi!", fg = "red", font = ("Helvetica", 13)).pack()

def role_isi_woy():
  Label(screen1, text = "Role harus diisi!", fg = "red", font = ("Helvetica", 13)).pack()

def all_woy():
  Label(screen1, text = "Datanya harus diisi semua!", fg = "red", font = ("Helvetica", 13)).pack()

#the ifs buat login
def berhasil_login():
  Label(screen, text = "Berhasil login!", fg = "green" ,font = ("Helvetica", 13)).pack()
  homescreen(screen)

def pengguna_salah():
  Label(screen, text = "Username atau Password salah! Coba lagi", fg = "red" ,font = ("Helvetica", 13)).pack()
