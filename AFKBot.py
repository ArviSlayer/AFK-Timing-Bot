import time
from  tkinter import *
import tkinter
from tkinter import ttk
import random
liste = ['w','a','s','d']
import keyboard
pencere = tkinter.Tk()
pencere.geometry("500x300")
pencere.resizable(0,0)
pencere.title("ArviS | AFK Bot")
icon = PhotoImage(file="icon.png")
pencere.iconphoto(False,icon)
checkbutton = IntVar()

def afkKal():
    checker = checkbutton.get()
    if checker==1:
        liste.append('space')
        x = random.choice(liste)
        y = random.choice(liste)
        z = random.choice(liste)
        keyboard.press(x)
        keyboard.press(x)
        keyboard.press(y)
        keyboard.press(y)
        keyboard.press(z)
        keyboard.press(z)
        time.sleep(1)
        keyboard.release(x)
        keyboard.release(y)
        keyboard.release(z)
    else:
        if 'space' in liste:
            liste.remove('space')
            x = random.choice(liste)
            y = random.choice(liste)
            z = random.choice(liste)
            keyboard.press(x)
            keyboard.press(x)
            keyboard.press(y)
            keyboard.press(y)
            keyboard.press(z)
            keyboard.press(z)
            time.sleep(1)
            keyboard.release(x)
            keyboard.release(y)
            keyboard.release(z)
        else:
            x = random.choice(liste)
            y = random.choice(liste)
            z = random.choice(liste)
            keyboard.press(x)
            keyboard.press(x)
            keyboard.press(y)
            keyboard.press(y)
            keyboard.press(z)
            keyboard.press(z)
            time.sleep(1)
            keyboard.release(x)
            keyboard.release(y)
            keyboard.release(z)


    global loop
    loop = pencere.after(3000,afkKal)

def baslat():
    time.sleep(3)
    afkKal()

def durdur():
    pencere.after_cancel(loop)
foto = PhotoImage(file="icon.png")
etiket = Label(pencere,image=foto).place(x=0,y=0)

buton = ttk.Button(pencere,text="AFK Modunu | Başlat",command=baslat).place(x=180,y=80,width=150,height=40)
buton2 = ttk.Button(pencere,text="AFK Modunu | Durdur",command=durdur).place(x=180,y=140,width=150,height=40)
check = ttk.Checkbutton(pencere,text="Zıplama [Space] Dahil Edilsin mi?",variable=checkbutton,onvalue=1,offvalue=0,width=22).place(x=180,y=220)

pencere.mainloop()