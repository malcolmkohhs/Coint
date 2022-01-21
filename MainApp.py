import os
import tkinter.font
from tkinter import *
from tkinter import ttk
from time import sleep
#import libraries

canvas = Tk() #making the window
canvas.title("Coint") #naming the window
canvas.geometry("600x400") #window dimension
canvas.geometry("+1500+0") #making the window centre #!!!

def coinidentification():
    coinidentification = Tk() #making the mainpage of the coin identification
    coinidentification.title("Coint") #naming the window
    coinidentification.geometry("600x400") #window dimension
    coinidentification.geometry("+1500+0") #making the window centre #!!!

def playgame():
    gamemain = Tk() #making the main page of the game
    gamemain.title("Coint") #naming the window
    gamemain.geometry("600x400") #window dimension
    gamemain.geometry("+1500+0") #making the window centre #!!!

labelspace = Label(canvas, text="                                           ")
labelspace.grid(row=0,column=0)
labelwelcome = Label(canvas, text="Welcome to Coint, What would you like to do?",)
labelwelcome.grid(row=0, column=1)

buttonidentify = Button(canvas, text="Coin Identification", command=coinidentification)
buttongame = Button(canvas, text = "Play a game", command=playgame)
buttonidentify.grid(row=1, column=1)
buttongame.grid(row=2, column=1) 

#os.system('python ok.py')

#fin = open("test.txt","r")
#test = fin.readline()

#print(test)


canvas.mainloop()

