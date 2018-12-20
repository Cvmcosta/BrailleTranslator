import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
from tqdm import tqdm



IMG_SIZE_X = 60
IMG_SIZE_Y = 80
THRESH = 10


d={'numbers': '001111' ,'capital': '000001' , 'decimal': '000101' }
alpha={'a': '100000', 'c': '100100', 'b': '110000', 'e': '100010', 'd': '100110', 'g': '110110', 'f': '110100', 'i': '010100', 'h': '110010', 'k': '101000', 'j': '010110', 'm': '101100', 'l': '111000', 'o': '101010', 'n': '101110', 'q': '111110', 'p': '111100', 's': '011100', 'r': '111010', 'u': '101001', 't': '011110', 'w': '010111', 'v': '111001', 'y': '101111', 'x': '101101', 'z': '101011', '+':'000101', 'ó':'001101', 'ã':'001110', 'é':'111111'}
n={'0':'010110', '1':'100000', '2':'110000', '3':'100100' ,'4':'100110'  ,'5':'100010' ,'6':'110100' ,'7':'110110'   ,'8':'110010' ,'9': '010100'}
c={',':'010000', '\'':'000010','.':'001000','!':'011010','?':'011001',';':'011000',' ':'000000', '-':'001001'}




#print(len(categories))



def create_training_data():
    i = 0
    translate = ""
    caps = False
    for img in range(len(os.listdir("train"))):  #Get images from test folder
            
            exists = os.path.isfile(os.path.join("train","char"+str(i)+".jpg"))
            
            while(not exists):
                i+=1
                exists = os.path.isfile(os.path.join("train","char"+str(i)+".jpg"))
           
            

            img_array = cv2.imread(os.path.join("train","char"+str(i)+".jpg") ,cv2.IMREAD_GRAYSCALE)  # convert to array
            new_array = cv2.resize(img_array, (IMG_SIZE_X, IMG_SIZE_Y))
           

            mat = ""
            
            
            value = 0
            for j in range(0, 29):
                for k in range(0, 26):
                    value = value + new_array[k, j]
            if (value/(j*k) > THRESH):
                mat += "1"
            else:
                mat += "0"


            value = 0
            for j in range(0, 29):
                for k in range(28, 53):
                    value = value + new_array[k, j]
            if (value/(j*k) >THRESH):
                mat += "1"
            else:
                mat += "0"


            value = 0
            for j in range(0, 29):
                for k in range(55, 79):
                    value = value + new_array[k, j]
            if (value/(j*k) >THRESH):
                mat += "1"
            else:
                mat += "0"


            
            value = 0
            for j in range(31, 59):
                for k in range(0, 26):
                    value = value + new_array[k, j]
            if (value/(j*k) >THRESH):
                mat += "1"
            else:
                mat += "0"

            


            value = 0
            for j in range(31, 59):
                for k in range(28, 53):
                    value = value + new_array[k, j]
            if (value/(j*k) >THRESH):
                mat += "1"
            else:
                mat += "0"



            

            value = 0
            for j in range(31, 59):
                for k in range(55, 79):
                    value = value + new_array[k, j]
            if (value/(j*k) >THRESH):
                mat += "1"
            else:
                mat += "0"
            


            

            flag  = False
            for ch,value in alpha.items():
                if (mat == value):
                    flag = True
                    if(ch == '+'):
                            caps = True
                    else:
                        if(caps):
                            translate += ch.upper()
                            caps = False
                        else:
                            translate += ch
            
            if(not flag):
                for ch,value in c.items():
                    if (mat == value):
                        flag = True
                        if(ch == '+'):
                                caps = True
                        else:
                            if(caps):
                                translate += ch.upper()
                                caps = False
                            else:
                                translate += ch
            if(not flag):
                for ch,value in n.items():
                    if (mat == value):
                        flag = True
                        if(ch == '+'):
                                caps = True
                        else:
                            if(caps):
                                translate += ch.upper()
                                caps = False
                            else:
                                translate += ch

            #print(mat)
            i = i+1
            """ plt.imshow(new_array, cmap='gray')
            plt.show() """
           
    print("-"+translate+"-") 
      




create_training_data()
