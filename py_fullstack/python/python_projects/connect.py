#improting modules
from tkinter import *
import sqlite3 
import tkinter.ttk as ttk
import tkinter.messagebox as tkmessagebox 

root =Tk()
root.title("contact")
width =700
height =400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width,height, x, y))
root.resizable(0, 0)
root.config(bg="#00ff00")


