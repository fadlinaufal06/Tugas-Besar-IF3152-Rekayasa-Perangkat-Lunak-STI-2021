# Penanggung Jawab testing: Kevin Kencana 18219050

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
    cur.execute('SELECT IDMenu, Nama_Menu, Deskripsi FROM menu')
    return cur.fetchall()

def tambah_menu(query,data):
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
        return 'berhasil'
    except:
        return 'tidak berhasil'

def test_connnection():
    nama_menu1 = Connect()
    assert (nama_menu1[0] == (1,'Nasi goreng','Isi sosis, ayam, bakso'))

def test_edit_normal():
    query = "INSERT INTO menu VALUES (%d,%s,%s)"
    data = (2,'Ayam Geprek','Nasi ambil sepuasnya')
    message = tambah_menu(query, data)
    assert (message == 'berhasil')

def test_edit_salah():
    query = "INSERT INTO menu VALUES (%d,%s,%s)"
    data = ('bukan angka','Nasi Uduk','Isi telor, tempe goreng, kacang')
    message = tambah_menu(query, data)
    assert (message == 'tidak berhasil')

def test_edit_tidaklengkap():
    query = "INSERT INTO menu VALUES (%d,%s,%s)"
    data = (3,None,'Refill sepuasnya')
    message = tambah_menu(query, data)
    assert (message == 'tidak berhasil')







