# Penanggung Jawab testing: Kevin Kencana 18219050

import sys
from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import ttk
import mysql.connector as mysql
import mariadb
import pytest

def homescreen(screen):
    global screenhome
    screen.destroy()
    screenhome = Tk()
    return screenhome
def logout(screenhome):
    from login import home
    home(screenhome)
def home(layar):
    global screen
    layar.destroy()

def func_logout():
    try:
        screen = Tk()
        screenhome = homescreen(screen)
        logout(screenhome)
        return 'berhasil'
    except:
        return 'tidak berhasil'


def test_logout():
    assert (func_logout() == 'berhasil')
        
