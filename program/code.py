from typing import no_type_check
import cv2
import numpy as np
i = 0
coins = ["fifty_cent_old.png","five_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]
trial = cv2.imread('trial_coin.png') #trialcoin image
template = cv2.imread('coin.png') #coin image
trialgray = cv2.cvtColor(trial, cv2.COLOR_BGR2GRAY)

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

print("hello world")