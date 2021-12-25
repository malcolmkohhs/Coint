import os
from typing import no_type_check
import cv2
import numpy as np
import imghdr

def main(image_name):
    coins = ["fifty_cent_old.png","five_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]
    template = cv2.imread('coin.png') #coin image
    trialgray = cv2.cvtColor(trial, cv2.COLOR_BGR2GRAY)
    trial = cv2.imread(image_name) #trialcoin image
    i=0
    for i in coins:
        coin = cv2.imread(i)
        w, h, j = template.shape
        
        res = cv2.matchTemplate(trial,coin,cv2.TM_SQDIFF)
        
        # Find min/max value and location
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        bottom_right = (min_loc[0] + w, min_loc[1] + h)
        
        # label
        cv2.rectangle(trial,min_loc, bottom_right, (0,0,255), 2)
        
        # show
        cv2.imshow(i, trial)
        cv2.waitKey(0)

while True:
    image_name=str(input("Enter the name of the image file that you would like to check for the prescence of coins.\n Do ensure that the image is in the same folder as this code.: "))
    if os.path.exists(image_name)==True:
        if imghdr.what(image_name)=="jpg" or imghdr.what(image_name)=="jpeg" or imghdr.what(image_name)=="png":
            break
        else:
            print("Re-", end="")
    else:
        print("Re-", end="")

