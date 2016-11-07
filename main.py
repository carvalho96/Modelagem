#!/usr/bin/python

import string
import sys
from Votacao import votacao
from Tkinter import *
import tkMessageBox
import time

'''
Projeto De Modelagem de Sistemas
'''
uev = votacao()
uev.UEvGet()
while ('19:44' != time.strftime("%H:%M")):
    time.sleep(5)
while uev.getHt() > time.strftime("%H:%M"):
    x = str(raw_input("\n\rEscreva CPF: "))
    while(uev.Voted(x) == 1):
        x = str(raw_input("CPF invalido!\n\nEscreva CPF: "))

    gui = Tk()
    ment = StringVar()
    def plus():
        if(uev.plusC() == 0):
            Acabou()
            return
        labelA = Label(text = uev.getCarg()).grid(row= 0, column = 1)


    def naoExiste():
       tkMessageBox.showinfo( "Aviso", "Nao Existe!")
    def Acabou():
       tkMessageBox.showinfo( "That's All Folks", "Obrigado Por Votar!")
       gui.destroy()

    def Candidato(nome, path, Apelido):
        p = "Nome: %s Apelido: %s  URL IMG: %s " % (nome, Apelido, path)
        tkMessageBox.showinfo( "Informacoes do Candidato", p)

    def callbackVer():
        mtxt = ment.get()
        candida = uev.getCandidato(uev.getCarg(), mtxt)
        if ( "0" != uev.getCandidato(uev.getCarg(), mtxt).getNome() ):
            path = candida.getpathImg()
            nome = candida.getNome()
            apelido = candida.getApelido()
            Candidato(nome, path, apelido)
        else:
            naoExiste()
    def callbackConf():
        mtxt = ment.get()
        candida = uev.getCandidato(uev.getCarg(), mtxt)
        if ( "0" != uev.getCandidato(uev.getCarg(), mtxt).getNome() ):
            candida.countVotos()
            plus()
        else:
            naoExiste()
    def callbackNulo():
        mtxt = ment.get()
        candida = uev.getCandidato(uev.getCarg(), "NULO")
        if ( "0" != uev.getCandidato(uev.getCarg(), "NULO").getNome() ):
            candida.countVotos()
            plus()
        else:
            naoExiste()
    def callbackBranco():
        mtxt = ment.get()
        candida = uev.getCandidato(uev.getCarg(), "BRANCO")
        if ( "0" != uev.getCandidato(uev.getCarg(), "BRANCO").getNome() ):
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
    B2 = Button(gui, text= "Nulo", command = callbackNulo).grid(row= 2, column = 0)
    B2 = Button(gui, text= "Branco", command = callbackBranco).grid(row= 2, column = 1)
#uev.sendData()
