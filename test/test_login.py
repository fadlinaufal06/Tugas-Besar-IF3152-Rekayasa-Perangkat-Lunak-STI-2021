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
    cur.execute("select * from data_user where Username=%s and Password=%s")
    return cur.fetchall()

def test_registrasi(query,data):
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
