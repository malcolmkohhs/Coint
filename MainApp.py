import os
import cv2
import tkinter.font
from tkinter import *
from tkinter import ttk
from time import sleep
from PIL import ImageTk, Image 
#import libraries
newfont = ("Open Sans", 20)
canvas = Tk() #making the window
canvas.title("Coint") #naming the window
canvas.geometry("600x400") #window dimension
canvas.geometry("+1500+0") #making the window centre #!!!

def coinidentification():
    coinidentification = Tk() #making the mainpage of the coin identification
    coinidentification.title("Coint: Coin Identification") #naming the window
    coinidentification.geometry("600x400") #window dimension
    coinidentification.geometry("+1500+0") #making the window centre #!!!

def playgame():
    gamemain = Tk() #making the main page of the game
    gamemain.title("Coint: Game") #naming the window
    gamemain.geometry("600x400") #window dimension
    gamemain.geometry("+1500+0") #making the window centre #!!!
    
def learn():
    learnmain = Tk() #making the main page of the game
    learnmain.title("Coint: Learn") #naming the window
    learnmain.geometry("600x400") #window dimension
    learnmain.geometry("+1500+0") #making the window centre #!!!
    
def helpp():
    helpmain = Tk() #making the main page of the game
    helpmain.title("Coint: Help") #naming the window
    helpmain.geometry("600x400") #window dimension
    helpmain.geometry("+1500+0") #making the window centre #!!!

labelspace = Label(canvas, text="                                           ")
labelspace.grid(row=0,column=0)
labelwelcome = Label(canvas, text="Hello! \nWelcome to Coint, \nwhat would you like to do?",)
labelwelcome.configure(font = newfont)
labelwelcome.place(x=330,y=50)

buttonidentify = Button(canvas, text="Coin Identification", command=coinidentification)
buttongame = Button(canvas, text = "Play a game", command=playgame)
buttonlearn = Button(canvas, text = "Learn", command=learn)
buttonhelp = Button(canvas, text = "Help", command=helpp)
buttonidentify.configure(height = 2,width = 20)
buttongame.configure(height = 2,width = 20)
buttonlearn.configure(height = 2,width = 20)
buttonhelp.configure(height = 2,width = 20)
buttonidentify.place(x=350,y=150)
buttongame.place(x=350,y=200)
buttonlearn.place(x=350,y=250)
buttonhelp.place(x=350, y=300)

img = ImageTk.PhotoImage(Image.open("cointmain.jpeg")) #load image
panel = tkinter.Label(canvas, image = img)
panel.place(x=0,y=0) #placement of image

#os.system('python ok.py')

#fin = open("test.txt","r")
#test = fin.readline()

#print(test)

canvas.mainloop()