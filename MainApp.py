from tkinter import *
from tkinter import ttk
import os
#importing libraries

canvas = Tk() #making the window
canvas.title("Coint") #naming the window
canvas.geometry("600x400") #window dimension
canvas.geometry("+350+250") #making the window centre

labelwelcome = Label(canvas, text="Welcome to Coint, What would you like to do?")
labelwelcome.grid(row=0, column=0)

buttonidentify = Button(canvas, text="Coin Identification")
buttongame = Button(canvas, text = "Play a game")
buttonidentify.grid(row=2, column=0)
buttongame.grid(row=2, column=1) 

os.system('python ok.py')

fin = open("test.txt","r")
test = fin.readline()

print(test)

canvas.mainloop()

