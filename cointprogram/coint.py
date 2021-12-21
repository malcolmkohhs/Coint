from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
same = False
i = 0 

'''
1. change all images to grey #src = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
2. find height and width of source shape #height, width =src.shape
3. find height and width of temp shape #H, W = temp.shape

'''
coins = ["fifty_cent_old.png","five_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]

temp = cv2.imread("trial_coin.png",0)
print(temp.shape)
temp1 = temp
#temp1 = cv2.resize(temp,(200,200))
cv2.imshow('idk',temp1)
cv2.waitKey()




while same ==  False:
    src = cv2.imread(coins[i],0)
    template = cv2.imread(src)
    result = cv2.matchTemplate(src, temp1, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)
    temp2 = temp1[min_loc[0]:max_loc[0],min_loc[1]:max_loc[1]]
    src1 = cv2.resize(src,(130,189))
    cv2.imshow('ok',src1)
    cv2.waitKey()
    print(src1.shape)
    print(temp2.shape)
    same = True
    '''s = ssim(temp2, src, multichannel=True)
    print(s)
    if s > 0.9:
        print(coins[i])
        same = True
    i += 1
'''
