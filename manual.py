from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
import tkinter

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
