from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import tkinter
xx,candestroy=0,True
def coins():
    global xx, candestroy
    if xx==0 and candestroy==True:
        learnmain.withdraw()
        candestroy=False
    coinslist=["Five Cent","Ten Cent","Twenty Cent","Fifty Cent","One Dollar"]
    coinsimglist=["five_cent","ten_cent","twenty_cent","fifty_cent","one_dollar"]
    coinsvalue=["0.05","0.10","0.20","0.50","1"]
    coinsmain=tk.Toplevel()
    coinsmain.title("Coint: Learn ({} Coin)".format(coinslist[xx]))
    coinsmain.geometry("600x400") #window dimension
    coinsmain.geometry("+550+250") #making the window centre #!!!
    cmainl=tk.Label(coinsmain,text=("{} Coin".format(coinslist[xx])),font=("Open Sans",20,"bold"))
    cmainl.place(x=220,y=10)
    e = Canvas(coinsmain, width=500, height=10)
    e.create_line(0, 10, 500, 10, fill="black")
    e.place(x=50,y=40)

    img = Image.open(coinsimglist[xx]+"0.png")
    img = img.resize((130, 130))
    img = ImageTk.PhotoImage(img)
    panel = tkinter.Label(coinsmain, image = img)
    panel.image=img
    panel.place(x=150,y=55)
    imgo = Image.open(coinsimglist[xx]+"_old0.png")
    imgo = imgo.resize((130, 130))
    imgo = ImageTk.PhotoImage(imgo)
    panelo = tkinter.Label(coinsmain, image = imgo)
    panelo.image=imgo
    panelo.place(x=350,y=55)

    cname=tk.Label(coinsmain,text="New Coin                                   Old Coin",font=("Open Sans",15))
    cname.place(x=170,y=180)
    e = Canvas(coinsmain, width=500, height=10)
    e.create_line(0, 10, 500, 10, fill="black")
    e.place(x=50,y=200)
    cval=tk.Label(coinsmain,text="Value",font=("Open Sans",15,"bold"))
    cval.place(x=50,y=215)
    cvalcd=tk.Label(coinsmain,text=("Cents (¢): {}                          Dollars ($): {}".format(int(float(coinsvalue[xx])*100),coinsvalue[xx])),font=("Open Sans",15))
    cvalcd.place(x=50,y=235)
    cfea=tk.Label(coinsmain,text="Key Features",font=("Open Sans",15,"bold"))
    cfea.place(x=50,y=258)
    file = open('coindesclearn.txt')
    content = file.readlines()
    mains=""
    for i in content[(xx+1)*4-4:(xx+1)*4]:
        mains+=i
    file.close()
    kfea=tk.Label(coinsmain,text=mains,justify="left",font=("Open Sans",14))
    kfea.place(x=50,y=282)
    if xx!=4:
        bnext1=Button(coinsmain,text="Next",width=15,command = lambda:nextl())
        bnext1.place(x=400,y=365)
        def nextl():
            global xx
            coinsmain.destroy()
            xx+=1
            coins()
    if xx!=0:
        bback=tk.Button(coinsmain,text="Back",width=15,command=lambda:backl())
        bback.place(x=50,y=365)
        def backl():
            global xx
            coinsmain.destroy()
            xx-=1
            coins()
    bquit=tk.Button(coinsmain,text="Quit",width=10,command=lambda:quitl())
    bquit.place(x=250,y=365)
    
    coinsmain.mainloop()

def quit():
    #go back to learn page
    print("quit")
learnmain = Tk() #making the main page of the game
learnmain.title("Coint: Learn") #naming the window
learnmain.geometry("600x400") #window dimension
learnmain.geometry("+550+250") #making the window centre #!!!
mainl=tk.Label(learnmain,text="Learn",font=("Open Sans",20,"bold"))
mainl.place(x=250,y=20)
mainl1=tk.Label(learnmain,text="Learn about all the coins that can be found in Singapore!",font=("Open Sans",17))
mainl1.place(x=70,y=50)
mainl2=tk.Label(learnmain,text="Disclaimer:\n Only covers 2nd and 3rd series of coins.",font=("Open Sans",15))
mainl2.place(x=150,y=290)
mainl3=tk.Label(learnmain,text="Instructions to use",font=("Open Sans",15,"bold"))
mainl3.place(x=210,y=100)
w = Canvas(learnmain, width=500, height=10)
w.create_line(0, 10, 500, 10, fill="black")
w.place(x=50,y=75)
description='1. Click "Next" to view the next coin on the next page.\n2. Click "Back" to view the previous coin on the previous page.\n3. Click "Quit" to go back to this page.\n4. The pages would display the images of the coins and the description of them. \n5. These information can help you with your game, have fun!'
descl=tk.Label(learnmain, text=description, font=("Open Sans",15))
descl.place(x=20,y=130)
bgo=Button(learnmain,text="Let's Go!",height=2,width=20,command = lambda:coins())
bgo.place(x=380,y=350)
bback=tk.Button(learnmain,text="Back",height=2,width=20,command=lambda:back())
bback.place(x=30,y=350)
learnmain.mainloop()
