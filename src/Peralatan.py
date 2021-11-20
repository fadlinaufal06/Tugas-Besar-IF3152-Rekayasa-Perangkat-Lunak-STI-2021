# Penanggung jawab: Kevin Kencana 18219050
import sys
if "tkinter" not in sys.modules:
    from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import mysql.connector as mysql
import mariadb

# Modul Tampilkan Kondisi Peralatan
def KondisiPeralatan():
    global root
    root = Tk()
    root.title("Tampilkan Peralatan")
    root.geometry('1270x690+0+0')
    root.resizable(0,0)
    root.config(bg='white')
    
    # Tampilan biru di atas
    Biru = Image.open(".\img\lightblue.png")
    Biru.load()
    Biru = Biru.resize((500,300), Image.ANTIALIAS)
    BiruPI = ImageTk.PhotoImage(Biru)
    Background_biru = Label(root, image=BiruPI, bg='deepskyblue').place(x=0,y=0,width=1500,height=150)

    # Tampilan atas MONITROS)
    FotoMonitros = Image.open(".\img\logo monitros.png")
    FotoMonitros.load()
    FotoMonitros = FotoMonitros.resize((500,300), Image.ANTIALIAS)
    FotoMonitrosPI = ImageTk.PhotoImage(FotoMonitros)
    logoMonitros = Label(root, image=FotoMonitrosPI,bg='deepskyblue').place(x=0,y=0,width=450,height=150)

    # Tulisan "DAFTAR PERALATAN"
    DaftarlabelTitle = Label(root, text='DAFTAR PERALATAN', font=('helvetica',40),bg='white',fg='Black', width=100, anchor='w').place(x=50,y=180)

    # Tampilan gambar profile 
    Profile = Image.open('.\img\Profile.png')
    Profile.load()
    Profile = Profile.resize((160,100), Image.ANTIALIAS)
    ProfilePI = ImageTk.PhotoImage(Profile)
    ProfilePicture = Label(root, image=ProfilePI,bg='deepskyblue').place(x=1060,y=20,width=110,height=100)

    # Fungsi untuk buka window Edit Peralatan
    def BukaEditPeralatan():
        EditPeralatan()
        root.destroy()

    # Tombol Edit peralatan
    EditBut = Image.open('.\img\EditPeralatan.png')
    EditBut.load()
    EditBut = EditBut.resize((220,70),Image.ANTIALIAS)
    EditButPI = ImageTk.PhotoImage(EditBut)
    EditButton = Button(root, image=EditButPI,command=BukaEditPeralatan).place(x=960,y=170,width=220,height=65)
    
    # Scrollbar di kanan
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )

    # setup treeview untuk tabel isi daftar peralatan
    columns = (1,2,3,4,5,6)
    tree = ttk.Treeview(root, height=10, columns=columns, show='headings')
    tree.column(1,width=30)
    tree.pack(side=BOTTOM, fill=Y,pady=20)
    tree.heading(1, text='ID')
    tree.heading(2, text='Nama Peralatan')
    tree.heading(3, text='Tipe Peralatan')
    tree.heading(4, text='Jumlah Ideal')
    tree.heading(5, text='Jumlah Peralatan')
    tree.heading(6, text='Kondisi')

    # Style Treeview
    style = ttk.Style()
    style.configure("Treeview",background="dodgerblue3",foreground="black",fieldbackground='dodgerblue3',rowheight=40)
    style.map("Treeview",background=[('selected','azure4')])

    # Connect ke Mariadb server untuk mengambil data peralatan
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="peralatan"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    cur.execute('SELECT IDPeralatan, Nama_Peralatan, Tipe_Peralatan, Jumlah_Ideal, Jumlah_Peralatan, Kondisi FROM peralatan')
    
    # Isi Treeview dengan data dari database
    i=1
    for (IDPeralatan, Nama_Peralatan, Tipe_Peralatan, Jumlah_Ideal, Jumlah_Peralatan, Kondisi) in cur:
        tree.insert(parent='',index=i,text='',values=(IDPeralatan,Nama_Peralatan,Tipe_Peralatan,Jumlah_Ideal,Jumlah_Peralatan,Kondisi))
        i=i+1
    
    # Pasang supaya scrollbar terhubung ke treeview
    scrollbar.config( command = tree.yview )

    # Paling akhir untuk infinite loop
    root.mainloop()

# Modul Edit Peralatan
def EditPeralatan():
    global root2
    root2 = Toplevel(root)
    root2.title("Edit Peralatan")
    root2.geometry('1270x690+0+0')
    root2.resizable(0,0)
    root2.config(bg='white')

    # Tampilan biru di atas
    Biru = Image.open(".\img\lightblue.png")
    Biru.load()
    Biru = Biru.resize((500,300), Image.ANTIALIAS)
    BiruPI = ImageTk.PhotoImage(Biru)
    Background_biru = Label(root2, image=BiruPI, bg='deepskyblue').place(x=0,y=0,width=1500,height=150)
    # Tampilan atas MONITROS)
    FotoMonitros = Image.open(".\img\logo monitros.png")
    FotoMonitros.load()
    FotoMonitros = FotoMonitros.resize((500,300), Image.ANTIALIAS)
    FotoMonitrosPI = ImageTk.PhotoImage(FotoMonitros)
    logoMonitros = Label(root2, image=FotoMonitrosPI,bg='deepskyblue').place(x=0,y=0,width=450,height=150)  

    # Tulisan "EDIT PERALATAN"
    DaftarlabelTitle = Label(root2, text='EDIT PERALATAN', font=('helvetica',40),bg='white',fg='Black', width=100, anchor='w').place(x=50,y=180)

    # Tampilan gambar profile 
    Profile = Image.open('.\img\Profile.png')
    Profile.load()
    Profile = Profile.resize((160,100), Image.ANTIALIAS)
    ProfilePI = ImageTk.PhotoImage(Profile)
    ProfilePicture = Label(root2, image=ProfilePI,bg='deepskyblue').place(x=1060,y=20,width=110,height=100)

    # Entry Box ID
    IDText = Label(root2, text='ID Peralatan', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=260)
    InputID = Entry(root2,bd=5,bg='deepskyblue')
    InputID.place(width=300,height=40,x=140,y=310)

    # Entry Box Nama
    NamaText = Label(root2, text='Nama Peralatan', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=380)
    InputNama = Entry(root2,bd=5,bg='deepskyblue')
    InputNama.place(width=300,height=40,x=140,y=430)

    # Entry Box Tipe
    TipeText = Label(root2, text='Tipe Peralatan', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=500)
    InputTipe = Entry(root2,bd=5,bg='deepskyblue')
    InputTipe.place(width=300,height=40,x=140,y=550)

    # Entry Box Jumlah Ideal
    IdealText = Label(root2, text='Jumlah Ideal', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=550,y=260)
    InputIdeal = Entry(root2,bd=5,bg='deepskyblue')
    InputIdeal.place(width=300,height=40,x=550,y=310)

    # Entry Box Jumlah Peralatan
    JlhText = Label(root2, text='Jumlah Peralatan', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=550,y=380)
    InputJlh = Entry(root2,bd=5,bg='deepskyblue')
    InputJlh.place(width=300,height=40,x=550,y=430)

    # Entry Box Kondisi
    KondisiText = Label(root2, text='Kondisi', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=550,y=500)
    InputKondisi = Entry(root2,bd=5,bg='deepskyblue')
    InputKondisi.place(width=300,height=40,x=550,y=550)
    
    # Function untuk tombol
    def FunctionTambah():
        # Connect to Mariadb
        conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="peralatan"
        )
        # Get Cursor
        cur = conn.cursor()
        Query = "INSERT INTO peralatan VALUES (%d,%s,%s,%d,%d,%s)"
        data = (InputID.get(),InputNama.get(),InputTipe.get(),InputIdeal.get(),InputJlh.get(),InputKondisi.get())
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
            database="peralatan"
        )
        # Get Cursor
        cur = conn.cursor()
        Query = "UPDATE peralatan SET Nama_Peralatan=%s, Tipe_Peralatan=%s,Jumlah_Ideal=%d,Jumlah_Peralatan=%d,Kondisi=%s WHERE IDPeralatan=%d"
        data = (InputNama.get(),InputTipe.get(),InputIdeal.get(),InputJlh.get(),InputKondisi.get(),InputID.get())
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
            database="peralatan"
        )
        # Get Cursor
        cur = conn.cursor()
        Query = "DELETE FROM peralatan WHERE IDPeralatan=%d AND Nama_Peralatan=%s"
        data = (InputID.get(),InputNama.get())
        cur.execute(Query, data)
        conn.commit()
        root2.destroy()

    # Button Tambah
    Tambah = Button(root2, text='TAMBAH!',font=('helvetica',30),bg='springgreen',bd=5,fg='Black',command=FunctionTambah).place(x=1000,y=300,width=200,height=50)
    Update = Button(root2, text='UPDATE!',font=('helvetica',30),bg='lightblue',bd=5,fg='Black',command=FunctionUpdate).place(x=1000,y=420,width=200,height=50)
    Hapus = Button(root2, text='HAPUS!',font=('helvetica',30),bg='red',bd=5,fg='Black',command=FunctionDelete).place(x=1000,y=540,width=200,height=50)
    # Paling Akhir
    root2.mainloop()

# Jalanin GUI
KondisiPeralatan()
