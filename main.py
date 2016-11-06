#!/usr/bin/python

import string
from include import Votacao
from Tkinter import *

'''
Projeto De Modelagem de Sistemas
'''
gui = Tk()

Cargo = "~Presidente~"
ment = StringVar()

def callback():
    mtxt = ment.get()
    labelA = Label(text = mtxt).grid(row= 6, column = 6)

gui.geometry('600x600+500+500')
gui.title("Uev Rio de Janeiro")

xEntry = Entry(gui,textvariable = ment).grid(row= 1, column = 1)
labelA = Label(text = Cargo).grid(row= 0, column = 1)   

B1 = Button(gui, text= "Ver", command = callback).grid(row = 3, column = 2)
B2 = Button(gui, text= "Confirma", command = callback).grid(row= 3, column = 2)
B2 = Button(gui, text= "Nulo", command = callback).grid(row= 2, column = 0)
B2 = Button(gui, text= "Branco", command = callback).grid(row= 2, column = 1)

gui.mainloop()
