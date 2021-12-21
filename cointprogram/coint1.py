'''
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np

coins = ["fifty_cent_old.png","five_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]

temp = cv2.imread("trial_coin.png")
tempgray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
print(tempgray.shape)
#cv2.imshow('ok',tempgray)
#cv2.waitKey()

test = ["fifty_cent_old.png", "coin.png"]

for i in range (1):
    coin = cv2.imread(test[i])
    #print(coin.shape)
    resized = cv2.resize(tempgray, newsize)
    result = cv2.matchTemplate(coin, temp, cv2.TM_CCOEFF_NORMED)
    print(result)
'''

import cv2
import numpy as np

#load image into variable
img_rgb = cv2.imread('trial_coin.png')

#load template
template = cv2.imread('coin.png')

List = []

#read height and width of template image
w, h = template.shape[0], template.shape[1]

res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.95
loc = np.where( res >= threshold)

for i in zip(*loc[::-1]):
    location = (i[0] + w, i[1] + h)
    List.append([i, location])

    cv2.rectangle(img_rgb, i, location, (0,255,0), 20)

img_rgb = cv2.resize(img_rgb,(433,577))
cv2.imshow("result",img_rgb)
cv2.waitKey(10000)