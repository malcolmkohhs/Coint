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
canvas.geometry("+550+250") #making the window centre #!!!

def coinidentification():
    identifymain = Tk() #making the mainpage of the coin identification
    identifymain.title("Coint: Coin Identification") #naming the window
    identifymain.geometry("600x400") #window dimension
    identifymain.geometry("+550+250") #making the window centre #!!!
    canvas.destroy()

    buttonai = Button(identifymain, text="Automated", command=automatic)
    buttonai.configure(height = 12,width = 62)
    buttonai.place(x=0, y=0)

    buttonmanual = Button(identifymain, text="Manual", command=manual)
    buttonmanual.configure(height = 12,width = 62)
    buttonmanual.place(x=0, y=200)

def playgame():
    gamemain = Tk() #making the main page of the game
    gamemain.title("Coint: Game") #naming the window
    gamemain.geometry("600x400") #window dimension
    gamemain.geometry("+550+250") #making the window centre #!!!
    canvas.destroy()
    
def learn():
    learnmain = Tk() #making the main page of the game
    learnmain.title("Coint: Learn") #naming the window
    learnmain.geometry("600x400") #window dimension
    learnmain.geometry("+550+250") #making the window centre #!!!
    canvas.destroy()
    
def helpp():
    helpmain = Tk() #making the main page of the game
    helpmain.title("Coint: Help") #naming the window
    helpmain.geometry("600x400") #window dimension
    helpmain.geometry("+550+250") #making the window centre #!!!
    canvas.destroy()

labelspace = Label(canvas, text="                                           ")
labelspace.grid(row=0,column=0)
labelwelcome = Label(canvas, text="Hello! \nWelcome to Coint, \nwhat would you like to do?",)
labelwelcome.configure(font = newfont)
labelwelcome.place(x=330,y=50)

buttonidentify = Button(canvas, text="Coin Identification", command=coinidentification) #button to toggle to the coin identification page
buttongame = Button(canvas, text = "Play a game", command=playgame) #button to toggle to the game page
buttonlearn = Button(canvas, text = "Learn", command=learn) #button to toggle to the learn page
buttonhelp = Button(canvas, text = "Help", command=helpp) #button to toggle to the help page
buttonidentify.configure(height = 2,width = 20) #change button size
buttongame.configure(height = 2,width = 20) #change button size
buttonlearn.configure(height = 2,width = 20) #change button size
buttonhelp.configure(height = 2,width = 20) #change button size
buttonidentify.place(x=350,y=150) #button coords
buttongame.place(x=350,y=200) #button coords
buttonlearn.place(x=350,y=250) #button coords
buttonhelp.place(x=350, y=300)  #button coords 

img = ImageTk.PhotoImage(Image.open("cointmain.jpeg")) #load image
panel = tkinter.Label(canvas, image = img)
panel.place(x=0,y=0) #placement of image

#os.system('python ok.py')

#fin = open("test.txt","r")
#test = fin.readline()

#print(test)

def automatic():
    automatic = Tk()
    automatic.title("Coint: Identify")
    automatic.geometry("600x400") #window dimension
    automatic.geometry("+550+250")


def manual():
    manual = Tk()
    manual.title("Coint: Identify")
    manual.geometry("600x400")
    manual.geometry("+550+250")




canvas.mainloop()
