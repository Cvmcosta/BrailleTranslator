import numpy as np
import cv2
import os
import copy

def retiraPontosReversos(img):
        #contraste(img, 1, 3)
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        
        #show_img(img, "initial")
        
        rows, cols = img.shape
        aux  = np.zeros([rows,cols], dtype=np.uint8)
        for i in range(rows):
                for j in range(cols):                 
                        aux[i,j] = img[i,j]
        #Pega imagem original
    
        
        img = cv2.medianBlur(img, 5)
        
       

        #img2 = negacao(img2)
        img = gama(img, 1, 2, 1)
        
        #img2 = gama(img2, 1, 1.5, 2)

        ret, thresh = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
        kernel = np.ones((3,3),np.uint8)
        thresh = cv2.erode(thresh,kernel,iterations = 4)


        #show_img(img3, "final")
        thresh = negacao(thresh)
        cv2.imwrite("preprocessing/ready.jpg", thresh)
        return img




def gama(img, c, gama, n):
        rows, cols = img.shape
        
        for i in range(rows):
                for j in range(cols):
                        aux = (img[i,j]*1.0)/255
                        value = c * (aux)**gama
                        value = value*255
                        if(value > 255):
                                img[i,j] = 255
                        else:
                                img[i,j] = value
        #show_img(img, "Gama "+str(n))              
        return img





def negacao(img):
    
        rows, cols = img.shape
        
        for i in range(rows):
                for j in range(cols):
                        img[i,j] = 255 - img[i,j]
        
        #show_img(img, "negativa")
        return img


def show_img(img, name):
        cv2.imshow(name, img)
        cv2.waitKey(0)



        


filename = "../newDS/3.jpg"
roi = cv2.imread(filename) 


#HoughCirc(roi)
retiraPontosReversos(roi)



