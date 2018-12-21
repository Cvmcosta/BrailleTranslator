import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
from tqdm import tqdm



IMG_SIZE_X = 60
IMG_SIZE_Y = 60

training_data = []
test_data = []




text = "+estados +unidos, +teresa para o convento, +raimundo morreu de desastre, +maria ficoupara tia, +joaquim suicidou-se e +lili casou com +j. +pinto +fernandes que não tinha entrado na história.     "

categories = "abcdefghijklmnopqrstuvwxyz,- ãáéó.+"
categories = list(categories)

text = text.lower()

chars = list(text)



def create_training_data():
    i = 0
    j = 0

    for img in range(len(os.listdir("train"))):  
            
            exists = os.path.isfile(os.path.join("train","char"+str(j)+".jpg"))
            
            while(not exists):
                j+=1
                exists = os.path.isfile(os.path.join("train","char"+str(j)+".jpg"))

            img_array = cv2.imread(os.path.join("train","char"+str(j)+".jpg") ,cv2.IMREAD_GRAYSCALE)  
            new_array = cv2.resize(img_array, (IMG_SIZE_X, IMG_SIZE_Y))
           
            

            training_data.append([new_array, categories.index(chars[i])])

            #Mostra a imagem
            """ plt.imshow(new_array, cmap='gray')
            plt.show() """
            
            i = i+1
            j = j+1

def create_test_data():
    i = 0
    j = 0

    for img in range(len(os.listdir("test"))):  
            
            exists = os.path.isfile(os.path.join("test","char"+str(j)+".jpg"))
            
            while(not exists):
                j+=1
                exists = os.path.isfile(os.path.join("test","char"+str(j)+".jpg"))

            img_array = cv2.imread(os.path.join("test","char"+str(j)+".jpg") ,cv2.IMREAD_GRAYSCALE)  
            new_array = cv2.resize(img_array, (IMG_SIZE_X, IMG_SIZE_Y))
           
            

            test_data.append(new_array)

            #Mostra a imagem
            """ plt.imshow(new_array, cmap='gray')
            plt.show() """
            
            i = i+1
            j = j+1




create_training_data()
create_test_data()


x = []
y = []

for features,label in training_data:
    x.append(features)
    y.append(label)


x = np.array(x).reshape(-1, IMG_SIZE_X, IMG_SIZE_Y, 1)

pickle_out = open("X.pickle","wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()



x_test = []

for features in test_data:
    x_test.append(features)



x_test = np.array(x_test).reshape(-1, IMG_SIZE_X, IMG_SIZE_Y, 1)

pickle_out_test = open("X_test.pickle","wb")
pickle.dump(x_test, pickle_out_test)
pickle_out_test.close()

