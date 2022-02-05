import os
from typing import final
from unicodedata import name
import cv2
import tkinter.font
from tkinter import *
from tkinter import ttk
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

def playgame():
    global finalanswer
    #beginner game mode
    def beginner():
        print('beginner')     
        gamebeginner = Tk()
        gamebeginner.title("Coint: Game [Beginner]")
        gamebeginner.geometry('600x400')
        gamebeginner.geometry('+550+250')
        
        def random():
            import random
            beginnerquestions = ['image1.png','image2.png','image3.png','image4.png','image5.png'] #iamges of coins in any order
            beginnervalues = [5,10,20,50,100] #value of coins in the same order as beginnerquestions
            r=random.choice(beginnerquestions)
            indexr = beginnerquestions.index(r)
            answer = beginnervalues[indexr]
            print(answer)
            return answer

        def button(a):
            answer = random()
            print(a)
            if a == answer:
                print('correct')
                correct = 'correct'
            else:
                print('wrong')
                correct = 'wrong'

            def no():
                print('no')
                gamecontinue.destroy()
                gamebeginner.destroy()

            def yes():
                print('yes')
                gamecontinue.destroy()
                gamebeginner.destroy()
                beginner()

            #pop up game conitnue
            gamecontinue = Tk()
            gamecontinue.title("Coint: Game [Beginner]")
            gamecontinue.geometry('270x150')
            gamecontinue.geometry('+720+450')
            #quit
            quitbutton = Button(gamecontinue, text= 'Quit', command = no)
            quitbutton.configure(height=3,width=11)
            quitbutton.pack(side =RIGHT)
            #continue
            continuebutton = Button(gamecontinue, text= 'Continue', command = yes)
            continuebutton.configure(height=3,width=11)
            continuebutton.pack(side = LEFT)
            #correct label
            correctlabel = Label(gamecontinue,text = correct)
            correctlabel.pack(side = TOP)

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
        questionlist = []
        questionindex = []
        questionvalues = []

        print('advanced')
        gameadvanced = Tk()
        gameadvanced.title("Coint: Game [Advanced]")
        gameadvanced.geometry('600x400')
        gameadvanced.geometry('+550+250')

        import random
        beginnerquestions = ['image1.png','image2.png','image3.png','image4.png','image5.png'] #iamges of coins in any order
        beginnervalues = [5,10,20,50,100] #value of coins in the same order as beginnerquestions
        #obtain questions
        for i in range(5):
            question = random.choice(beginnerquestions)
            questionlist.append(question)
        print(questionlist)
        #obtain position of questions
        for i in questionlist:
            index = beginnerquestions.index(i)
            questionindex.append(index)
        print(questionindex)
        #obtain answers
        for i in questionindex:
            value = beginnervalues[i]
            questionvalues.append(value)
        print(questionvalues)
        answer1 = sum(questionvalues)
        print(answer1)
    
        #dollar dropbar
        optionsdollar = ['0.00','1.00','2.00','3.00','4.00','5.00','6.00','7.00','8.00']
        clickeddollar = StringVar(gameadvanced)
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
        optionscents1 = ['0.00','0.10','0.20','0.30','0.40','0.50','0.60','0.70','0.80']
        clickedcents1 = StringVar(gameadvanced)
        dropcents1 = OptionMenu( gameadvanced , clickedcents1 , *optionscents1 )
        dropcents1.configure(width=5)
        dropcents1.place(x=260,y=250)
        cents1 = 0
        def change_dropdown(*args):
            global cents1
            value2 = clickedcents1.get()
            cents1 = value2
            print(value2)
        clickedcents1.trace('w', change_dropdown)

        #cents 2 dropbar
        optionscents2 = ['0.00','0.01','0.02','0.03','0.04','0.05','0.06','0.07','0.08']
        clickedcents2 = StringVar(gameadvanced)
        dropcents2 = OptionMenu( gameadvanced , clickedcents2 , *optionscents2 )
        dropcents2.configure(width=5)
        dropcents2.place(x=360,y=250)
        cents2 = 0
        def change_dropdown(*args):
            global cents2
            value3 = clickedcents2.get()
            cents2 = value3
            print(value3)
        clickedcents2.trace('w', change_dropdown)
        
        finalanswer = 0
        def answer():
            global dollar
            global cents1
            global cents2
            global finalanswer
            #print('submit')
            answer = float(dollar) + float(cents1) + float(cents2)
            finalanswer = round(answer*100)

        #submission button
        def submit():
            global dollar
            global cents1
            global cents2
            global finalanswer
            print('submit')
            print(answer1)
            answer()
            print(finalanswer)
            if finalanswer == answer1:
                print('correct')
            else:
               print('wrong')
            
            def no():
                print('no')
                gamecontinue.destroy()
                gameadvanced.destroy()
            def yes():
                print('yes')
                gamecontinue.destroy()
                gameadvanced.destroy()
                advanced()

            gamecontinue = Tk()
            gamecontinue.title("Coint: Game [Beginner]")
            gamecontinue.geometry('270x150')
            gamecontinue.geometry('+720+450')
            #quit
            quitbutton = Button(gamecontinue, text= 'Quit', command = no)
            quitbutton.configure(height=3,width=11)
            quitbutton.pack(side =RIGHT)
            #continue
            continuebutton = Button(gamecontinue, text= 'Continue', command = yes)
            continuebutton.configure(height=3,width=11)
            continuebutton.pack(side = LEFT)

        submitbutton = Button(gameadvanced,text = 'Submit', command = submit)
        submitbutton.configure(height=3,width=15)
        submitbutton.configure(font=newfont)
        submitbutton.place(x=310,y=290)

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
    helpmain.title("Coint: help")
    helpmain.geometry('600x570')
    helpmain.geometry('+550+250')

    f = open("README.txt", "r",)
    data = f.read()
    
    helplabel = Label(helpmain, text = data,wraplength=600,justify='left',)
    helplabel.place(x=0,y=0)

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
mainpagehelp = Button(mainpage, text="help", command=help)
mainpagehelp.configure(height=2,width=20)
mainpagehelp.place(x=340,y=300)

#executing the app
mainpage.mainloop()