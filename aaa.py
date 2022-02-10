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
import tkinter
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk #to display image
from imutils import perspective
from imutils import contours #to check for contours/ object detect
import numpy as np #for arrays
import cv2 
import imutils
import cv2 as cv #opencv
from skimage.metrics import structural_similarity as ssim #ssim comparison 

newfont = ("Open Sans", 20)

#IDENTIFY FUNCTION
yy=0
imagefile="" #set string variable for the imagefile
coind,perc=[],[]
def coinidentification():
    #automatic function
    def auto():
        #Main page/ front page
        newfont = ("Open Sans", 20,"bold")
        newfont1 = ("Open Sans",15)
        canvas = tk.Toplevel()
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
        width=20,command = lambda:upload_file()) #button to upload file
        b1.place(x=220,y=60)
        yourimg = Image.open("yourimg.jpeg") #load image
        yourimg = yourimg.resize((100, 100))
        yourimg = ImageTk.PhotoImage(yourimg)
        l4 = tk.Label(canvas, image=yourimg)
        l4.image = yourimg
        l4.place(x=220,y=100)
        l5 = tk.Label(canvas,text="Upload and identify here",font=newfont1)
        l5.place(x=200,y=310)
        l6 = tk.Label(canvas, text="Please enter numbers only. Leave blank if you have no cost value.\nDecimal is allowed for dollars ($) with no spaces.                           ",font=("Open Sans",10,"italic"))
        l6.place(x=220,y=260)
        l8 = tk.Label(canvas,text="Upload an image with a coin and identify it with a click!",font=("Open Sans",12))
        l8.place(x=170,y=30)

        

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
            imagefile=StringVar()
            f_types = [('Jpg Files', '*.jpg'),
            ('PNG Files','*.png'),
            ('Jpeg Files','*.jpeg')]   # type of files accepted only
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
        drop = OptionMenu(canvas, clicked, *options) #dropdown menu
        drop.pack(pady=20)
        drop.place(x=220,y=215)
        costin=StringVar()
        costinp=tk.Entry(canvas,textvariable=costin)
        costinp.place(x=220,y=235)

        #=== Validation check for input of image/ input for the cost ===
        def submit1():
                global imagefile
                a=False
                inputs=str(costin.get()).split(".") 
                if len(inputs)<3: #if dollar sign, only can have one decimal
                    for i in inputs:
                        if str(i).isdigit()==True: #check for alpha, return false
                            a=True
                        else:
                            a=False
                            break
                if costin.get()=="": #no cost input
                    a=True
                if len(inputs)>1 and clicked.get()=="Cents (¢)": #cents cannot have decimal
                    a=False
                if str(imagefile)!="":
                    if str(imagefile)[0]!="(": #check if there is any image input
                        a=False
                return a

        # === WINDOW WHEN NO OBJECT/ COIN DETECTED ===
        def nothing(): 
            canvas.destroy()
            resultf=tk.Toplevel()
            resultf.title("Coint: Computer Identification Result")
            resultf.geometry("600x400") #window dimension
            resultf.geometry("+550+250") #making the window centre
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

        # === WINDOW WHEN A COIN/ OBJECT IS FOUND ===
        def something():
            canvas.destroy()
            global coind, perc
            resultp=tk.Toplevel()
            resultp.title("Coint: Computer Identification Result")
            resultp.geometry("600x400") #window dimension
            resultp.geometry("+550+250") #making the window centre
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
            tperccopy=totalperc.copy()
            tperccopy.sort()
            tperccopy=tperccopy[::-1]
            for i in tperccopy:
                x=totalperc.index(i)
                totalpos.append(coinlist[x])
                totalperc[x]="i"
                totalpos.append(i)
            ans=str(totalpos[0]).split("_") #convert image filename to strname for display
            ansstr=""
            perans=round(totalpos[1]*100,2) #percentage for display
            perans=str(perans)
            for i in range (len(ans)): #convert image filename to strname for display
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
            inpimg = ImageTk.PhotoImage(inpimg) #display input image
            inppanel = tkinter.Label(resultp, image = inpimg)
            inppanel.image=inpimg
            inppanel.place(x=40,y=115)
            
            ansimgn=str(totalpos[0])+"0.png" #display coin indetified image
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
            des=open("coindesc.txt") #txt file for all the coins
            descon=des.readlines()
            num=acoin.index(totalpos[0])
            if num>4:
                num-=5
            desc=descon[num] #line for desc of the coin found
            des.close()
            descl=tk.Label(resultp,text=desc,wraplength=270,justify="left",font=("Open Sans",14))
            descl.place(x=300,y=140)
            coinv=[0.05,0.10,0.20,0.50,1.00]
            formcost=coinv[num]
            inputcost=costin.get() #get the input cost format d/c and the value
            formatcost=clicked.get()
            textcost=""
            changecost,colour1,changing,dol,cen=0,"blue","Change: ","$","¢"
            inputcosttemp=inputcost
            if inputcost!="":
                if formatcost=="Cents (¢)":
                    inputcost=float(inputcost)
                    inputcost/=100 #change to dollars first for calculations
                    dol="" #set to nothing as cents is set
                if formatcost=="Dollars ($)":
                    cen="" #set to nothing as dollar is set
                    if str(inputcost).find(".")>0:
                        inputcost=str(inputcost)
                        if len(inputcost[inputcost.find(".")+1:])<2:
                            inputcost+="0" #leading zero
                changecost=float(formcost)-float(inputcost) #calculate dif
                if changecost==0:
                    textcost="You have just enough money."
                elif changecost>0:
                    textcost="You will receive change."
                else:
                    textcost="You do not have enough money."
                    colour1="#ff7700"
                    changing="Short of: "
                changecost=abs(round(changecost,2)) #change to positive number
                if formatcost=="Cents (¢)":
                    inputcost=inputcosttemp
                    changecost*=100 #conver back to cents
                    changecost=int(changecost)
                elif str(changecost).find(".")>0:
                    changecost=str(changecost)
                    if len(changecost[changecost.find(".")+1:])<2:
                        changecost+="0" #leading zero

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
            for i in range(10): #to arrange the top 5 coins and values into the lists namecoin5 and valuecoin5
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
            

        # === ALGO TO IDENTIFY IMG ====
        def algo(imginput):
            global coind, perc
            while True:
                    # change image to black and white
                    image = cv2.imread(imginput)
                    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    gray = cv2.GaussianBlur(gray, (7, 7), 0)
                    # find the edges in the image
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
                    # sort contours based on the array and their coord
                    (cnts, _) = contours.sort_contours(cnts)
                    colors = ((0, 0, 255), (240, 0, 159), (255, 0, 0), (255, 255, 0))
                    coord,area,coordmax=[],[],[]
                    for (i, c) in enumerate(cnts): #goes through all the contours 1 by 1
                            if cv2.contourArea(c) < 1000: #if area too small, ignore
                                    continue
                            # draw contours
                            box = cv2.minAreaRect(c)
                            if imutils.is_cv2():
                                box = cv2.cv.BoxPoints(box)
                            else:
                                box = cv2.boxPoints(box)
                            box = np.array(box, dtype="int")
                            cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
                            area.append(cv2.contourArea(c)) #append the coordinates and area of the boundaries for comparison and comparing later
                            coord.append(box.astype("int"))
                    if len(area)>5: #want top 5 area covered
                            areatemp=area.copy()
                            areatemp.sort() #sorts area covered
                            areatemp=areatemp[::-1]
                            for i in range (5):
                                    coordmax.append(coord[area.index(areatemp[i])]) #finds the top 5 largest areas coordinates
                    else:
                            coordmax=coord
                    if len(coord)==0: #BREAK, no significant object detected, where no objects are even found, break
                            nothing()
                            break
                    x_coord,y_coord=[],[]
                    for i in coordmax:
                            for c in i:
                                    c=str(c)
                                    c=c[1:(len(c)-1)]
                                    x,y=c.split()
                                    x_coord.append(int(x))
                                    y_coord.append(int(y)) #sorts the x and y coordinates of each boundary

                    # === CROPPING IMAGE TO FIT OBJECT/ COIN ===
                    orgimg = cv2.imread(imginput)
                    points=[min(y_coord),max(y_coord), min(x_coord),max(x_coord)]
                    for i in range (4):
                            if i==0 or i==2:
                                    if points[i]<0: #if coordinate is outside the image, set to zero
                                            points[i]=0
                            elif i==1: #if coordinate is outside image, set to the max height of image
                                    if points[1]>orgimg.shape[1]:
                                            points[1]=orgimg.shape[1]
                            elif i==3: #if coorfinate is outside image, set to max width of image
                                    if points[3]>orgimg.shape[0]:
                                            points[3]=orgimg.shape[0]
                    cropped_image = orgimg[points[0]:points[1], points[2]:points[3]] #crop image
                    cv2.imwrite("cropimg.png", cropped_image)

                    # === LOOK FOR CIRCLE --> COIN ===
                    cimg=cv2.imread("cropimg.png")
                    gray = cv2.cvtColor(cimg, cv.COLOR_BGR2GRAY) #change to black and white
                    gray = cv.medianBlur(gray, 5)
                    rows = gray.shape[0]
                    rad=int(0.4*min(cimg.shape[:2])) #minimum radius is 40% of the smallest side of the image
                    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                                            param1=100, param2=30,
                                            minRadius=rad, maxRadius=rad+50) #look for circles with radius of sort
                    if circles is not None: #if there are circles
                            # === COMPARE IMAGE WITH DATA BASE ===
                            x=[]
                            coinsrank=[]
                            fivo,teno,tweo,fifo,oneo=(['five_cent_old0.png','five_cent_old1.png', 'five_cent_old2.png', 'five_cent_old3.png', 'five_cent_old4.png', 'five_cent_old5.png']),(['ten_cent_old0.png','ten_cent_old1.png', 'ten_cent_old2.png', 'ten_cent_old3.png', 'ten_cent_old4.png', 'ten_cent_old5.png']),(['twenty_cent_old0.png','twenty_cent_old1.png', 'twenty_cent_old2.png', 'twenty_cent_old3.png', 'twenty_cent_old4.png']),(['fifty_cent_old0.png','fifty_cent_old1.png', 'fifty_cent_old2.png', 'fifty_cent_old3.png', 'fifty_cent_old4.png']),(['one_dollar_old0.png','one_dollar_old1.png', 'one_dollar_old2.png', 'one_dollar_old3.png', 'one_dollar_old4.png', 'one_dollar_old5.png'])
                            fiv,ten,twe,fif,one=(['five_cent0.png','five_cent1.png', 'five_cent2.png', 'five_cent3.png', 'five_cent4.png']),(['ten_cent0.png','ten_cent1.png', 'ten_cent2.png', 'ten_cent3.png', 'ten_cent4.png']),(['twenty_cent0.png','twenty_cent1.png', 'twenty_cent2.png', 'twenty_cent3.png', 'twenty_cent4.png', 'twenty_cent5.png']),(['fifty_cent0.png','fifty_cent1.png', 'fifty_cent2.png', 'fifty_cent3.png']),(['one_dollar0.png','one_dollar1.png', 'one_dollar2.png', 'one_dollar3.png', 'one_dollar4.png'])
                            random.shuffle(fivo) #randomly shuffle the lists
                            random.shuffle(teno)
                            random.shuffle(tweo)
                            random.shuffle(fifo)
                            random.shuffle(oneo)
                            random.shuffle(fiv)
                            random.shuffle(ten)
                            random.shuffle(twe)
                            random.shuffle(fif)
                            random.shuffle(one)
                            #randomly get the images to compare with
                            coins = [fivo[0],fivo[3],teno[1],teno[2],tweo[3],tweo[2],fifo[2],fifo[1],oneo[0],oneo[3],fiv[2],fiv[0],ten[1],ten[2],twe[1],twe[0],fif[3],fif[2],one[2],one[1]]
                            for i in range (20):
                                img_org=cv2.imread("cropimg.png")
                                img_org_1=cv2.resize(img_org, (500, 500)) #resize the dimenssions
                                img_test=cv2.imread(coins[i])
                                img_test_1=cv2.resize(img_test, (500, 500)) #resize the dimenssions
                                s = ssim(img_org_1, img_test_1,  multichannel=True) #ssim test
                                x.append(s)
                            y=x.copy()
                            y.sort()
                            for i in y:
                                coinsrank.append(coins[x.index(i)]) #link the coin file name with their calculated ssim value that is arranged in descending order
                            coind=coinsrank[::-1]
                            perc=y[::-1]
                            something()

                    else:
                            nothing()         
                    break

        def submit():
            ltrue=tk.Label(canvas,text="                     Entries accepted!                               ",fg="blue",font=("Open Sans",15))
            ltrue.place(x=145,y=365)
            print(imagefile)
            if submit1()==True: #input pass
                algo(imagefile[0])
            elif submit1()==False: #input fail
                l7=tk.Label(canvas,text="Invalid entries. Please try again, thank you!",fg="#ff7700",font=("Open Sans",15))
                l7.place(x=160,y=365)
                
            
        b2 = tk.Button(canvas, text="Identify and calculate!",command=submit)
        b2.place(x=205,y=335)

        canvas.mainloop()

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
            global yy,coinsmain1
            coinslist=["Five Cent","Ten Cent","Twenty Cent","Fifty Cent","One Dollar"]
            coinsimglist=["five_cent","ten_cent","twenty_cent","fifty_cent","one_dollar"]
            coinsvalue=["0.05","0.10","0.20","0.50","1"]
            coinsmain1=tk.Toplevel()
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
            new_gold = tk.Toplevel()
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
            small_gold_window = tk.Toplevel()
            small_gold_window.title('Manual Coin Finder')
            small_gold_window.geometry('600x400')
            small_gold_window.geometry('+550+250')
            small_gold_window_label = Label(small_gold_window, text="Is the coin small?", font=('Open Sans', 20,'bold'))
            small_gold_window_label.place(x=190,y=20)
            img = Image.open("shsmall.png")
            img = ImageTk.PhotoImage(img)
            panel = tkinter.Label(small_gold_window, image = img)
            panel.image=img
            panel.place(x=120,y=110)
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
            coin_silver_window = tk.Toplevel()
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
            silver_and_small_window = tk.Toplevel()
            silver_and_small_window.title('Manual Coin Finder')
            silver_and_small_window.geometry('600x400')
            silver_and_small_window.geometry('+550+250')
            silver_small_Label = Label(silver_and_small_window, text='Is the coin small?', font=('Open Sans', 20,'bold'))
            silver_small_Label.place(x=180,y=20)
            img = Image.open("shsmall.png")
            img = ImageTk.PhotoImage(img)
            panel = tkinter.Label(silver_and_small_window, image = img)
            panel.image=img
            panel.place(x=120,y=110)
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
            changi_airport_window = tk.Toplevel()
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
            main_screen.destroy()
            #quit the program
        def bthome():
            coinsmain1.destroy()

        main_start_btn = Button(main_screen,text = "Let's Go!",height=2,width=20,command= gold_window)
        main_end_btn = Button(main_screen,text='Back', height=2,width=20, command=quit_window)

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
    mainl.place(x=270,y=20)
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
    bgo.place(x=350,y=350)
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