import tkinter.font
from tkinter import *
from tkinter import ttk
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
    def beginner():
        print('beginner')
        
        gamebeginner = Tk()
        gamebeginner.title("Coint: Game[Beginner]")
        gamebeginner.geometry('600x400')
        gamebeginner.geometry('+550+250')

        beginnerquestions = ['image1.png','image2.png','imafe3.png','image4.png','image5.png'] #iamges of coins in any order
        beginnervalues = [5,10,20,50,100] #do according to beginnerquestions
        
        randomanswer = beginnervalues[random.randint(1,len(beginnerquestions)-1)]
        print(randomanswer)

        def fivecent():
            chosenanswer = 5
            print(5)
            if randomanswer == chosenanswer:
                print('Correct!')
            else:
                print('Wrong!')
        def tencent():
            chosenanswer = 10
            print(10)
            if randomanswer == chosenanswer:
                print('Correct!')
            else:
                print('Wrong!')
        def twentycent():
            chosenanswer = 20
            print(20)
            if randomanswer == chosenanswer:
                print('Correct!')
            else:
                print('Wrong!')
        def fiftycent():
            chosenanswer = 50
            print(50)
            if randomanswer == chosenanswer:
                print('Correct!')
            else:
                print('Wrong!')
        def onedollar():
            chosenanswer = 100
            print(100)
            if randomanswer == chosenanswer:
                print('Correct!')
            else:
                print('Wrong!')
        
        #choice 1
        value1button = Button(gamebeginner, text= '$0.05' ,command = fivecent)
        value1button.configure(height=3,width=25)
        value1button.place(x=40,y=200)
        #choice 2
        value2button = Button(gamebeginner, text= '$0.10', command = tencent)
        value2button.configure(height=3,width=25)
        value2button.place(x=300,y=200)
        #choice 3
        value3button = Button(gamebeginner, text= '$0.20', command = twentycent)
        value3button.configure(height=3,width=25)
        value3button.place(x=40,y=260)
        #choice 4
        value4button = Button(gamebeginner, text= '$0.50', command = fiftycent)
        value4button.configure(height=3,width=25)
        value4button.place(x=300,y=260)
        #choice 5
        value5button = Button(gamebeginner, text= '$1.00', command = onedollar)
        value5button.configure(height=3,width=25)
        value5button.place(x=170,y=320)




    def moderate():
        print('moderate')

    def advanced():
        print('advanced')

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
    easy.configure(height=3,width=30)
    easy.place(x=150,y=120)

    #gamemode moderate
    easy = Button(gamemain,text='Moderate',command=moderate)
    easy.configure(height=3,width=30)
    easy.place(x=150,y=190)

    #gamemode advanced
    hard = Button(gamemain, text='Advanced', command=advanced)
    hard.configure(height=3,width=30)
    hard.place(x=150,y=260)

def learn():
    print('learn')

    learnmain = Tk()
    learnmain.title("Coint: Learn")
    learnmain.geometry('600x400')
    learnmain.geometry('+550+250')

def help():
    print('help')
    
    helpmain = Tk()
    helpmain.title("Coint: help")
    helpmain.geometry('600x400')
    helpmain.geometry('+550+250')

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


mainpage.mainloop()