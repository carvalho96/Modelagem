#!/usr/bin/python

from include import Votacao
from Tkinter import *

'''
Projeto De Modelagem de Sistemas
'''

master = Tk()

def callback():
    print "click!"

f = Frame(master, height=320, width=320)
f.pack_propagate(0) # don't shrink
f.pack()

b = Button(master, text="Click me",  command=callback)
a = Button(master, text="Click me", compound=CENTER, command=callback)
d = Button(master, text="Click me", compound=CENTER, command=callback)
c = Button(master, text="Click me", compound=CENTER, command=callback)


b.pack()

mainloop()
