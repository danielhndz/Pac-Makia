from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from Options_window import *
from controls import *    
    
def MainWindow():
    global window 
    window = Tk()
    window.resizable(width=False, height=False)
    window.title("Pacman")
    window.configure(background="black",width="350", height="390")
    image = Image.open("Images/background_mw.png")
    photo = ImageTk.PhotoImage(image)
    l = Label(window,image=photo)
    l.imagen=photo
    l.place(x=-2,y=0)
    center(window)
    btnStart = Button(window,text="START GAME", fg="White", bg="black", font=("courier",15), command = lambda : show_optionsWindow(window))
    btnStart.place(x=105,y=180)
    btnControls = Button(window,text="CONTROLS", fg="White", bg="black", font=("courier",15), command = lambda : show_controls(window))
    btnControls.place(x=115,y=240)
    btnback = Button(window,text="CLOSE", fg="White", bg="black", font=("courier",15), command = lambda : window.destroy())
    btnback.place(x=130,y=300)
    labelMiamor = Label(window,text="» Daniel Hernández",fg="White",bg=("black"),font=("courier",8))
    labelMiamor.place(x=105,y=370)
    labelMe = Label(window,text="» Angi Jiménez",fg="White",bg=("black"),font=("courier",8))
    labelMe.place(x=0,y=370)
    window.mainloop()
    
def show():
    MainWindow()
show()
