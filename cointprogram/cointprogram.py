from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
same = False
i = 0

coins = ["fifty_cent_old.png","five_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]

while same == False:
    img_org = cv2.imread("trial_coin.png",1)
    img_org_1 = cv2.resize(img_org,(433,577))
    img_changed_2 = cv2.imread(coins[i],1)
    s = ssim(img_org_1, img_changed_2,  multichannel=True)
    print(s)
    if s > 0.9:
        print(coins[i])
        same == True
    i += 1
