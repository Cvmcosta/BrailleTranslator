from __future__ import print_function
import cv2
import numpy as np
import math
import string
import sys
import os

part = 0
char = 0


while(True):
    
    exists = os.path.isfile('horizontal/part'+str(part)+'.jpg')
    if not exists:
            break
    
    img=cv2.imread('horizontal/part'+str(part)+'.jpg', 0)
    ret, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

    rows,cols = img.shape

   
    #Tamanho da celula
    mask = 72

    #Taxa de correcao de tamanho de celula
    correction_rate = 5
    correction = 0
    correction_num = 4
  

    i=0
    while(i < cols):
                aux  = np.zeros([rows, mask], dtype=np.uint8)
                
                for k in range(mask):
                         if(i+k >= cols): 
                                 break
                         for j in range(rows):
                                 if(img[j,i+k] == 255):
                                        aux[j,k] = img[j,i+k]

                if(correction == correction_rate):
                        correction = 0
                        i = i - correction_num
                else:
                        correction = correction + 1
                
                cv2.imwrite("chars/char"+str(char)+".jpg", aux)
                char = char + 1
                i = i+mask
                
             
    part = part+1                    



