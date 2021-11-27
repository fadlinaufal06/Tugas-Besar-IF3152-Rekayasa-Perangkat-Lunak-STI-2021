# Penanggung jawab : Fadli Naufal Rahman 18219043

import sys
if "tkinter" not in sys.modules:
    from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import mysql.connector as mysql
import mariadb

def DaftarMenu():
    global root
    root = Tk()
    root.title("Tampilkan Daftar Menu")
    root.geometry('1270x690+0+0')
    root.config(bg='white')

    # Tampilan biru di atas
    Biru = Image.open("img\lightblue.png")
    Biru.load()
    Biru = Biru.resize((500,300), Image.ANTIALIAS)
    BiruPI = ImageTk.PhotoImage(Biru)
    Background_biru = Label(root, image=BiruPI, bg='deepskyblue').place(x=0,y=0,width=1500,height=150)

    # Tampilan atas MONITROS)
    FotoMonitros = Image.open("img\logo_monitros.png")
    FotoMonitros.load()
    FotoMonitros = FotoMonitros.resize((500,300), Image.ANTIALIAS)
    FotoMonitrosPI = ImageTk.PhotoImage(FotoMonitros)
    logoMonitros = Label(root, image=FotoMonitrosPI,bg='deepskyblue').place(x=0,y=0,width=450,height=150)

    # Tulisan "DAFTAR TO-DO LIST"
    DaftarlabelTitle = Label(root, text='DAFTAR MENU', font=('helvetica',40, 'bold'),bg='white',fg='Black', width=100, anchor='w').place(x=50,y=180)

    # Tampilan button Homie  
    Homie = Image.open('img\home.png')
    Homie.load()
    Homie = Homie.resize((100,100), Image.ANTIALIAS)
    HomiePI = ImageTk.PhotoImage(Homie)
    HomiePicture = Button(root, image=HomiePI,bg='lightgreen').place(x=1090,y=20,width=100,height=100)
    
    # Fungsi untuk buka window Edit Peralatan
    def BukaEditMenu():
        EditMenu()
        root.destroy()

    # Tombol Edit Menu
    EditBut = Image.open('img\EditMenu.png')
    EditBut.load()
    EditBut = EditBut.resize((220,70),Image.ANTIALIAS)
    EditButPI = ImageTk.PhotoImage(EditBut)
    EditButton = Button(root, image=EditButPI,command=BukaEditMenu).place(x=970,y=170,width=220,height=65)
    
    # Scrollbar di kanan
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )

    # setup treeview untuk tabel isi daftar peralatan
    columns = (1,2,3)
    tree = ttk.Treeview(root, height=10, columns=columns, show='headings')
    tree.column(1,width=30)
    tree.pack(side=BOTTOM, fill=Y,pady=20)
    tree.heading(1, text='ID')
    tree.heading(2, text='Nama Menu')
    tree.heading(3, text='Deskripsi')

    # Style Treeview
    style = ttk.Style()
    style.configure("Treeview", font=('helvetica', 11), background="lightgrey",foreground="black",fieldbackground='dodgerblue3',rowheight=40)
    style.map("Treeview",background=[('selected','azure4')])

    # Connect ke Mariadb server untuk mengambil data menu
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
    cur.execute('SELECT IDMenu, Nama_Menu, Deskripsi  FROM menu')

    # Isi Treeview dengan data dari database
    i=1
    for (IDMenu, Nama_Menu, Deskripsi) in cur:
        tree.insert(parent='',index=i,text='',values=(IDMenu,Nama_Menu,Deskripsi))
        i=i+1
    
    # Pasang supaya scrollbar terhubung ke treeview
    scrollbar.config( command = tree.yview )

    # Paling akhir untuk infinite loop
    root.mainloop()

# Modul Edit Peralatan
def EditMenu():
    global root2
    root2 = Toplevel(root)
    root2.title("Edit Menu")
    root2.geometry('1270x690+0+0')
    root2.config(bg='white')

    # Tampilan biru di atas
    Biru = Image.open("img\lightblue.png")
    Biru.load()
    Biru = Biru.resize((500,300), Image.ANTIALIAS)
    BiruPI = ImageTk.PhotoImage(Biru)
    Background_biru = Label(root2, image=BiruPI, bg='deepskyblue').place(x=0,y=0,width=1500,height=150)
    # Tampilan atas MONITROS)
    FotoMonitros = Image.open("img\logo_monitros.png")
    FotoMonitros.load()
    FotoMonitros = FotoMonitros.resize((500,300), Image.ANTIALIAS)
    FotoMonitrosPI = ImageTk.PhotoImage(FotoMonitros)
    logoMonitros = Label(root2, image=FotoMonitrosPI,bg='deepskyblue').place(x=0,y=0,width=450,height=150)  

    # Tulisan "EDIT MENU"
    DaftarlabelTitle = Label(root2, text='EDIT MENU', font=('helvetica',40, 'bold'),bg='white',fg='Black', width=100, anchor='w').place(x=50,y=180)

    # Tampilan button Homie  
    Homie = Image.open('img\home.png')
    Homie.load()
    Homie = Homie.resize((100,100), Image.ANTIALIAS)
    HomiePI = ImageTk.PhotoImage(Homie)
    HomiePicture = Button(root2, image=HomiePI,bg='lightgreen').place(x=1090,y=20,width=100,height=100)

    # Entry Box ID
    IDText = Label(root2, text='ID Menu', font=('helvetica',25),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=260)
    InputID = Entry(root2,bd=5, font=('helvetica',15),bg='deepskyblue')
    InputID.place(width=300,height=40,x=140,y=310)

    # Entry Box Nama
    NamaText = Label(root2, text='Nama Menu', font=('helvetica',25),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=380)
    InputNama = Entry(root2,bd=5, font=('helvetica',15), bg='deepskyblue')
    InputNama.place(width=300,height=40,x=140,y=430)

    # Entry Box Deskripsi
    TipeText = Label(root2, text='Deskripsi', font=('helvetica',25),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=500)
    InputDeskripsi = Entry(root2,bd=5, font=('helvetica',15), bg='deepskyblue')
    InputDeskripsi.place(width=300,height=40,x=140,y=550)

     # Function untuk tombol
    def FunctionTambah():
        # Connect to Mariadb
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="monitros"
        )
        # Get Cursor
        cur = conn.cursor()
        Query = "INSERT INTO menu VALUES (%d,%s,%s)"
        data = (InputID.get(),InputNama.get(),InputDeskripsi.get())
        cur.execute(Query, data)
        conn.commit()
        root2.destroy()
    def FunctionUpdate():
        # Connect to Mariadb
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="monitros"
        )
        # Get Cursor
        cur = conn.cursor()
        Query = "UPDATE menu SET Nama_Menu=%s, Deskripsi=%s, WHERE IDMenu=%d"
        data = (InputNama.get(),InputDeskripsi.get(),InputID.get())
        cur.execute(Query, data)
        conn.commit()
        root2.destroy()

    def FunctionDelete():
        # Connect to Mariadb
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="monitros"
        )
        # Get Cursor
        cur = conn.cursor()
        Query = "DELETE FROM menu WHERE IDMenu=%d AND Nama_Menu=%s"
        data = (InputID.get(),InputNama.get())
        cur.execute(Query, data)
        conn.commit()
        root2.destroy()

    # Button Tambah
    Tambah = Button(root2, text='TAMBAH',font=('helvetica',30, 'bold'),bg='springgreen',bd=5,fg='Black',command=FunctionTambah).place(x=550,y=300,width=200,height=50)
    Update = Button(root2, text='UPDATE',font=('helvetica',30, 'bold'),bg='lightblue',bd=5,fg='Black',command=FunctionUpdate).place(x=550,y=420,width=200,height=50)
    Hapus = Button(root2, text='HAPUS',font=('helvetica',30, 'bold'),bg='red',bd=5,fg='Black',command=FunctionDelete).place(x=550,y=540,width=200,height=50)
    # Paling Akhir
    root2.mainloop()



#Menjalankan GUI
DaftarMenu()
