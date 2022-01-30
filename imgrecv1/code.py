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
import time
def nothing():
        print("No coins found, please try again")
imginput="cointest3.png"
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
        #orgimg = cv2.imread('cointest.png')
        cropped_image = image[min(y_coord)-50:max(y_coord)+50, min(x_coord)-50:max(x_coord)+50]
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
                print("coin found")
                # === COMPARE IMAGE WITH DATA BASE ===
                x=[]
                coinsrank=[]
                coins = ["five_cent_old.png","fifty_cent_old.png","one_dollar_old.png","ten_cent_old.png","twenty_cent_old.png","fifty_cent.png","five_cent.png","one_dollar.png","ten_cent.png","twenty_cent.png"]
                process= ["Processing...","Reading image...","Comparing image..."]
                for i in range (3):
                    print(process[i])
                    time.sleep(1)
                for i in range (10):
                    img_org=cv2.imread("cropimg.png")
                    img_org_1=cv2.resize(img_org, (500, 500)) #resize the dimenssions
                    img_test=cv2.imread(coins[i])
                    img_test_1=cv2.resize(img_test, (500, 500)) #resize the dimenssions
                    s = ssim(img_org_1, img_test_1,  multichannel=True)
                    x.append(s)
                print("=== Results ===")
                y=x.copy()
                y.sort()
                for i in y:
                    coinsrank.append(coins[x.index(i)])
                for i in range (10):
                    print("{}. {}: {} %".format(i+1, coinsrank[9-i], format(float(y[9-i]*100),".2f")))


        else:
                nothing()
                break
        break



