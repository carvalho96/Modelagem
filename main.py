#!/usr/bin/python

import string
from Votacao import votacao
from Tkinter import *
import tkMessageBox

'''
Projeto De Modelagem de Sistemas
'''
gui = Tk()
uev = votacao()
ment = StringVar()
def plus():
    if(uev.plusC() == 0):
        Acabou()
    labelA = Label(text = uev.getCarg()).grid(row= 0, column = 1)
def naoExiste():
   tkMessageBox.showinfo( "Aviso", "Nao Existe!")
def Acabou():
   tkMessageBox.showinfo( "Aviso", "Obrigado Por Votar!")
def callbackVer():
    mtxt = ment.get()
    candida = uev.getCandidato(uev.getCarg(), mtxt)
    if ( "0" != uev.getCandidato(uev.getCarg(), mtxt).getNome() ):
        path = candida.getpathImg()
        nome = candida.getNome()
        print nome
        apelido = candida.getApelido()
    else:
        naoExiste()
def callbackConf():
    mtxt = ment.get()
    candida = uev.getCandidato(uev.getCarg(), mtxt)
    print uev.getCarg()
    if ( "0" != uev.getCandidato(uev.getCarg(), mtxt).getNome() ):
        candida.countVotos()
        plus()
    else:
        naoExiste()

gui.geometry('600x600+500+500')
gui.title("Uev Rio de Janeiro")

xEntry = Entry(gui,textvariable = ment).grid(row= 1, column = 1)
labelA = Label(text = uev.getCarg()).grid(row= 0, column = 1)

B1 = Button(gui, text= "Ver", command = callbackVer).grid(row = 3, column = 1)
B2 = Button(gui, text= "Confirma", command = callbackConf).grid(row= 3, column = 2)
B2 = Button(gui, text= "Nulo", command = callbackVer).grid(row= 2, column = 0)
B2 = Button(gui, text= "Branco", command = callbackVer).grid(row= 2, column = 1)

gui.mainloop()
