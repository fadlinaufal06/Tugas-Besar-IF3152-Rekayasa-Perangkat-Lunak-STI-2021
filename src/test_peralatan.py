# Penanggung Jawab testing: Fadli Naufal Rahman 18219043

import sys
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import mysql.connector as mysql
import mariadb
import pytest

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
    cur.execute('SELECT IDPeralatan, Nama_Peralatan, Tipe_Peralatan, Jumlah_Ideal, Jumlah_Peralatan, Kondisi FROM peralatan')
    return cur.fetchall()

def tambah_peralatan(query,data):
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
        #Query = "DELETE FROM peralatan WHERE IDPeralatan=%d AND Nama_Peralatan=%s"
        return 'berhasil'
    except:
        return 'tidak berhasil'

def test_connnection():
    nama_peralatan1 = Connect()
    assert (nama_peralatan1[0] == (1,'Piring','AlatMakan',200,170,'Butuh Beli Baru'))

def test_edit_normal():
    peralatan = Connect()
    query = "INSERT INTO peralatan VALUES (%d,%s,%s,%d,%d,%s)"
    data = (len(nama_peralatan[0]),'mangkok','alatmakan',12,11,'normal')
    message = tambah_peralatan(query, data)
    assert (message == 'berhasil')

def test_edit_salah():
    query = "INSERT INTO peralatan VALUES (%d,%s,%s,%d,%d,%s)"
    data = ('bukan angka','Piring putih','AlatMakan',200,170,'Butuh Beli Baru')
    message = tambah_peralatan(query, data)
    assert (message == 'tidak berhasil')

def test_edit_tidaklengkap():
    query = "INSERT INTO peralatan VALUES (%d,%s,%s,%d,%d,%s)"
    data = (1,None,'AlatMakan',200,170,'Butuh Beli Baru')
    message = tambah_peralatan(query, data)
    assert (message == 'tidak berhasil')







