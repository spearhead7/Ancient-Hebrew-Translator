import csv

import tkinter as tk

import sqlite3
from tkinter import Menu
from tkinter import ttk
from tkinter.messagebox import showinfo
import re

root = tk.Tk()

root.title("Hebrew Translator")

w = 1000 # width for the Tk window
h = 650 # height for the Tk window

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the root window
x = (ws/5) - (w/5)
y = (hs/4) - (h/4)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# %%
def searchverse(event=None):
    
    searchinput = searchversetxt.get()
    
    if len(searchinput) < 6:
      print("incorrect search entry")
      return

    searchinput = searchinput.replace(":", ".")
    searchinput = searchinput.capitalize()
    
    # split search string into parts for variable verse word data
    # searchinput = (re.split(r'\s',searchinput))
    # searchinput.append("-")
    # searchinput[0] = searchinput[0] + '.'
    # searchstring = ''.join(searchinput)
    
    # print("converted entry:", searchstring)

    searchstring = searchinput 

    try:
       
      con = sqlite3.connect('hebrewdata.db')
      cursor = con.cursor()
      print("Database successfully connected to SQLite")

      sql_select_query ="""SELECT * from hebrewdata where Ref LIKE ?"""

      cursor.execute(sql_select_query, (searchstring,))
      verse = cursor.fetchall()
      print("Reading single verse ", searchstring)
      
      if len(verse) == 0:
         print (searchstring + " not found!")
         readerlabel.config(text = "No results")
         hebrewtxt.config(text = "No results")
      else: 
         print(verse)
         # english column 1, hebrew columns 2-7
         engwords = []
         hebwords =[]
         for row in verse:
            for i in row:
               ['' if i is None else i for i in row]
   
            engwords.append(row[1])
            hebwords.append(row[2])
            hebwords.append(row[3])
            hebwords.append(row[4])
            hebwords.append(row[5])
            hebwords.append(row[6])
            hebwords.append(row[7])
            readerlabel.config(text=engwords)
            hebrewtxt.config(text=hebwords)
                      
      cursor.close()

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        if con:
            con.close()

def searchheb (event=None):
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Search")
   button.pack()
def searcheng (event=None):
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Search")
   button.pack()
def searchmorph (event=None):
   filewin = tk.Toplevel(root)
   button = Button(filewin, text="Search")
   button.pack()
def searchstrong (event=None):
   filewin = tk.Toplevel(root)
   button = tk.Button(filewin, text="Search")
   button.pack()
def donothing():
   filewin = tk.Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
# open search window function
def open_searchwindow():
    global searchversetxt
    global searchhebtxt
    global searchengtxt
    global searchmorphtxt
    global searchstrongtxt
    
    searchwindow = tk.Toplevel(root)
    searchwindow.config(menu=menubar)
    searchwindow.title("Search")
    searchwindow.geometry ('280x170+1100+50')

    srchverselbl = tk.Label(searchwindow, text="Reference:", padx=5, pady=5, font=("arial", 12))
    srchverselbl.grid(column=0, row=0)
    srchheblbl = tk.Label(searchwindow, text="Search Hebrew:", padx=5, pady=5, font=("arial", 12))
    srchheblbl.grid(column=0, row=1)
    srchenglbl = tk.Label(searchwindow, text="Search English:", padx=5, pady=5, font=("arial", 12))
    srchenglbl.grid(column=0, row=2)
    srchmorphlbl = tk.Label(searchwindow, text="Search Morphology:", padx=5, pady=5, font=("arial", 12))
    srchmorphlbl.grid(column=0, row=3)
    srchstronglbl = tk.Label(searchwindow, text="Search Strong's #:", padx=5, pady=5, font=("arial", 12))
    srchstronglbl.grid(column=0, row=4)

    searchversetxt = tk.Entry(searchwindow, width=14)
    searchversetxt.grid(column=1, row=0)
    searchversetxt.focus()
    searchversetxt.bind('<Return>', searchverse)

    searchhebtxt = tk.Entry(searchwindow, width=14)
    searchhebtxt.grid(column=1, row=1)
    searchhebtxt.focus()
    searchhebtxt.bind('<Return>', searchheb)

    searchengtxt = tk.Entry(searchwindow, width=14)
    searchengtxt.grid(column=1, row=2)
    searchengtxt.focus()
    searchengtxt.bind('<Return>', searcheng)

    searchmorphtxt = tk.Entry(searchwindow, width=14)
    searchmorphtxt.grid(column=1, row=3)
    searchmorphtxt.focus()
    searchmorphtxt.bind('<Return>', searchmorph)

    searchstrongtxt = tk.Entry(searchwindow, width=14)
    searchstrongtxt.grid(column=1, row=4)
    searchstrongtxt.focus()
    searchstrongtxt.bind('<Return>', searchstrong)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

windowmenu = Menu(menubar, tearoff=0)
windowmenu.add_command(label="Search...", command=open_searchwindow)
menubar.add_cascade(label="Windows", menu=windowmenu)

root.config(menu=menubar)

# create all of the main containers
top_frame = tk.Frame(root, bg='white', width=450, height=150, borderwidth=1, relief="groove", padx=10, pady=10)
main = tk.Frame(root, borderwidth=1, relief="groove", bg='gray', width=50, height=40, padx=3, pady=3)
bottom_frame = tk.Frame(root, bg='gray', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
top_frame.grid(row=0, sticky="ew")
main.grid(row=1, sticky="nsew")
bottom_frame.grid(row=3, sticky="ew")

# create the center widgets
main.grid_rowconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)

readerlabel = tk.Label(top_frame, bg="white", fg="black", text="reader area", font=("Garamond", 20))
readerlabel.pack(padx=5, pady=15, side=tk.LEFT)

hebrewtxt = tk.Label(main, text="אֱלֹהִים מְרַחֶפֶת", border=1, bg="#bdbdbd", fg="black", font=("Times New Roman", 30))
hebrewtxt.pack(padx=15, pady=15, side=tk.TOP, anchor='ne')

open_searchwindow()



root.mainloop()
# %%
