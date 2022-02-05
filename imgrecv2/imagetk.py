import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import tkinter
import time
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import cv2
import imutils
import sys
import cv2 as cv
from typing import no_type_check
from skimage.metrics import structural_similarity as ssim
import imghdr
import random

newfont = ("Open Sans", 20,"bold")
newfont1 = ("Open Sans",15)
canvas = tk.Tk()
canvas.geometry("600x400")  # Size of the window
canvas.geometry("+550+250")
l1 = tk.Label(canvas,text='Enter your image here:')  
l1.place(x=20,y=60)
l1.configure(font=newfont1)
l2 = tk.Label(canvas,text='Computer Identification')
l2.place(x=180,y=0)
l2.configure(font=newfont)
l3=tk.Label(canvas,text="Cost of product (Optional): ")
l3.place(x=20,y=210)
l3.configure(font=newfont1)
b1 = tk.Button(canvas, text='Upload Image', 
   width=20,command = lambda:upload_file())
b1.place(x=220,y=60)
yourimg = Image.open("yourimg.jpeg") #load image
yourimg = yourimg.resize((100, 100))
yourimg = ImageTk.PhotoImage(yourimg)
l4 = Label(image=yourimg)
l4.image = yourimg
l4.place(x=220,y=100)
l5 = tk.Label(canvas,text="Upload and identify here",font=newfont1)
l5.place(x=200,y=310)
l6 = tk.Label(canvas, text="Please enter numbers only. Leave blank if you have no cost value.\nDecimal is allowed for dollars ($) with no spaces.                           ",font=("Open Sans",10,"italic"))
l6.place(x=220,y=260)
l8 = tk.Label(canvas,text="Upload an image with a coin and identify it with a click!",font=("Open Sans",12))
l8.place(x=170,y=30)

imagefile=StringVar()
coind,perc=[],[]

#GO TO OTHER PAGES DIRECTORIES
def mani():
    # GO TO MANUAL IDENTIFICATION PAGE ***
    print("manuali")
def reent():
    # GO TO COMP IMG RECOG PAGE ***
    print("reent")
def bthome():
    #GO TO HOME PAGE/ MAINAPP ***
    print("go back home")
    

def upload_file():
    global imagefile #takes in variable from outside function
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png'),
    ('Jpeg Files','*.jpeg')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)
    imagefile = filename #flename
    for f in filename:
        img=Image.open(f) # read the image file
        img=img.resize((100,100)) # new width & height of image (to resize and fit)
        img=ImageTk.PhotoImage(img)
        e1 =tk.Label(canvas)
        e1.place(x=220,y=100)
        e1.image = img
        e1['image']=img

#dropdown menu for cents or dollars
options = ["Dollars ($)", "Cents (¢)"]        
clicked=StringVar()
clicked.set(options[0])
drop = OptionMenu(canvas, clicked, *options)#,command=selected)
drop.pack(pady=20)
drop.place(x=220,y=215)
costin=StringVar()
costinp=tk.Entry(canvas,textvariable=costin)
costinp.place(x=220,y=235)
def submit1():
        global imagefile
        a=False
        inputs=str(costin.get()).split(".")
        if len(inputs)<3:
            for i in inputs:
                if str(i).isdigit()==True:
                    a=True
                else:
                    a=False
                    break
        if costin.get()=="":
            a=True
        if len(inputs)>1 and clicked.get()=="Cents (¢)":
            a=False
        if str(imagefile)!="":
            if str(imagefile)[0]!="(": #check if there is any image input
                a=False
        return a

def nothing(): #NO COIN DETECTED #maybe need to overlay instead
    canvas.destroy()
    resultf=tk.Tk()
    resultf.title("Coint: Computer Identification Result")
    resultf.geometry("600x400") #window dimension
    resultf.geometry("+550+250") #making the window centre #!!!
    lhead = tk.Label(resultf,text='Computer Identification',font=("Open Sans",20,"bold"))
    lhead.place(x=180,y=0)
    errimg = Image.open("coinerror.png")
    errimg = errimg.resize((380, 300))
    errimg = ImageTk.PhotoImage(errimg)
    errpanel = tkinter.Label(resultf, image = errimg)
    errpanel.image=errimg
    errpanel.place(x=115,y=35)
    lsub = tk.Label(resultf,text='----  RESULT  ----',font=("Open Sans",15))
    lsub.place(x=250,y=25)
    lsub1 = tk.Label(resultf, text="Identify a coin maunally",font=("Open Sans",14))
    lsub1.place(x=30,y=325)
    lsub2 = tk.Label(resultf, text="Re-upload another image",font=("Open Sans",14))
    lsub2.place(x=220,y=325)
    lsub3 = tk.Label(resultf, text="Go back to mainpage",font=("Open Sans",14))
    lsub3.place(x=430,y=325)
    manb = tk.Button(resultf, text = 'Manual Identification', width=15, command=lambda:mani())
    manb.place(x=30,y=350)
    reb = tk.Button(resultf, text = 'Identify Another', width=15, command=lambda:reent())
    reb.place(x=220,y=350)
    gbackb = tk.Button(resultf, text = 'Back To Home', width=15, command=lambda:bthome())
    gbackb.place(x=420,y=350)
    resultf.mainloop()

def something(): #COIN DETECTED
    canvas.destroy()
    global coind
    global perc
    global errpanel
    resultp=tk.Tk()
    resultp.title("Coint: Computer Identification Result")
    resultp.geometry("600x400") #window dimension
    resultp.geometry("+550+250") #making the window centre #!!!
    lhead = tk.Label(resultp,text='Computer Identification',font=("Open Sans",20,"bold"))
    lhead.place(x=180,y=0)
    bgimg = Image.open("backrec.png")
    bgimg = bgimg.resize((540, 60))
    bgimg = ImageTk.PhotoImage(bgimg)
    bgpanel = tkinter.Label(resultp, image = bgimg)
    bgpanel.image=bgimg
    bgpanel.place(x=30,y=51)
    lsub = tk.Label(resultp,text='----  RESULT  ----',font=("Open Sans",15))
    lsub.place(x=250,y=30)
    totalperc=[0,0,0,0,0,0,0,0,0,0]#start from fiveold to one new
    coinlist=['five_cent_old','ten_cent_old','twenty_cent_old','fifty_cent_old','one_dollar_old','five_cent','ten_cent','twenty_cent','fifty_cent','one_dollar']
    totalpos,pos=[],[]
    for i in coind:
            pos=0
            for x in coinlist:
                    if i[:len(i)-5] == x:
                            totalperc[pos]+=perc[coind.index(i)]
                            break
                    else:
                            pos+=1
    #print(totalperc)
    tperccopy=totalperc.copy()
    tperccopy.sort()
    tperccopy=tperccopy[::-1]
    for i in tperccopy:
        x=totalperc.index(i)
        totalpos.append(coinlist[x])
        totalperc[x]="i"
        totalpos.append(i)
    #print(totalpos)
    ans=str(totalpos[0]).split("_")
    ansstr=""
    perans=round(totalpos[1]*100,2)
    #print(perans)
    perans=str(perans)
    for i in range (len(ans)):
        ans[i]=str(ans[i]).capitalize()
    if len(ans)==3:
        ans[2]="(Old)"
    else:
        ans.append("(New)")
    for i in ans:
        ansstr+=i+" "
    lans= tk.Label(resultp,text=ansstr,font=("Open Sans",18,"bold"),fg="white",bg="#f0a03b")
    lans.place(x=240,y=55)
    lans= tk.Label(resultp,text=(perans+" %"),font=("Open Sans",15),fg="white",bg="#f0a03b")
    lans.place(x=270,y=80)

    inpimg = Image.open(imagefile[0])
    inpimg = inpimg.resize((120, 120))
    inpimg = ImageTk.PhotoImage(inpimg)
    inppanel = tkinter.Label(resultp, image = inpimg)
    inppanel.image=inpimg
    inppanel.place(x=40,y=115)
    
    ansimgn=str(totalpos[0])+"0.png"
    ansimg = Image.open(ansimgn)
    ansimg = ansimg.resize((120, 120))
    ansimg = ImageTk.PhotoImage(ansimg)
    anspanel = tkinter.Label(resultp, image = ansimg)
    anspanel.image=ansimg
    anspanel.place(x=170,y=115)
    imgsl= tk.Label(resultp,text="Your Image                     Coin Identified",font=("Open Sans",10))
    imgsl.place(x=70,y=236)
    resl = tk.Label(resultp,text=ansstr,font=("Open Sans",15,"bold"))
    resl.place(x=300,y=115)
    lines=[3,7,11,15,19]
    acoin=['five_cent','ten_cent','twenty_cent','fifty_cent','one_dollar','five_cent_old','ten_cent_old','twenty_cent_old','fifty_cent_old','one_dollar_old']
    des=open("coindesc.txt")
    descon=des.readlines()
    num=acoin.index(totalpos[0])
    if num>4:
        num-=5
    desc=descon[num]
    des.close()
    descl=tk.Label(resultp,text=desc,wraplength=270,justify="left",font=("Open Sans",14))
    descl.place(x=300,y=140)
    coinv=[0.05,0.10,0.20,0.50,1.00]
    formcost=coinv[num]
    inputcost=costin.get()
    formatcost=clicked.get()
    textcost=""
    changecost,colour1,changing,dol,cen=0,"blue","Change: ","$","¢"
    inputcosttemp=inputcost
    if inputcost!="":
        if formatcost=="Cents (¢)":
            inputcost=float(inputcost)
            inputcost/=100
            dol=""
        if formatcost=="Dollars ($)":
            cen=""
            if str(inputcost).find(".")>0:
                inputcost=str(inputcost)
                if len(inputcost[inputcost.find(".")+1:])<2:
                    inputcost+="0"
        changecost=float(formcost)-float(inputcost)
        if changecost==0:
            textcost="You have just enough money."
        elif changecost>0:
            textcost="You will receive change."
        else:
            textcost="You do not have enough money."
            colour1="#ff7700"
            changing="Short of: "
        changecost=abs(round(changecost,2))
        if formatcost=="Cents (¢)":
            inputcost=inputcosttemp
            changecost*=100
            changecost=int(changecost)
        elif str(changecost).find(".")>0:
            changecost=str(changecost)
            if len(changecost[changecost.find(".")+1:])<2:
                changecost+="0"
        
        #print("{}\n{}\n{}\n{}\n{}".format(formcost,inputcost,formatcost,textcost,changecost))
        cosl = tk.Label(resultp,text="Balance",font=("Open Sans",15,"bold"))
        cosl.place(x=300,y=260)
        inpcostl=tk.Label(resultp,text=("Cost Input: "+dol+str(inputcost)+cen),font=("Open Sans",14))
        inpcostl.place(x=300,y=280)
        outcostl=tk.Label(resultp,text=(changing+dol+str(changecost)+cen),font=("Open Sans",14))
        outcostl.place(x=300,y=303)
        outtxtl=tk.Label(resultp,text=textcost,fg=colour1,font=("Open Sans",14,"bold"))
        outtxtl.place(x=300,y=325)
    otherposl=tk.Label(resultp,text="Other Possibilities",font=("Open Sans",15,"bold"))
    otherposl.place(x=30,y=255)
    namecoin5,valcoin5=[],[]
    for i in range(10):
        if i%2==0:
            ans5=str(totalpos[i]).split("_")
            ansstr5=""
            for i in range (len(ans5)):
                ans5[i]=str(ans5[i]).capitalize()
            if len(ans5)==3:
                ans5[2]="(Old)"
            else:
                ans5.append("(New)")
            for i in ans5:
                ansstr5+=i+" "
            namecoin5.append(ansstr5)
        elif i%2==1:
            perc5=round(totalpos[i]*100,2)
            perc5=str(perc5)+" %"
            valcoin5.append(perc5)
    otherpos1=tk.Label(resultp,text=("1. "+namecoin5[0]+": "+valcoin5[0]),font=("Open Sans",11))
    otherpos1.place(x=30,y=275)
    otherpos1=tk.Label(resultp,text=("2. "+namecoin5[1]+": "+valcoin5[1]),font=("Open Sans",11))
    otherpos1.place(x=30,y=293)
    otherpos1=tk.Label(resultp,text=("3. "+namecoin5[2]+": "+valcoin5[2]),font=("Open Sans",11))
    otherpos1.place(x=30,y=311)
    otherpos1=tk.Label(resultp,text=("4. "+namecoin5[3]+": "+valcoin5[3]),font=("Open Sans",11))
    otherpos1.place(x=30,y=329)
    otherpos1=tk.Label(resultp,text=("5. "+namecoin5[4]+": "+valcoin5[4]),font=("Open Sans",11))
    otherpos1.place(x=30,y=347)
    manb = tk.Button(resultp, text = 'Manual Identification', width=15, command=lambda:mani())
    manb.place(x=30,y=368)
    reb = tk.Button(resultp, text = 'Identify Another Coin', width=15, command=lambda:reent())
    reb.place(x=220,y=368)
    gbackb = tk.Button(resultp, text = 'Back To Home', width=15, command=lambda:bthome())
    gbackb.place(x=420,y=368)
    

# ALGO TO IDENTIFY IMG
def algo(imginput):
    global coind
    global perc
    while True:
            # load image, black and white
            image = cv2.imread(imginput)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            gray = cv2.GaussianBlur(gray, (7, 7), 0)
            # detect the edges of object
            edged = cv2.Canny(gray, 50, 100)
            edged = cv2.dilate(edged, None, iterations=1)
            edged = cv2.erode(edged, None, iterations=1)
            #find contours
            cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            
            if len(cnts)==0: #BREAK, NO OBJECT detected (e.x. plain black colour pic)
                    nothing()
                    break
            # sort the contours
            (cnts, _) = contours.sort_contours(cnts)
            colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))
            coord,area,coordmax=[],[],[]
            for (i, c) in enumerate(cnts):
                    if cv2.contourArea(c) < 1000: #if area too small, ignore
                            continue
                    # draw contours
                    box = cv2.minAreaRect(c)
                    box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
                    box = np.array(box, dtype="int")
                    cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
                    area.append(cv2.contourArea(c))
                    coord.append(box.astype("int"))
            if len(area)>5: #want top 5 area covered
                    areatemp=area.copy()
                    areatemp.sort() #sorts area covered
                    areatemp=areatemp[::-1]
                    for i in range (5):
                            coordmax.append(coord[area.index(areatemp[i])])
            else:
                    coordmax=coord
            if len(coord)==0: #BREAK, no significant object detected, break
                    nothing()
                    break
            x_coord,y_coord=[],[]
            for i in coordmax:
                    for c in i:
                            c=str(c)
                            c=c[1:(len(c)-1)]
                            x,y=c.split()
                            x_coord.append(int(x))
                            y_coord.append(int(y))

            # === CROPPING IMAGE TO FIT OBJECT/ COIN ===
            orgimg = cv2.imread(imginput)
            points=[min(y_coord),max(y_coord), min(x_coord),max(x_coord)]
            for i in range (4):
                    if i==0 or i==2:
                            if points[i]<0:
                                    points[i]=0
                    elif i==1:
                            if points[1]>orgimg.shape[1]:
                                    points[1]=orgimg.shape[1]
                    elif i==3:
                            if points[3]>orgimg.shape[0]:
                                    points[3]=orgimg.shape[0]
            cropped_image = orgimg[points[0]:points[1], points[2]:points[3]]
            cv2.imwrite("cropimg.png", cropped_image)

            # === LOOK FOR CIRCLE --> COIN ===
            cimg=cv2.imread("cropimg.png")
            gray = cv2.cvtColor(cimg, cv.COLOR_BGR2GRAY)
            gray = cv.medianBlur(gray, 5)
            rows = gray.shape[0]
            rad=int(0.4*min(cimg.shape[:2]))
            circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                                       param1=100, param2=30,
                                       minRadius=rad, maxRadius=rad+50)
            if circles is not None:
                    circles = np.uint16(np.around(circles))
                    #print("coin found")
                    # === COMPARE IMAGE WITH DATA BASE ===
                    x=[]
                    coinsrank=[]
                    fivo,teno,tweo,fifo,oneo=(['five_cent_old0.png','five_cent_old1.png', 'five_cent_old2.png', 'five_cent_old3.png', 'five_cent_old4.png', 'five_cent_old5.png']),(['ten_cent_old0.png','ten_cent_old1.png', 'ten_cent_old2.png', 'ten_cent_old3.png', 'ten_cent_old4.png', 'ten_cent_old5.png']),(['twenty_cent_old0.png','twenty_cent_old1.png', 'twenty_cent_old2.png', 'twenty_cent_old3.png', 'twenty_cent_old4.png']),(['fifty_cent_old0.png','fifty_cent_old1.png', 'fifty_cent_old2.png', 'fifty_cent_old3.png', 'fifty_cent_old4.png']),(['one_dollar_old0.png','one_dollar_old1.png', 'one_dollar_old2.png', 'one_dollar_old3.png', 'one_dollar_old4.png', 'one_dollar_old5.png'])
                    fiv,ten,twe,fif,one=(['five_cent0.png','five_cent1.png', 'five_cent2.png', 'five_cent3.png', 'five_cent4.png']),(['ten_cent0.png','ten_cent1.png', 'ten_cent2.png', 'ten_cent3.png', 'ten_cent4.png']),(['twenty_cent0.png','twenty_cent1.png', 'twenty_cent2.png', 'twenty_cent3.png', 'twenty_cent4.png', 'twenty_cent5.png']),(['fifty_cent0.png','fifty_cent1.png', 'fifty_cent2.png', 'fifty_cent3.png']),(['one_dollar0.png','one_dollar1.png', 'one_dollar2.png', 'one_dollar3.png', 'one_dollar4.png'])
                    random.shuffle(fivo) #randomly shuffle
                    random.shuffle(teno)
                    random.shuffle(tweo)
                    random.shuffle(fifo)
                    random.shuffle(oneo)
                    random.shuffle(fiv)
                    random.shuffle(ten)
                    random.shuffle(twe)
                    random.shuffle(fif)
                    random.shuffle(one)
                    coins = [fivo[0],fivo[3],teno[1],teno[2],tweo[3],tweo[2],fifo[2],fifo[1],oneo[0],oneo[3],fiv[2],fiv[0],ten[1],ten[2],twe[1],twe[0],fif[3],fif[2],one[2],one[1]]
                    for i in range (20):
                        img_org=cv2.imread("cropimg.png")
                        img_org_1=cv2.resize(img_org, (500, 500)) #resize the dimenssions
                        img_test=cv2.imread(coins[i])
                        img_test_1=cv2.resize(img_test, (500, 500)) #resize the dimenssions
                        s = ssim(img_org_1, img_test_1,  multichannel=True)
                        x.append(s)
                    #print("=== Results ===")
                    y=x.copy()
                    y.sort()
                    for i in y:
                        coinsrank.append(coins[x.index(i)])
                    #for i in range (20):
                        #print("{}. {}: {} %".format(i+1, coinsrank[19-i], format(float(y[19-i]*100),".2f")))
                    coind=coinsrank[::-1]
                    perc=y[::-1]
                    something()

            else:
                    nothing()         
            break

def submit():
    ltrue=tk.Label(canvas,text="                     Entries accepted!                               ",fg="blue",font=("Open Sans",15))
    ltrue.place(x=145,y=365)
    if submit1()==True: #input pass
        algo(imagefile[0])
    elif submit1()==False: #input fail
        l7=tk.Label(canvas,text="Invalid entries. Please try again, thank you!",fg="#ff7700",font=("Open Sans",15))
        l7.place(x=160,y=365)
        
    
b2 = tk.Button(canvas, text="Identify and calculate!",command=submit)
b2.place(x=205,y=335)

canvas.mainloop()  # Keep the window open
