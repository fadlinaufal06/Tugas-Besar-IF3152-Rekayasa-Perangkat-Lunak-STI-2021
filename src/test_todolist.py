# Penanggung Jawab testing: Aindrea Rayhan 18219034

import sys
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import mysql.connector as mysql
import mariadb
import pytest
import todolist


def Connect():
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
    return cur.fetchall()

def tambah_pekerjaan(query,data):
    conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="monitros"
        )
    # Get Cursor
    cur = conn.cursor()
    try:
        cur.execute(query, data)
        conn.commit()
        #Query = "DELETE FROM menu WHERE IDMenu=%d AND Nama_Menu=%s"
        #Data = (data[0],data[1])
        #cur.execute(Query, Data)
        #conn.commit()
        return 'berhasil'
    except:
        return 'tidak berhasil'

def test_connnection():
    nama_pekerjaan1 = Connect()
    assert (nama_pekerjaan1[0] == (1,'arga34','Karyawan', 'Rekap Penjualan', 'Mengecek ulang dan merekap hasil penjualan', 'Belum Dilakukan'))

def test_edit_normal():
    todolist = Connect()
    query = "INSERT INTO todolist VALUES (%d,%s,%s,%s,%s,%s)"
    data = (len(todolist[0]),'brunofernandes','Karyawan', 'Membersihkan lantai', 'Sapu dan pel lantai', 'Sudah dilakukan') #Pakai len(todolist[0]) agar pytest bisa dijalan berkali-kali
    message = tambah_pekerjaan(query, data)
    assert (message == 'berhasil')

def test_edit_salah():
    query = "INSERT INTO todolist VALUES (%d,%s,%s,%s,%s,%s)"
    data = ('bukan angka','siapacoba','Karyawan','Ngegabut','Ngapain aja bebas','Selalu dilakukan')
    message = tambah_pekerjaan(query, data)
    assert (message == 'tidak berhasil')

def test_edit_tidaklengkap():
    query = "INSERT INTO todolist VALUES (%d,%s,%s,%s,%s,%s)"
    data = (3,'brunofernandes','Karyawan',None,'rekap dan verifikasi penjualan','Belum dilakukan')
    message = tambah_pekerjaan(query, data)
    assert (message == 'tidak berhasil')







