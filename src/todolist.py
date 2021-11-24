# Penanggung jawab: Aindrea Rayhan 18219034
import sys
from tkinter import*
from PIL import Image, ImageTk
import os
from tkinter import ttk
import mysql.connector as mysql
import mariadb

# Modul Tampilkan Kondisi todolist
def Todolist():
    global root
    root = Tk()
    root.title("Tampilkan To-do List")
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

    # Tulisan "DAFTAR TODOLIST"
    DaftarlabelTitle = Label(root, text='TO-DO LIST', font=('helvetica',40,'bold'),bg='white',fg='Black', width=100, anchor='w').place(x=50,y=180)

    # Tampilan button Homie  
    Homie = Image.open('img\home.png')
    Homie.load()
    Homie = Homie.resize((100,100), Image.ANTIALIAS)
    HomiePI = ImageTk.PhotoImage(Homie)
    HomiePicture = Button(root, image=HomiePI,bg='lightgreen').place(x=1090,y=20,width=100,height=100)

    # Fungsi untuk buka window Edit Todolist
    def BukaEditTodolist():
        EditTodolist()
        root.destroy()

    # Tombol Edit Todolist
    EditBut = Image.open('img\EditPeralatan.png')
    EditBut.load()
    EditBut = EditBut.resize((220,70),Image.ANTIALIAS)
    EditButPI = ImageTk.PhotoImage(EditBut)
    EditButton = Button(root, image=EditButPI,command=BukaEditTodolist).place(x=960,y=170,width=220,height=65)
    
    # Frame untuk tabel

    table_frame = Frame(root)
    table_frame.place(x=150, y=250, width=1000, height=430)

    # Scrollbar di kanan
    scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL)
    scrollbar.pack( side = RIGHT, fill = Y )

    # setup treeview untuk tabel isi daftar todolist
    columns = (1,2,3,4,5,6)
    tree = ttk.Treeview(table_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
    tree.column(1,width=30)
    tree.pack(fill=BOTH,expand=1)
    tree.heading(1, text='ID')
    tree.heading(2, text='Username')
    tree.heading(3, text='Role')
    tree.heading(4, text='Nama Pekerjaan')
    tree.heading(5, text='Deskripsi')
    tree.heading(6, text='Status')

    tree.column(1, width=30)
    tree.column(2, width=50)
    tree.column(3 ,width=50)
    tree.column(4, width=100)
    tree.column(5, width=200)
    tree.column(6, width=50)

    # Style Treeview
    style = ttk.Style()
    style.configure("Treeview", font=('helvetica', 11), background="lightgrey",foreground="black",fieldbackground='dodgerblue3',rowheight=40)
    style.map("Treeview",background=[('selected','azure4')])

    # Connect ke Mariadb server untuk mengambil data pekerjaan
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
    cur.execute('SELECT IDPekerjaan, Username, Role, Nama_Pekerjaan, Deskripsi, Status FROM todolist')
    
    # Isi Treeview dengan data dari database
    i=1
    for (IDPekerjaan, Username, Role, Nama_Pekerjaan, Deskripsi, Status) in cur:
        tree.insert(parent='',index=i,text='',values=(IDPekerjaan, Username, Role, Nama_Pekerjaan, Deskripsi, Status))
        i=i+1
    
    # Pasang supaya scrollbar terhubung ke treeview
    scrollbar.config(command=tree.yview)

    # Paling akhir untuk infinite loop
    root.mainloop()

# Modul Edit Todolist
def EditTodolist():
    global root2
    root2 = Toplevel(root)
    root2.title("Edit To-do List")
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

    # Tulisan "EDIT TODOLIST"
    DaftarlabelTitle = Label(root2, text='EDIT TO-DO LIST', font=('helvetica',40),bg='white',fg='Black', width=100, anchor='w').place(x=50,y=180)

   # Tampilan button Homie  
    Homie = Image.open('img\home.png')
    Homie.load()
    Homie = Homie.resize((100,100), Image.ANTIALIAS)
    HomiePI = ImageTk.PhotoImage(Homie)
    HomiePicture = Button(root2, image=HomiePI,bg='lightgreen').place(x=1090,y=20,width=100,height=100)

    # Entry Box ID
    IDText = Label(root2, text='ID Pekerjaan', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=260)
    InputIDPekerjaan = Entry(root2,bd=5,font=('helvetica',15),bg='deepskyblue')
    InputIDPekerjaan.place(width=300,height=40,x=140,y=310)

    # Entry Box Username
    UsernameText = Label(root2, text='Username', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=380)
    InputUsername = Entry(root2,bd=5,font=('helvetica',15),bg='deepskyblue')
    InputUsername.place(width=300,height=40,x=140,y=430)

    # Entry Box Role
    RoleText = Label(root2, text='Role', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=140,y=500)
    InputRole = Entry(root2,bd=5,font=('helvetica',15),bg='deepskyblue')
    InputRole.place(width=300,height=40,x=140,y=550)

    # Entry Box Nama Pekerjaan
    NamaPekerjaanText = Label(root2, text='Nama Pekerjaan', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=550,y=260)
    InputNamaPekerjaan = Entry(root2,bd=5,font=('helvetica',15),bg='deepskyblue')
    InputNamaPekerjaan.place(width=300,height=40,x=550,y=310)

    # Entry Box Deskripsi
    DescText = Label(root2, text='Deskripsi', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=550,y=380)
    InputDesc = Entry(root2,bd=5,font=('helvetica',15),bg='deepskyblue')
    InputDesc.place(width=300,height=40,x=550,y=430)

    # Entry Box Status
    StatusText = Label(root2, text='Status', font=('helvetica',30),bg='white',fg='Black', width=100, anchor='w').place(x=550,y=500)
    InputStatus = Entry(root2,bd=5,font=('helvetica',15),bg='deepskyblue')
    InputStatus.place(width=300,height=40,x=550,y=550)
    
    # Function untuk tombol
    def FunctionAdd():
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
        Query = "INSERT INTO todolist VALUES (%d,%s,%s,%s,%s,%s)"
        data = (InputIDPekerjaan.get(),InputUsername.get(),InputRole.get(),InputNamaPekerjaan.get(),InputDesc.get(),InputStatus.get())
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
        Query = "UPDATE todolist SET Username=%s, Role=%s, Nama_Pekerjaan=%s, Deskripsi=%s, Status=%s WHERE IDPekerjaan=%d"
        data = (InputUsername.get(),InputRole.get(),InputNamaPekerjaan.get(),InputDesc.get(),InputStatus.get(),InputIDPekerjaan.get())
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
        Query = "DELETE FROM todolist WHERE IDPekerjaan=%d AND Nama_Pekerjaan=%s"
        data = (InputIDPekerjaan.get(),InputNamaPekerjaan.get())
        cur.execute(Query, data)
        conn.commit()
        root2.destroy()

    # Button Tambah
    Tambah = Button(root2, text='TAMBAH',font=('helvetica',30,'bold'),bg='springgreen',bd=5,fg='Black',command=FunctionAdd).place(x=1000,y=300,width=200,height=50)
    Update = Button(root2, text='UPDATE',font=('helvetica',30,'bold'),bg='lightblue',bd=5,fg='Black',command=FunctionUpdate).place(x=1000,y=420,width=200,height=50)
    Hapus = Button(root2, text='HAPUS',font=('helvetica',30,'bold'),bg='red',bd=5,fg='Black',command=FunctionDelete).place(x=1000,y=540,width=200,height=50)

    # infinite looping
    root2.mainloop()

# Run GUI
Todolist()