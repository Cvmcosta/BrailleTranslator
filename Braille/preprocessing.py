import cv2
import argparse
import numpy as np

mask= cv2.imread('preprocessing/ready.jpg',0)



rows,cols=mask.shape
cv2.imwrite('preprocessing/mask.jpg',mask)


refPt = []
cropping = False
 
def click_and_crop(event, x, y, flags, param):
        global refPt, cropping
 
        if event == cv2.EVENT_LBUTTONDOWN:
                refPt = [(x, y)]
                cropping = True
 

        elif event == cv2.EVENT_LBUTTONUP:


                refPt.append((x, y))
                cropping = False
 

                cv2.rectangle(mask, refPt[0], refPt[1], (255, 255, 255), 2)
                cv2.namedWindow('image',cv2.WINDOW_NORMAL)
                cv2.resizeWindow('image',  rows,cols)
                cv2.imshow("image", mask)

 

clone = mask.copy()
cv2.namedWindow("image" ,cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',  rows,cols)
cv2.setMouseCallback("image", click_and_crop)
 

while True:
        
        cv2.namedWindow("image" ,cv2.WINDOW_NORMAL) 
        cv2.resizeWindow('image',  rows,cols)
        cv2.imshow("image", mask)
        key = cv2.waitKey(1) & 0xFF
 

        if key == ord("r"):
                image = clone.copy()
 

        elif key == ord("c"):
                break
 

if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        cv2.imwrite('preprocessing/roi.jpg',roi)

        cv2.namedWindow("ROI" ,cv2.WINDOW_NORMAL)
        cv2.resizeWindow('ROI',refPt[0][1]-refPt[1][1], refPt[0][0]-refPt[1][0] )
        cv2.imshow("ROI", roi)
       
cv2.waitKey(0)
cv2.destroyAllWindows()




