import os
from typing import no_type_check
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import imghdr
from datetime import date

def main(image_name): #main algo to determine the coin in img
    i = 0

    coins = ["fifty_cent_old.png","five_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]

    while True:
        img_org = cv2.imread(image_name,1)
        img_org_1 = cv2.resize(img_org,(433,577))
        img_changed_2 = cv2.imread(coins[i],0)
        s = ssim(img_org_1, img_changed_2,  multichannel=True)
        if s > 0.9:
            return coins[i],s
        i += 1
while True:
    while True: #check if the image is present and the formatting
        image_name=str(input("Enter the name of the image file that you would like to check for the prescence of coins.\n Do ensure that the image is in the same folder as this code.: "))
        if os.path.exists(image_name)==True:
            if imghdr.what(image_name)=="jpg" or imghdr.what(image_name)=="jpeg" or imghdr.what(image_name)=="png":
                break
            else:
                print("Re-", end="")
        else:
            print("Re-", end="")

    while True: #validation check of cost price
        print("The cost of the product you are buying. Enter the following number to enter the kind of value for the item.")
        print("1: Dollars ($)\n2: Cents (¢)\n3: No cost to enter.")
        option_cost=input()
        item_cost=0
        if option_cost.isdigit()==False or int(option_cost)<1 or int(option_cost)>3:
            print("Invalid format/ number, please re-enter. Thank you!")
        else:
            break
    while True:
        if int(option_cost)==3:
            break
        sign="Dollars ($)"
        if int(option_cost)==2:
            sign="Cents (¢)"
        item_cost=input("Enter the cost of your item in {}: ".format(sign))
        alpha,decimal=0,0
        for i in str(item_cost):
            if i.isalpha()==True:
                alpha+=1
            if i==".":
                decimal+=1
        if alpha>0 or decimal>1:
            print("The entered cost is incorrect. Please Re-",end="")
        else:
            break
    if option_cost==1 or option_cost==2: #get name of item to write to file
        item_bought=str(input("Name of item bought: "))

    return_values=main(image_name)
    coint_true=return_values[0] #coin identified thru algo
    coins=["five","ten","twenty","fifty","one"]
    coins_real,temp=["five cent (5¢)","ten cent (10¢)","twenty cent (20¢)","fifty cent (50¢)","one dollar ($1)"],0
    coins_value=[0.05,0.1,0.2,0.5,1]
    for i in range (int(len(coins))): #find value of found coin
        if coint_true.find(coins[i])>-1:
            coint_true=coins_value[i]
            temp=i
            break
    if coint_true==None:
        print("No coin was identified in the image. Please upload an image with a coin in it.")
    else:
        if option_cost==2:
            ditem_cost=item_cost/100
        change= float(ditem_cost)-coint_true
        if option_cost==2:
            coint_true*=100
        if option_cost==1 and str(change).find(".")>-1:
            x,y=change.split(".")
            if len(y)==1:
                change=str(change)
                change+="0"
    print("In the image, a {} coin has been identified, with an accuracy of {}%.".format(coins_real[temp],int(return_values[1]*100)))
    if option_cost!=3:
        print("Cost of your item: {}({})\n Value of coin in image: {}({})".format(item_cost,sign[::-1][1],coint_true,sign[::-1][1]))
        if change<0:
            print("You do have enough money to pay for the item. You would need {}({}) more.".format(change,sign[::-1][1]))
        elif change==0:
            print("You have just enough money to pay the item. You will not receive any change.")
        else:
            print("You have more than enough moeny to pay for the item. You would receive a change of {}({}).".format(change,sign[::-1][1]))
    print("\n---------------\nWould you like to input another image?\nEnter the following number for your answer\n1: Yes\n2: No")
    while True:
        xxx=str(input())
        if xxx!="1" or xxx!="2":
            print("Invalid input, please enter a valid input. Refer to as above^. Thank you.")
        else:
            break
    if xxx=="2":
        print("You have exited the program. Thank you and goodbye! :)")
        break
    break
