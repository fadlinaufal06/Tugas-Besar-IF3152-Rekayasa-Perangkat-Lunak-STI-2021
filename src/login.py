from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import os


def main_screen():
  global screen
  screen = Tk()
  screen.title("MONITROS")
  screen.geometry("1920x1080")
  screen.config(bg = "white")
  screen.bg_img = ImageTk.PhotoImage(file="img/login.jpg")
  background = Label(screen, image = screen.bg_img).place(x = 0, y = 0, relwidth = 1, relheight = 1)

  global username_verify
  global password_verify
  
  username_verify = StringVar()
  password_verify = StringVar()

  global username_login
  global password_login
  
  #field username
  Label(screen, text = "Username", font = ("Helvetica", 15, "bold"), bg="white").place(x = 850, y = 220)
  username_login = Entry(screen, textvariable = username_verify, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  username_login.place(x = 850, y = 250, width = 300, height = 30)

  #field password
  Label(screen, text = "Password", font = ("Helvetica", 15, "bold"), bg="white").place(x = 850, y = 320)
  password_login = Entry(screen, textvariable = password_verify, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  password_login.place(x = 850, y = 350, width = 300, height = 30)

  #button login
  Button(screen, text = "LOGIN", font = ("Helvetica", 15, "bold"), bg="cyan", width = 10, height = 1, command = login_verify).place(x = 940, y = 420)

  #register
  Label(screen, text = "Belum punya akun? ", font = ("Helvetica", 15, "bold"), bg="white").place(x = 500, y = 570)
  Button(text = "DAFTAR DISINI!", font=("Helvetica", 15, "bold"), bg = "red", fg = "white", command = register).place(x = 700, y = 570, height = 30, width = 160)

  screen.mainloop()

def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("MONITROS")
  screen1.geometry("1920x1080")
  screen1.config(bg = "white")
  screen1.bg_img = ImageTk.PhotoImage(file="img/register.jpg")
  background = Label(screen1, image = screen1.bg_img).place(x = 0, y = 0, relwidth = 1, relheight = 1)

  global username
  global password
  global username_register
  global password_register
  username = StringVar()
  password = StringVar()

  #field username
  Label(screen1, text = "Username", font = ("Helvetica", 15, "bold"), bg="white").place(x = 50, y = 200)
  username_register = Entry(screen1, textvariable = username, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  username_register.place(x = 50, y = 230, width = 300, height = 30)

  #field password
  Label(screen1, text = "Password", font = ("Helvetica", 15, "bold"), bg="white").place(x = 450, y = 400)
  password_register = Entry(screen1, textvariable = password, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  password_register.place(x = 450, y = 430, width = 300, height = 30)

  #field nama
  Label(screen1, text = "Nama Lengkap", font = ("Helvetica", 15, "bold"), bg="white").place(x = 50, y = 300)
  nama_register = Entry(screen1, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  nama_register.place(x = 50, y = 330, width = 300, height = 30)

  #field nomor hp
  Label(screen1, text = "Nomor HP", font = ("Helvetica", 15, "bold"), bg="white").place(x = 50, y = 400)
  phone_register = Entry(screen1, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  phone_register.place(x = 50, y = 430, width = 300, height = 30)

  #field alamat
  Label(screen1, text = "Alamat", font = ("Helvetica", 15, "bold"), bg="white").place(x = 450, y = 200)
  alamat_register = Entry(screen1, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  alamat_register.place(x = 450, y = 230, width = 300, height = 30)

  #field posisi
  Label(screen1, text = "Role", font = ("Helvetica", 15, "bold"), bg="white").place(x = 450, y = 300)
  role_register = Entry(screen1, font=("Helvetica", 15, "bold"), bg = "light grey", fg = "black")
  role_register.place(x = 450, y = 330, width = 300, height = 30)

  #button register
  Button(screen1, text = "DAFTAR", font=("Helvetica", 15, "bold"), bg = "cyan", fg = "black", command = register_user).place(x = 900, y = 315, height = 50, width = 160)

#fungsi actionzzzz
def register_user():
  username_info = username.get()
  password_info = password.get()

  file = open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_register.delete(0, END)
  password_register.delete(0, END)

  Label(screen1, text = "Berhasil terdaftar!", fg = "green" ,font = ("Helveica", 11)).pack()

def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_login.delete(0, END)
  password_login.delete(0, END)

  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        berhasil_login()
    else:
        password_salah()

  else:
        pengguna_salah()

#the ifs
def berhasil_login():
  Label(screen, text = "Berhasil login!", fg = "green" ,font = ("Helvetica", 13)).pack()

def password_salah():
  Label(screen, text = "Password yang anda masukkan salah!", fg = "green" ,font = ("Helvetica", 13)).pack()

def pengguna_salah():
  Label(screen, text = "Pengguna tidak ditemukan!", fg = "green" ,font = ("Helvetica", 13)).pack()
        
main_screen()
