import cv2
import numpy as np

img_rgb = cv2.imread('trial_coin.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('template',0)
coins = ["fifty_cent_old.png","five_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]


# Store width and height of template in w and h
#print(template.shape)
 
# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
 
# Specify a threshold
threshold = 0.8
 
# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold)
 
# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
 
# Show the final image with the matched area.
cv2.imshow('Detected',img_rgb)
cv2.waitKey()
