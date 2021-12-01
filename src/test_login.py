# Penanggung Jawab testing: Rahmat Fabhian Aminuddin 18219055

import sys
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import mysql.connector as mysql
import mariadb
import pytest

#pytest buat login
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
    cur.execute("select * from data_user")
    return cur.fetchall()

def registrasilogin(query,data):
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
    regtest = Connect()
    assert (regtest[0] == ('abhifabhian','abhi','abhi fabhian',213123,'Tangerang','Owner'))

def test_registrasi():
    query = "INSERT INTO data_user VALUES (%s,%s,%s,%d,%s,%s)"
    data = ('sugino','sss123','sugino fabhian',22123,'Jakarta','Owner')
    message = registrasilogin(query, data)
    assert (message == 'berhasil')

def test_login():
    conn = mariadb.connect(
            user="root",
            password="",
            host="localhost",
            port=3306,
            database="monitros"
        )
    # Get Cursor
    try:
        cur = conn.cursor()
        message = cur.execute("SELECT * FROM data_user WHERE Username=%s and Password=%s",('abhifabhian','abhi'))
        assert (message == 'berhasil')
    except:
        return 'tidak berhasil'
