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

#IDENTIFY FUNCTION
def coinidentification():
    #automatic function
    def auto():
        print('auto')

    #manual function
    def manual():
        print('manual')
        main_screen = Tk()
        main_screen.geometry('600x400')
        main_screen.geometry("+550+250")
        main_screen.title('Manual Coin Finder')
        main_title = tk.Label(main_screen,text='Manual Coin Finder', font=('Open Sans', 20, 'bold'))
        main_title.place(x=190,y=20)
        main_title1=tk.Label(main_screen,text="Identify the coin you have in hand manually and learn about it along the way!",font=("Open Sans",15))
        main_title1.place(x=30,y=50)
        w = Canvas(main_screen, width=500, height=10)
        w.create_line(0, 10, 500, 10, fill="black")
        w.place(x=50,y=75)
        main_title2=tk.Label(main_screen,text="Instructions to use",font=("Open Sans",15,"bold"))
        main_title2.place(x=210,y=100)
        description='1. Read the description as displayed on the screen.\n2. Check if the coin matches the description/ image.\n3. Click "Yes" if the coins matches the description.\n4. Click "No" if otherwise.'
        descl=tk.Label(main_screen, text=description, font=("Open Sans",15))
        descl.place(x=100,y=130)
        yy=0
        def result():
            global yy
            coinslist=["Five Cent","Ten Cent","Twenty Cent","Fifty Cent","One Dollar"]
            coinsimglist=["five_cent","ten_cent","twenty_cent","fifty_cent","one_dollar"]
            coinsvalue=["0.05","0.10","0.20","0.50","1"]
            coinsmain1=tk.Tk()
            coinsmain1.title("Coint: Identified ({} Coin)".format(coinslist[yy]))
            coinsmain1.geometry("600x400") #window dimension
            coinsmain1.geometry("+550+250") #making the window centre #!!!
            cmainl=tk.Label(coinsmain1,text=("{} Coin".format(coinslist[yy])),font=("Open Sans",20,"bold"))
            cmainl.place(x=220,y=10)
            e = Canvas(coinsmain1, width=500, height=10)
            e.create_line(0, 10, 500, 10, fill="black")
            e.place(x=50,y=40)

            img = Image.open(coinsimglist[yy]+"0.png")
            img = img.resize((130, 130))
            img = ImageTk.PhotoImage(img)
            panel = tkinter.Label(coinsmain1, image = img)
            panel.image=img
            panel.place(x=150,y=55)
            imgo = Image.open(coinsimglist[yy]+"_old0.png")
            imgo = imgo.resize((130, 130))
            imgo = ImageTk.PhotoImage(imgo)
            panelo = tkinter.Label(coinsmain1, image = imgo)
            panelo.image=imgo
            panelo.place(x=350,y=55)

            cname=tk.Label(coinsmain1,text="New Coin                                   Old Coin",font=("Open Sans",15))
            cname.place(x=170,y=180)
            e = Canvas(coinsmain1, width=500, height=10)
            e.create_line(0, 10, 500, 10, fill="black")
            e.place(x=50,y=200)
            cval=tk.Label(coinsmain1,text="Value",font=("Open Sans",15,"bold"))
            cval.place(x=50,y=215)
            cvalcd=tk.Label(coinsmain1,text=("Cents (¢): {}                          Dollars ($): {}".format(int(float(coinsvalue[yy])*100),coinsvalue[yy])),font=("Open Sans",15))
            cvalcd.place(x=50,y=235)
            cfea=tk.Label(coinsmain1,text="Key Features",font=("Open Sans",15,"bold"))
            cfea.place(x=50,y=258)
            file = open('coindesclearn.txt')
            content = file.readlines()
            mains=""
            for i in content[(yy+1)*4-4:(yy+1)*4]:
                mains+=i
            file.close()
            kfea=tk.Label(coinsmain1,text=mains,justify="left",font=("Open Sans",14))
            kfea.place(x=50,y=282)
            bbback= Button(coinsmain1, text="Back to Home",width=20,command=bthome)
            bbback.place(x=180,y=360)
        #if they choose to start the programme
        def gold_window():
            global new_gold
            main_screen.destroy()
            new_gold = tk.Tk()
            new_gold.title('Manual Coin Finder')
            new_gold.geometry('600x400')
            new_gold.geometry("+550+250")
            l1 = Label(new_gold, text="Is the coin mainly gold?", font=('Open Sans', 20, 'bold'))
            l1.place(x=185,y=20)
            img = Image.open("gold.png")
            img = ImageTk.PhotoImage(img)
            panel = tkinter.Label(new_gold, image = img)
            panel.image=img
            panel.place(x=120,y=110)
            w = Canvas(new_gold, width=500, height=10)
            w.create_line(0, 10, 500, 10, fill="black")
            w.place(x=50,y=60)
            gold_yes_btn = Button(new_gold, text='Yes', height=2, width=20, command=small_gold)
            gold_no_btn = Button(new_gold, text='No', height=2, width=20, command=silver_window)
            gold_no_btn.place(x=30, y=350)
            gold_yes_btn.place(x=380, y=350)


        #if they choose gold , ask if its small
        def small_gold():
            global small_gold_window
            new_gold.destroy()
            small_gold_window = tk.Tk()
            small_gold_window.title('Manual Coin Finder')
            small_gold_window.geometry('600x400')
            small_gold_window.geometry('+550+250')
            small_gold_window_label = Label(small_gold_window, text="Is the coin small?", font=('Open Sans', 20,'bold'))
            small_gold_window_label.place(x=190,y=20)
            small_gold_yes_btn = Button(small_gold_window, text= 'Yes', height=2, width=20, command=five_cent)
            small_gold_no_btn = Button(small_gold_window, text='No', height=2, width=20, command=one_dollar_coin1)
            w = Canvas(small_gold_window, width=500, height=10)
            w.create_line(0, 10, 500, 10, fill="black")
            w.place(x=50,y=60)
            small_gold_yes_btn.place(x=380, y=350)
            small_gold_no_btn.place(x=30, y=350)
        #when its not gold
        def silver_window():
            new_gold.destroy()
            global coin_silver_window
            coin_silver_window = tk.Tk()
            coin_silver_window.title('Manual Coin Finder')
            coin_silver_window.geometry('600x400')
            coin_silver_window.geometry('+550+250')
            silver_Label = Label(coin_silver_window, text='Is the coin mainly silver?', font=('Open Sans', 20,'bold'))
            silver_Label.place(x=180, y=20)
            img = Image.open("silver.png")
            img = ImageTk.PhotoImage(img)
            panel = tkinter.Label(coin_silver_window, image = img)
            panel.image=img
            panel.place(x=110,y=110)
            w = Canvas(coin_silver_window, width=500, height=10)
            w.create_line(0, 10, 500, 10, fill="black")
            w.place(x=50,y=60)
            silver_no_btn = Button(coin_silver_window, text='No', height=2, width=20, command=one_dollar_coin2)
            silver_yes_btn = Button(coin_silver_window, text='Yes', height=2, width=20, command=small_silver)
            silver_yes_btn.pack()
            silver_no_btn.pack()
            silver_yes_btn.place(x=380, y=350)
            silver_no_btn.place(x=30, y=350)
        # when it is silver,
        def small_silver():
            coin_silver_window.destroy()
            global silver_and_small_window
            silver_and_small_window = tk.Tk()
            silver_and_small_window.title('Manual Coin Finder')
            silver_and_small_window.geometry('600x400')
            silver_and_small_window.geometry('+550+250')
            silver_small_Label = Label(silver_and_small_window, text='Is the coin small?', font=('Open Sans', 20,'bold'))
            silver_small_Label.place(x=180,y=20)
            w = Canvas(silver_and_small_window, width=500, height=10)
            w.create_line(0, 10, 500, 10, fill="black")
            w.place(x=50,y=60)
            small_silver_no_btn = Button(silver_and_small_window, text='No', height=2, width=20, command=changi_airport_image)
            small_silver_yes_btn = Button(silver_and_small_window, text='Yes', height=2, width=20, command=ten_cent_coin)
            small_silver_yes_btn.pack()
            small_silver_yes_btn.place(x=380, y=350)
            small_silver_no_btn.pack()
            small_silver_no_btn.place(x=30, y=350)

        #when its not small but silver
        def changi_airport_image():
            silver_and_small_window.destroy()
            global changi_airport_window
            changi_airport_window = tk.Tk()
            changi_airport_window.title('Manual Coin Finder')
            changi_airport_window.geometry('600x400')
            changi_airport_window.geometry('+550+250')
            changi_airport_Label = Label(changi_airport_window,text='Does the coin have an image of Changi Airport or the number "20"?', font=('Open Sans', 15,'bold'))
            changi_airport_Label.place(x=50,y=20)
            img = Image.open("changi.png")
            img = ImageTk.PhotoImage(img)
            panel = tkinter.Label(changi_airport_window, image = img)
            panel.image=img
            panel.place(x=110,y=90)
            w = Canvas(changi_airport_window, width=500, height=10)
            w.create_line(0, 10, 500, 10, fill="black")
            w.place(x=50,y=60)
            changi_airport_no_btn = Button(changi_airport_window, text='No', height=2, width=20, command=fifty_cent_coin)
            changi_airport_yes_btn = Button(changi_airport_window, text='Yes', height=2, width=20, command=twenty_cent_coin)
            changi_airport_yes_btn.pack()
            changi_airport_yes_btn.place(x=380, y=350)
            changi_airport_no_btn.pack()
            changi_airport_no_btn.place(x=30, y=350)

        def one_dollar_coin1():
            small_gold_window.destroy()
            global yy
            yy=5
            result()
        #when its gold and small = 5 cent
        def five_cent():
            small_gold_window.destroy()
            global yy
            yy=0
            result()
        # when its not MAINLY silver,
        def one_dollar_coin2():
            coin_silver_window.destroy()
            global yy
            yy=4
            result()
        #when its small and silver
        def ten_cent_coin():
            silver_and_small_window.destroy()
            global yy
            yy=1
            result()
        #when there is no picture fo changi airport
        def fifty_cent_coin():
            changi_airport_window.destroy()
            global yy
            yy=3
            result()
        #when there is a picture of changi airport
        def twenty_cent_coin():
            changi_airport_window.destroy()
            global yy
            yy=2
            result()
        #if they choose to quit the manual coin finder
        def quit_window():
            print("quit")
            #quit the program
        def bthome():
            print("go back to main page of manual identify")

        main_start_btn = Button(text = "Let's Go!",height=2,width=20,command= gold_window)
        main_end_btn = Button(text='Back', height=2,width=20, command=quit_window)

        main_end_btn.pack()
        main_end_btn.place(x=30,y=350)
        main_start_btn.pack()
        main_start_btn.place(x=380,y=350)

        main_screen.mainloop()
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

#GAME FUNCTION
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

#LEARN FUNCTION
xx,candestroy=0,True
def learn():
    print('learn')
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

#HELP FUNCTION
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
