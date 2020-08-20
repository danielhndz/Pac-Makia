# -*- coding: utf-8 -*-
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
from tkinter import messagebox
from Options_window import * 
import random
from coordenaties import *
from normalGame import *
from Board import *
from Automatic import*
import pygame

global rows 
global columns
        
def Graph(tablero_juego):
    listAd = {}
    for i in range (len(tablero_juego)):
        for j in range (len(tablero_juego[i])):
            if tablero_juego[i][j] != 1:
                temp = []
                if i-1 >= 0:
                    if tablero_juego[i-1][j] == 0:
                        temp.append((i-1,j))
                if j-1 >= 0:
                    if tablero_juego[i][j-1] == 0:
                        temp.append((i,j-1))
                if i+1 < len(tablero_juego):
                    if tablero_juego[i+1][j] == 0:
                        temp.append((i+1,j))
                if j+1 < len(tablero_juego[i]):
                    if tablero_juego[i][j+1] == 0:
                        temp.append((i,j+1))
                listAd [(i,j)] = temp
    
    return listAd    
    
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


def drawBoard(inputBoard, current, typeGame):
    if typeGame == "Coordenaties":
        give_coordenaties(inputBoard)
    elif typeGame == "Normal":
        normalgame(inputBoard)
    else:
        automaticGame(inputBoard)

def fullBoard(listxt,current, back, typeGame):
    inputBoard = []
    cont = 0
    while cont < len(listxt):
        for i in range(rows):
            temp = []
            for j in range(columns):
                if listxt[cont] == 'pacman' or listxt[cont].get()== '1' or listxt[cont].get() == '0' or listxt[cont].get()== 'f':
                    if listxt[cont]== 'pacman':
                        temp.append('pacman')
                    elif listxt[cont].get().isdigit():
                        temp.append(int(listxt[cont].get()))
                    else:
                        temp.append(listxt[cont].get())
                    cont+=1
                else:
                    messagebox.showerror("Board", "Only values ​​0, 1 and 'f' are accepted. Check te matrix values")
                    temp = []
                    break
            if temp == []:
                inputBoard = []
                break
            else:
                inputBoard.append(temp)
        if inputBoard == []:
            break
    if inputBoard != []:
        back.destroy()
        drawBoard(inputBoard, current, typeGame)
    
    

def Board(current, typeGame):
    messagebox.showwarning("Board", "Write 0 to represent a cookie, 1 for an obstacle and ' f ' to a ghost")
    windowb =   Toplevel()
    windowb.resizable(width=False, height=False)
    windowb.title("Pacman")
    x = 25*columns+60
    y = 25*rows+70
    windowb.configure(background="black",width=x, height=y)
    center(windowb)
    y1 = 15
    listxt = []
    for i in range(rows):
        x1 = 30
        for j in range(columns):
            if i == rows-1 and j==0:
                image = Image.open("Images/pacman1_2.png")
                photo = ImageTk.PhotoImage(image)
                l = Label(windowb,image=photo,bg="black")
                l.imagen=photo
                l.place(x=x1,y=y1)
                listxt.append('pacman')
            else:  
                txtval= Entry(windowb,font=("courier",12),width="2")
                listxt.append(txtval)
                txtval.place(x=x1,y=y1)
            x1+=25
        y1+=23
    btnAcept= Button(windowb,text="ACEPT", fg="White", bg="black", font=("courier",15), command = lambda : fullBoard(listxt,current, windowb, typeGame))
    k = x//2-85
    p = y1+15
    btnAcept.place(x=k,y=p)
    btnCncel= Button(windowb,text="CANCEL", fg="White", bg="black", font=("courier",15), command = lambda : close(windowb,current))
    k += 83
    btnCncel.place(x=k,y=p)
    windowb.mainloop()
    
    


def validateData(r, c, current1, option, current, typeGame):
    global rows
    rows = None
    global columns
    columns = None
    if r == "" or c == "":
        messagebox.showerror("Board", "You must fill out all the boxes")
    elif r.isdigit() and c.isdigit():
        r , c = int(r) , int(c)
        if r > 4 and r < 16 and  c > 4 and c < 16:
            rows = r
            columns = c
            current1.destroy()
            if option == 1:
                Board(current, typeGame)
            else:
                board = main_board(c,r)
                drawBoard(board, current, typeGame)
        else:
            messagebox.showerror("Board", "Enter numbers between 5 and 15")
    else:
         messagebox.showerror("Board", "Enter integer numbers between 5 and 15")

def close(current, back):
    current.destroy()
    back.deiconify()
        
def boardSize(option, current, typeGame):
    global windowboard 
    windowboard = Toplevel()
    windowboard.resizable(width=False, height=False)
    windowboard.title("Pacman")
    windowboard.configure(background="black",width="320", height="120")
    center(windowboard)
    labelrows = Label(windowboard,text="Rows: ",fg="White",bg=("black"),font=("courier",12))
    labelrows.place(x=10,y=10)
    txtrows= Entry(windowboard,font=("courier",12))
    txtrows.place(x=100,y=10)
    labelcolumns = Label(windowboard,text="Columns: ",fg="White",bg=("black"),font=("courier",12))
    labelcolumns.place(x=10,y=40)
    txtcolumns= Entry(windowboard,font=("courier",12))
    txtcolumns.place(x=100,y=40)
    btnAcept = Button(windowboard,text="ACEPT", fg="White", bg="black", font=("courier",15), command = lambda : validateData(txtrows.get(), txtcolumns.get(), windowboard, option, current, typeGame))
    btnAcept.place(x=70,y=75)
    btncancel = Button(windowboard,text="CANCEL", fg="White", bg="black", font=("courier",15), command = lambda : close(windowboard, current))
    btncancel.place(x=170,y=75)
    windowboard.mainloop()

def windowGame(current, typeGame):
    ##random 0, no random 1
    x = messagebox.askyesno(message="Do you want to get a random board?", title="Board")
    if x == True: 
        option = 0
        y = messagebox.askyesno(message="You want to set the size of the board random?", title="Board")
        if y == True:
             board = main_board()
             global rows
             global columns
             rows = len(board)
             columns = len(board[0])                
             drawBoard(board,current, typeGame)
        else:
            boardSize(option, current, typeGame)
    else:
        option = 1            
        boardSize(option, current, typeGame)
    
def show_windowGame(current, typeGame):
    current.iconify()
    windowGame(current, typeGame)

    
