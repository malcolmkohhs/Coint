import os
from typing import final
from unicodedata import name
import cv2
import tkinter.font
from tkinter import *
from tkinter import ttk
import tkinter as tk
from time import sleep
from PIL import ImageTk, Image 
import random
newfont = ("Open Sans", 20)

#identify function
def coinidentification():
    #automatic function
    def auto():
        print('auto')

    #manual function
    def manual():
        print('manual')

    #identify page
    print('coin identification')
    identifypage = Tk()
    identifypage.title("Coint: Identify")
    identifypage.geometry('600x400')
    identifypage.geometry('+550+250')


    #identify question
    identifyquestion = Label(identifypage,text='Welcome! \nHow would you like to identify your coin')
    identifyquestion.place(x=120,y=50)
    identifyquestion.configure(font=newfont)

    #automatic button
    automatic = Button(identifypage, text="Automatic", command=auto)
    automatic.configure(height=3,width=30)
    automatic.place(x=150,y=150)

    #manual button
    automatic = Button(identifypage, text="Manual", command=manual)
    automatic.configure(height=3,width=30)
    automatic.place(x=150,y=220)
correct,cont,correct1,ansimg=True,"Continue",True,""
prevans,answer,prevans1=0,0,[]
dollar,cents1,cents2=0,0,0
totalscore=0
def playgame():
    global finalanswer
    #beginner game mode
    def beginner():
        global correct, prevans, answer, ansimg
        print('beginner')     
        gamebeginner = tk.Toplevel()
        gamebeginner.title("Coint: Game [Beginner]")
        gamebeginner.geometry('600x400')
        gamebeginner.geometry('+550+250')
        beginnerquestions = ['five_cent0.png','ten_cent0.png','twenty_cent0.png','fifty_cent0.png','one_dollar0.png','five_cent_old0.png','ten_cent_old0.png','twenty_cent_old0.png','fifty_cent_old0.png','one_dollar_old0.png'] #iamges of coins in any order
        beginnervalues = [5,10,20,50,100,5,10,20,50,100] #value of coins in the same order as beginnerquestions
        if correct==True:
            r=random.choice(beginnerquestions)
            indexr = beginnerquestions.index(r)
            answer = beginnervalues[indexr]
        elif correct==False:
            answer=prevans
            r=ansimg
        prevans=answer
        ansimg=r
        imgc = Image.open(r)
        imgc = imgc.resize((150, 150))
        imgc = ImageTk.PhotoImage(imgc)
        panelc = tkinter.Label(gamebeginner, image = imgc)
        panelc.image=imgc
        panelc.place(x=220,y=60)
        lbegin1=Label(gamebeginner,text="Identify the coin!",font=("Open Sans",20,"bold"))
        lbegin1.place(x=200,y=10)
        lbegin2=Label(gamebeginner,text="Pick the option (value) that matches the image of the coin.",font=("Open Sans",15))
        lbegin2.place(x=110,y=40)
        def button(a):
            global correct, answer, cont, totalscore
            print(answer)
            print(a)
            if a == answer:
                print('correct')
                correct = True
                cont="Continue"
                totalscore+=3
            else:
                print('wrong')
                correct = False
                cont="Try Again"
                totalscore+=1

            def no():
                print('no')
                gamecontinue.destroy()
                gamebeginner.destroy()

            def yes():
                print('yes')
                gamecontinue.destroy()
                gamebeginner.destroy()
                beginner()

            gamecontinue = tk.Toplevel()
            gamecontinue.title("Coint: Game [Beginner] Result")
            gamecontinue.geometry('600x400')
            gamecontinue.geometry('+550+250')
            qwe,pic,ptt=0,["win.png","tryagain.png"],["3","1"]
            if correct==False:
                qwe=1
            imgd = Image.open(pic[qwe])
            imgd = imgd.resize((600, 110))
            imgd = ImageTk.PhotoImage(imgd)
            paneld = tkinter.Label(gamecontinue, image = imgd)
            paneld.image=imgd
            paneld.place(x=0,y=0)
            w = Canvas(gamecontinue, width=400, height=10)
            w.create_line(0, 10, 500, 10, fill="black")
            w.place(x=100,y=205)
            tscore= Label(gamecontinue,text=("Total Score: "+str(totalscore)),font=("Open Sans",20))
            tscore.place(x=230,y=220)
            tadd= Label(gamecontinue,text=("Added Points: "+ptt[qwe]),font=("Open Sans",20))
            tadd.place(x=220,y=250)
            if qwe==0:
                tins=Label(gamecontinue,text='Challenge Passed!\nClick "Continue" for another problem or\nclick "Quit" to leave the game.',font=("Open Sans",18))
                tins.place(x=130,y=120)
            else:
                tins=Label(gamecontinue,text='Keep Trying!\nClick "Try Again" to re-attempt the problem or\nclick "Quit" to leave the game.',font=("Open Sans",18))
                tins.place(x=100,y=120)
            #quit
            quitbutton = Button(gamecontinue, text= 'Quit', command = no)
            quitbutton.configure(height=2,width=11)
            quitbutton.place(x=20,y=350)
            #continue
            continuebutton = Button(gamecontinue, text= cont, command = yes)
            continuebutton.configure(height=2,width=11)
            continuebutton.place(x=450,y=350)
        
        #choice 1
        fivecentbutton = Button(gamebeginner, text= '$0.05', command = lambda: button(5))
        fivecentbutton.configure(height=3,width=25)
        fivecentbutton.place(x=40,y=200)
        #choice 2
        tencentbutton = Button(gamebeginner, text= '$0.10', command = lambda:button(10))
        tencentbutton.configure(height=3,width=25)
        tencentbutton.place(x=300,y=200)
        #choice 3
        twentycentbutton = Button(gamebeginner, text= '$0.20', command = lambda:button(20))
        twentycentbutton.configure(height=3,width=25)
        twentycentbutton.place(x=40,y=260)
        #choice 4
        fiftycentbutton = Button(gamebeginner, text= '$0.50', command = lambda:button(50))
        fiftycentbutton.configure(height=3,width=25)
        fiftycentbutton.place(x=300,y=260)
        #choice 5
        onedollarbutton = Button(gamebeginner, text= '$1.00', command = lambda:button(100))
        onedollarbutton.configure(height=3,width=25)
        onedollarbutton.place(x=170,y=320)
     
    #advanced game mode
    def advanced():
        global correct1, prevans1
        questionlist = []
        questionindex = []
        questionvalues = []
        print('advanced')
        gameadvanced = tk.Toplevel()
        gameadvanced.title("Coint: Game [Advanced]")
        gameadvanced.geometry('600x400')
        gameadvanced.geometry('+550+250')

        beginnerquestions = ['five_cent0.png','ten_cent0.png','twenty_cent0.png','fifty_cent0.png','one_dollar0.png','five_cent_old0.png','ten_cent_old0.png','twenty_cent_old0.png','fifty_cent_old0.png','one_dollar_old0.png'] #iamges of coins in any order #iamges of coins in any order
        beginnervalues = [5,10,20,50,100,5,10,20,50,100] #value of coins in the same order as beginnerquestions

        #obtain questions
        if correct1==True:
            for i in range(5):
                question = random.choice(beginnerquestions)
                questionlist.append(question)
        else:
            questionlist=prevans1
        prevans1=questionlist
        #obtain position of questions
        for i in questionlist:
            index = beginnerquestions.index(i)
            questionindex.append(index)
        print(questionindex)
        x1,y1=50,100
        for i in range (5):
            imgc = Image.open(questionlist[i])
            imgc = imgc.resize((100, 100))
            imgc = ImageTk.PhotoImage(imgc)
            panelc = tkinter.Label(gameadvanced, image = imgc)
            panelc.image=imgc
            panelc.place(x=x1,y=y1)
            x1+=100
        #obtain answers
        ladv1=Label(gameadvanced,text="Calculate The Value!",font=("Open Sans",20,"bold"))
        ladv1.place(x=200,y=10)
        ladv2=Label(gameadvanced,text="Calculate the total value of the coins shown down below and enter using the drop down list.",font=("Open Sans",13))
        ladv2.place(x=30,y=40)
        for i in questionindex:
            value = beginnervalues[i]
            questionvalues.append(value)
        print(questionvalues)
        answer1 = sum(questionvalues)
        print(answer1)
        valbel=Label(gameadvanced,text="$",font=("Open Sans",20))
        valbel.place(x=140,y=245)
        dlabel=Label(gameadvanced,text=".",font=("Open Sans",20))
        dlabel.place(x=260,y=245)
        #dollar dropbar
        optionsdollar = ['0','1','2','3','4','5','6','7','8','9']
        clickeddollar = StringVar(gameadvanced)
        clickeddollar.set(optionsdollar[0])
        dropdollar = OptionMenu( gameadvanced , clickeddollar , *optionsdollar )
        dropdollar.configure(width=5)

        dropdollar.place(x=160,y=250)
        dollar = 0
        def change_dropdown(*args):
            global dollar
            value1 = clickeddollar.get()
            dollar = value1
            print(value1)
        clickeddollar.trace('w', change_dropdown)

        #cents 1 dropbar 
        optionscents1 = ['0','1','2','3','4','5','6','7','8','9']
        clickedcents1 = StringVar(gameadvanced)
        clickedcents1.set(optionscents1[0])
        dropcents1 = OptionMenu( gameadvanced , clickedcents1 , *optionscents1 )
        dropcents1.configure(width=5)
        dropcents1.place(x=280,y=250)
        cents1 = 0
        def change_dropdown(*args):
            global cents1
            value2 = clickedcents1.get()
            cents1 = value2
            print(value2)
        clickedcents1.trace('w', change_dropdown)

        #cents 2 dropbar
        optionscents2 = ['0','1','2','3','4','5','6','7','8','9']
        clickedcents2 = StringVar(gameadvanced)
        clickedcents2.set(optionscents2[0])
        dropcents2 = OptionMenu( gameadvanced , clickedcents2 , *optionscents2 )
        dropcents2.configure(width=5)
        dropcents2.place(x=380,y=250)
        cents2 = 0
        def change_dropdown(*args):
            global cents2
            value3 = clickedcents2.get()
            cents2 = value3
            print(value3)
        clickedcents2.trace('w', change_dropdown)
        
        finalanswer = 0
        def answer():
            global dollar, cents1, cents2, finalanswer
            answer = float(dollar) + float(cents1)*0.1 + float(cents2)*0.01
            finalanswer = round(answer*100)

        #submission button
        def submit():
            global dollar, cents1, cents2, finalanswer, correct1, totalscore
            print('submit')
            print(answer1)
            answer()
            print(finalanswer)
            gameadvanced.destroy()
            if finalanswer == answer1:
                print('correct')
                correct1=True
                cont="Continue"
                totalscore+=3
            else:
               print('wrong')
               correct1=False
               cont="Try Again"
               totalscore+=1
            dollar,cents1,cents2=0,0,0
            def no():
                print('no')
                gamecontinue.destroy()
                #gameadvanced.destroy()
            def yes():
                print('yes')
                gamecontinue.destroy()
                #gameadvanced.destroy()
                advanced()

            gamecontinue = tk.Toplevel()
            gamecontinue.title("Coint: Game [Advanced] Result")
            gamecontinue.geometry('600x400')
            gamecontinue.geometry('+550+250')
            qwe,pic,ptt=0,["win.png","tryagain.png"],["3","1"]
            if correct1==False:
                qwe=1
            imgd = Image.open(pic[qwe])
            imgd = imgd.resize((600, 110))
            imgd = ImageTk.PhotoImage(imgd)
            paneld = tkinter.Label(gamecontinue, image = imgd)
            paneld.image=imgd
            paneld.place(x=0,y=0)
            w = Canvas(gamecontinue, width=400, height=10)
            w.create_line(0, 10, 500, 10, fill="black")
            w.place(x=100,y=205)
            tscore= Label(gamecontinue,text=("Total Score: "+str(totalscore)),font=("Open Sans",20))
            tscore.place(x=230,y=220)
            tadd= Label(gamecontinue,text=("Added Points: "+ptt[qwe]),font=("Open Sans",20))
            tadd.place(x=220,y=250)
            if qwe==0:
                tins=Label(gamecontinue,text='Challenge Passed!\nClick "Continue" for another problem or\nclick "Quit" to leave the game.',font=("Open Sans",18))
                tins.place(x=130,y=120)
            else:
                tins=Label(gamecontinue,text='Keep Trying!\nClick "Try Again" to re-attempt the problem or\nclick "Quit" to leave the game.',font=("Open Sans",18))
                tins.place(x=100,y=120)
            #quit
            quitbutton = Button(gamecontinue, text= 'Quit', command = no)
            quitbutton.configure(height=2,width=11)
            quitbutton.place(x=20,y=350)
            #continue
            continuebutton = Button(gamecontinue, text= cont, command = yes)
            continuebutton.configure(height=2,width=11)
            continuebutton.place(x=450,y=350)

        submitbutton = Button(gameadvanced,text = 'Submit', command = submit)
        submitbutton.configure(height=1,width=10)
        submitbutton.configure(font=newfont)
        submitbutton.place(x=220,y=350)

    print('play game')
    gamemain = Tk()
    gamemain.title("Coint: Game")
    gamemain.geometry('600x400')
    gamemain.geometry('+550+250')
    #gamemode question
    gamemodequestion = Label(gamemain, text="Select your Game Mode!")
    gamemodequestion.place(x=190,y=70)
    gamemodequestion.configure(font=newfont)
    #gamemode beginner
    easy = Button(gamemain,text='Beginner',command=beginner)
    easy.configure(height=6,width=30)
    easy.place(x=150,y=120)
    #gamemode advanced
    hard = Button(gamemain, text='Advanced', command=advanced)
    hard.configure(height=6,width=30)
    hard.place(x=150,y=240)

def learn():
    print('learn')
    learnmain = Tk()
    learnmain.title("Coint: Learn")
    learnmain.geometry('600x400')
    learnmain.geometry('+550+250')

def help():
    helpmain = Tk()
    helpmain.title("Coint: Help")
    helpmain.geometry('600x700')
    helpmain.geometry('+550+250')
    
    f = open("README.txt", "r",)
    data = f.readlines()
    data1=""
    for i in data[18:]:
        data1+=i
    helplabel = Label(helpmain, text = data1,wraplength=595,justify='left',font=("Open Sans",13))
    helplabel.place(x=2,y=20)
    lhead=Label(helpmain,text="Help",font=("Open Sans",18,"bold"))
    lhead.place(x=280,y=2)
#mainpage
mainpage = Tk()
mainpage.title("Coint")
mainpage.geometry("600x400")
mainpage.geometry("+550+250")
#image on mainpage
img = ImageTk.PhotoImage(Image.open("cointmain.jpeg"))
panel = tkinter.Label(mainpage, image = img)
panel.place(x=0,y=0)
#welcome text
mainpagewelcome = Label(mainpage, text="Hello! \nWelcome to Coint, \nwhat would you like to do?")
mainpagewelcome.place(x=330,y=50)
mainpagewelcome.configure(font = newfont)
#identify button
mainpageidentify = Button(mainpage, text="Coin Identification", command=coinidentification)
mainpageidentify.configure(height=2,width=20)
mainpageidentify.place(x=340,y=150)
#game button
mainpagegame = Button(mainpage, text="Play A Game", command=playgame)
mainpagegame.configure(height=2,width=20)
mainpagegame.place(x=340,y=200)
#learn button
mainpagelearn = Button(mainpage, text="Learn", command=learn)
mainpagelearn.configure(height=2,width=20)
mainpagelearn.place(x=340,y=250)
#help button
mainpagehelp = Button(mainpage, text="Help", command=help)
mainpagehelp.configure(height=2,width=20)
mainpagehelp.place(x=340,y=300)

#executing the app
mainpage.mainloop()
