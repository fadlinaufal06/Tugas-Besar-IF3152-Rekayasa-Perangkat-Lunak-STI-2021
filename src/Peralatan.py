# Penanggung jawab: Kevin Kencana 18219050
import sys
if "tkinter" not in sys.modules:
    from tkinter import *
from PIL import Image, ImageTk
import os


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
    #Background_biru.image=BiruPI
    # Tampilan atas MONITROS)
    FotoMonitros = Image.open(".\img\logo monitros.png")
    FotoMonitros.load()
    FotoMonitros = FotoMonitros.resize((500,300), Image.ANTIALIAS)
    FotoMonitrosPI = ImageTk.PhotoImage(FotoMonitros)
    logoMonitros = Label(root, image=FotoMonitrosPI,bg='deepskyblue').place(x=0,y=0,width=450,height=150)
    #logoMonitros.image=FotoMonitrosPI

    # Tulisan "DAFTAR PERALATAN"
    DaftarlabelTitle = Label(root, text='DAFTAR PERALATAN', font=('helvetica',40),bg='white',fg='Black', width=100, anchor='w').place(x=50,y=180)

    # Tampilan gambar profile 
    Profile = Image.open('.\img\Profile.png')
    Profile.load()
    Profile = Profile.resize((160,100), Image.ANTIALIAS)
    ProfilePI = ImageTk.PhotoImage(Profile)
    ProfilePicture = Label(root, image=ProfilePI,bg='deepskyblue').place(x=1060,y=20,width=110,height=100)

    def BukaEditPeralatan():
        EditPeralatan()
        root.destroy()

    def multiple_yview(*args):
        mylistID.yview(*args)
        mylistNama.yview(*args)
        mylistTipe.yview(*args)
        mylistIdeal.yview(*args)
        mylistJlh.yview(*args)
        mylistKondisi.yview(*args)

    # Tombol Edit peralatan
    EditBut = Image.open('.\img\EditPeralatan.png')
    EditBut.load()
    EditBut = EditBut.resize((220,70),Image.ANTIALIAS)
    EditButPI = ImageTk.PhotoImage(EditBut)
    EditButton = Button(root, image=EditButPI,command=BukaEditPeralatan).place(x=960,y=170,width=220,height=65)

    # Baris paling atas tabel peralatan
    ID = Label(root, text='ID',bg='azure2',font=('helvetica',20,'bold')).place(x=80,y=267,width=48,height=55)
    Nama = Label(root, text='Nama',bg='azure2',font=('helvetica',20,'bold')).place(x=125,y=267,width=160,height=55)
    Tipe = Label(root, text='Tipe',bg='azure2',font=('helvetica',20,'bold')).place(x=280,y=267,width=200,height=55)
    Jlh_Ideal = Label(root, text='Jumlah Ideal',bg='azure2',font=('helvetica',20,'bold')).place(x=477,y=267,width=180,height=55)
    Jlh_Alat = Label(root, text='Jumlah Peralatan',bg='azure2',font=('helvetica',20,'bold')).place(x=656,y=267,width=243,height=55)
    Kondisi = Label(root, text='Kondisi',bg='azure2',font=('helvetica',20,'bold')).place(x=897,y=267,width=243,height=55)
    # Daftar Peralatan
    scrollbar = Scrollbar(root)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylistID = Listbox(root, yscrollcommand = scrollbar.set,bd=1,width=3, bg='dodgerblue3', font=('helvetica',20))
    mylistID.insert(1,"1")
    mylistID.insert(2,"2")
    mylistID.insert(3,"3")
    mylistID.insert(4,"4")
    mylistID.insert(5,"5")
    mylistID.insert(6,"6")
    mylistID.insert(7,"7")
    mylistID.insert(8,"8")
    mylistID.insert(9,"9")
    mylistID.insert(10,"10")
    mylistID.insert(11,"11")
    mylistID.insert(12,"12")
    mylistID.insert(13,"13")
    mylistID.insert(14,"14")
    mylistID.insert(15,"15")
    mylistID.insert(16,"16")
    mylistID.insert(17,"17")
    mylistID.insert(18,"18")
    mylistID.place(x=80,y=320)

    mylistNama = Listbox(root, yscrollcommand = scrollbar.set,width=11, bg='dodgerblue3',font=('helvetica',20))
    mylistNama.insert(1,"Piring")
    mylistNama.insert(2,"Sendok")
    mylistNama.insert(3,"Garpu")
    mylistNama.insert(4,"Sumpit")
    mylistNama.insert(5,"Mangkok")
    mylistNama.insert(6,"Burner")
    mylistNama.insert(7,"Tong")
    mylistNama.insert(8,"Gunting")
    mylistNama.insert(9,"Gelas")
    mylistNama.insert(10,"Pitcher")
    mylistNama.insert(11,"Sapu")
    mylistNama.insert(12,"Pel")
    mylistNama.insert(13,"Kain Lap")
    mylistNama.insert(14,"Kotak Tissue")
    mylistNama.insert(15,"Condament")
    mylistNama.insert(16,"Tong Sampah")
    mylistNama.insert(17,"Tray")
    mylistNama.insert(18,"Menu")
    mylistNama.place(x=125,y=320)

    mylistTipe = Listbox(root, yscrollcommand = scrollbar.set,width=13, bg='dodgerblue3',font=('helvetica',20))
    mylistTipe.insert(1,"AlatMakan")
    mylistTipe.insert(2,"AlatMakan")
    mylistTipe.insert(3,"AlatMakan")
    mylistTipe.insert(4,"AlatMakan")
    mylistTipe.insert(5,"AlatMakan")
    mylistTipe.insert(6,"AlatMeja")
    mylistTipe.insert(7,"AlatMakan")
    mylistTipe.insert(8,"AlatMakan")
    mylistTipe.insert(9,"AlatMakan")
    mylistTipe.insert(10,"AlatWaiter")
    mylistTipe.insert(11,"AlatKebersihan")
    mylistTipe.insert(12,"AlatKebersihan")
    mylistTipe.insert(13,"AlatKebersihan")
    mylistTipe.insert(14,"AlatMeja")
    mylistTipe.insert(15,"AlatMeja")
    mylistTipe.insert(16,"AlatMeja")
    mylistTipe.insert(17,"AlatWaiter")
    mylistTipe.insert(18,"AlatMeja")
    mylistTipe.place(x=280,y=320)

    mylistIdeal = Listbox(root, yscrollcommand = scrollbar.set,width=12, bg='dodgerblue3',font=('helvetica',20))
    mylistIdeal.insert(1,"200")
    mylistIdeal.insert(2,"200")
    mylistIdeal.insert(3,"100")
    mylistIdeal.insert(4,"100")
    mylistIdeal.insert(5,"150")
    mylistIdeal.insert(6,"15")
    mylistIdeal.insert(7,"30")
    mylistIdeal.insert(8,"15")
    mylistIdeal.insert(9,"80")
    mylistIdeal.insert(10,"10")
    mylistIdeal.insert(11,"10")
    mylistIdeal.insert(12,"10")
    mylistIdeal.insert(13,"20")
    mylistIdeal.insert(14,"45")
    mylistIdeal.insert(15,"30")
    mylistIdeal.insert(16,"6")
    mylistIdeal.insert(17,"8")
    mylistIdeal.insert(18,"15")
    mylistIdeal.place(x=474,y=320)

    mylistJlh = Listbox(root, yscrollcommand = scrollbar.set,width=16, bg='dodgerblue3',font=('helvetica',20))
    mylistJlh.insert(1,"170")
    mylistJlh.insert(2,"130")
    mylistJlh.insert(3,"70")
    mylistJlh.insert(4,"90")
    mylistJlh.insert(5,"145")
    mylistJlh.insert(6,"15")
    mylistJlh.insert(7,"30")
    mylistJlh.insert(8,"15")
    mylistJlh.insert(9,"75")
    mylistJlh.insert(10,"9")
    mylistJlh.insert(11,"10")
    mylistJlh.insert(12,"10")
    mylistJlh.insert(13,"14")
    mylistJlh.insert(14,"20")
    mylistJlh.insert(15,"29")
    mylistJlh.insert(16,"6")
    mylistJlh.insert(17,"8")
    mylistJlh.insert(18,"15")
    mylistJlh.place(x=656,y=320)

    mylistKondisi = Listbox(root, yscrollcommand = scrollbar.set,width=16, bg='dodgerblue3',font=('helvetica',20))
    mylistKondisi.insert(1,"Butuh Beli Baru")
    mylistKondisi.insert(2,"Butuh Beli Baru")
    mylistKondisi.insert(3,"Butuh Beli Baru")
    mylistKondisi.insert(4,"Aman")
    mylistKondisi.insert(5,"Aman")
    mylistKondisi.insert(6,"Aman")
    mylistKondisi.insert(7,"Aman")
    mylistKondisi.insert(8,"Aman")
    mylistKondisi.insert(9,"Aman")
    mylistKondisi.insert(10,"Aman")
    mylistKondisi.insert(11,"Aman")
    mylistKondisi.insert(12,"Aman")
    mylistKondisi.insert(13,"Butuh Beli Baru")
    mylistKondisi.insert(14,"Butuh Beli Baru")
    mylistKondisi.insert(15,"Aman")
    mylistKondisi.insert(16,"Aman")
    mylistKondisi.insert(17,"Aman")
    mylistKondisi.insert(18,"Aman")
    mylistKondisi.place(x=897,y=320)

    # Configuration si Scrollbar
    scrollbar.config( command = multiple_yview )
    # Paling Akhir
    root.mainloop()

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
        root2.destroy()
    def FunctionUpdate():
        root2.destroy()
    def FunctionDelete():
        root2.destroy()

    # Button Tambah
    Tambah = Button(root2, text='TAMBAH!',font=('helvetica',30),bg='springgreen',bd=5,fg='Black',command=FunctionTambah).place(x=1000,y=300,width=200,height=50)
    Update = Button(root2, text='UPDATE!',font=('helvetica',30),bg='lightblue',bd=5,fg='Black',command=FunctionUpdate).place(x=1000,y=420,width=200,height=50)
    Hapus = Button(root2, text='HAPUS!',font=('helvetica',30),bg='red',bd=5,fg='Black',command=FunctionDelete).place(x=1000,y=540,width=200,height=50)
    # Paling Akhir
    root2.mainloop()



KondisiPeralatan()
