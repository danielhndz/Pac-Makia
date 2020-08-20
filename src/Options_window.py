# -*- coding: utf-8 -*-
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from window_of_game import*

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def optionsWindow(root):
    global windowOpt 
    windowOpt = Toplevel(root)
    windowOpt.resizable(width=False, height=False)
    root.iconify()
    windowOpt.title("Pacman options")
    windowOpt.configure(background="black",width="350", height="450")
    image = Image.open("Images/background_mw.png")
    photo = ImageTk.PhotoImage(image)
    l = Label(windowOpt,image=photo)
    l.imagen=photo
    l.place(x=-2,y=0)
    center(windowOpt)
    btncoordenaties = Button(windowOpt,text="GIVE COORDENATIES", fg="White", bg="black", font=("courier",15), command = lambda : show_windowGame(windowOpt, "Coordenaties"))
    btncoordenaties.place(x=65,y=180)
    btnAutomatic = Button(windowOpt,text="AUTOMATIC GAME", fg="White", bg="black", font=("courier",15), command = lambda : show_windowGame(windowOpt, "Automatic"))
    btnAutomatic.place(x=83,y=240)
    btnNormal = Button(windowOpt,text="NORMAL GAME", fg="White", bg="black", font=("courier",15), command = lambda : show_windowGame(windowOpt, "Normal"))
    btnNormal.place(x=100,y=300)
    btnback = Button(windowOpt,text="BACK", fg="White", bg="black", font=("courier",15), command = lambda : close(windowOpt, root))
    btnback.place(x=145,y=360)
    labelMiamor = Label(windowOpt,text="» Daniel Hernández",fg="White",bg=("black"),font=("courier",8))
    labelMiamor.place(x=105,y=430)
    labelMe = Label(windowOpt,text="» Angi Jiménez",fg="White",bg=("black"),font=("courier",8))
    labelMe.place(x=0,y=430)
    windowOpt.mainloop()
    windowOpt.destroy()
    
    
def show_optionsWindow(root):
    optionsWindow(root)



  