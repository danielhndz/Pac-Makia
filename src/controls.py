# -*- coding: utf-8 -*-
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
from Options_window import*


def close(current, root):
    current.destroy()
    root.deiconify()

def first(windowcont):
    image = Image.open("Images/background_mw.png")
    photo = ImageTk.PhotoImage(image)
    l = Label(windowcont,image=photo)
    l.imagen=photo
    l.place(x=-2,y=0)
    center(windowcont)

def second (windowcont, root):
    labelMiamor = Label(windowcont,text="» Daniel Hernández",fg="White",bg=("black"),font=("courier",8))
    labelMiamor.place(x=105,y=430)
    labelMe = Label(windowcont,text="» Angi Jiménez",fg="White",bg=("black"),font=("courier",8))
    labelMe.place(x=0,y=430)
    lblTipo = Label(windowcont,text="Type of game: ",fg="white",bg=("black"),font=("courier",15))
    lblTipo.place(x=40,y=135)
    menuTipo = ttk.Combobox(windowcont, font=("courier",10))
    menuTipo["values"] = ["Give coordenaties","Automatic game", "Normal game"]
    menuTipo.place(x=40,y=165)
    btnacept = Button(windowcont,text="ACEPT", fg="White", bg="black", font=("courier",15), command = lambda : different_controls(windowcont, menuTipo.get(), root))
    btnacept.place(x=235, y=150)
    btnback = Button(windowcont,text="BACK", fg="White", bg="black", font=("courier",15), command = lambda : close(windowcont, root))
    btnback.place(x=275, y=400)
    windowcont.mainloop()
    
    
def different_controls(windowcont, typeOfGame, root):
    first(windowcont)
    if typeOfGame == "Normal game": 
        image = Image.open("Images/controls.png")
        photo = ImageTk.PhotoImage(image)
        l = Label(windowcont,image=photo,bg="black")
        l.imagen=photo
        l.place(x=110,y=200)
        lblcont = Label(windowcont,text="Use the arrows to move the ",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=40,y=300)
        lblcont = Label(windowcont,text="character to up, down, left ",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=40,y=330)
        lblcont = Label(windowcont,text="and right.",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=40,y=360)
   
        
    elif typeOfGame == "Automatic game":
      
        lblcont = Label(windowcont,text="When you press the ",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=40,y=245)
        lblcont = Label(windowcont,text="-Automatic game- button,",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=40,y=275)
        lblcont = Label(windowcont,text="the game starts.",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=40,y=305)
        
    elif typeOfGame == "Give coordenaties":
        lblcont = Label(windowcont,text="You must enter the coordinate",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=30,y=245)
        lblcont = Label(windowcont,text="where you want the character",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=30,y=275)
        lblcont = Label(windowcont,text="to go.",fg="white",bg=("black"),font=("courier",12))
        lblcont.place(x=30,y=305)
    else:
        messagebox.showerror("Controls", "You must select a  option from menu.")
    second(windowcont, root)
        
    

def controls(root):
    global windowcont 
    windowcont = Toplevel(root)
    windowcont.resizable(width=False, height=False)
    root.iconify()
    windowcont.title("Pacman controls")
    windowcont.configure(background="black",width="350", height="450")
    first(windowcont)
    second(windowcont, root)
    
    
def show_controls(root):
    controls(root)


