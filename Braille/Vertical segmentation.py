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

    rows,cols = img.shape

   
    #Tamanho da celula
    mask = 72

    #Taxa de correcao de tamanho de celula
    correction_rate = 4
    correction = 0
  

    i=0
    while(i < cols):
                aux  = np.zeros([rows, mask], dtype=np.uint8)
                
                for k in range(mask):
                         if(i+k >= cols): 
                                 break
                         for j in range(rows):
                                 aux[j,k] = img[j,i+k]

                if(correction == correction_rate):
                        correction = 0
                        i = i - 3
                else:
                        correction = correction + 1  
                cv2.imwrite("chars/char"+str(char)+".jpg", aux)
                char = char + 1
                i = i+mask
                
             
    part = part+1                    



#Retira alfabeto         

""" while(True):
    
    exists = os.path.isfile('part'+str(part)+'.jpg')
    if not exists:
            break
    
    img=cv2.imread('part'+str(part)+'.jpg', 0)

    rows,cols = img.shape

    #gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret, threshold = cv2.threshold(gray_image,200,255,cv2.THRESH_BINARY)

    mask = 72
    cur = 0
    count  = 0
    i=0
    while(i < cols):
                aux  = np.zeros([rows, mask], dtype=np.uint8)
                
                for k in range(mask):
                         if(i+k >= cols): 
                                 break
                         for j in range(rows):
                                 aux[j,k] = img[j,i+k]
                                
                cv2.imwrite("alphabet/char"+str(char)+".jpg", aux)
                char = char + 1
                i = i+mask
                
             
    part = part+1                    
                         """
                        
 