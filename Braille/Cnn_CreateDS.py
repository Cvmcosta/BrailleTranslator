import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
from tqdm import tqdm



IMG_SIZE_X = 60
IMG_SIZE_Y = 80

training_data = []



text = "+Estados +Unidos, +Teresa para o convento, +Raimundo morreu de desastre, +Maria ficoupara tia, +Joaquim suicidou-se e +Lili casou com +J. +Pinto +Fernandes que não tinha entrado na história."

categories = "abcdefghijklmnopqrstuvwxyz,- áàéèãóç.+"
categories = list(categories)

text = text.lower()

chars = list(text)
print(len(categories))


def create_training_data():
    i = 0
   
    for img in sorted(os.listdir("train")):  #Get images from test folder
            img_array = cv2.imread(os.path.join("test",img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
            new_array = cv2.resize(img_array, (IMG_SIZE_X, IMG_SIZE_Y))
           
            

            training_data.append([new_array, categories.index(chars[i])])

            #Mostra a imagem
            """ plt.imshow(new_array, cmap='gray')
            plt.show() """
            
            i = i+1
            




create_training_data()
#Embaralha os dados
random.shuffle(training_data)


x = []
y = []

for features,label in training_data:
    x.append(features)
    y.append(label)

print(x[0].reshape(-1, IMG_SIZE_X, IMG_SIZE_Y, 1))

x = np.array(x).reshape(-1, IMG_SIZE_X, IMG_SIZE_Y, 1)

pickle_out = open("X.pickle","wb")
pickle.dump(x, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()



   
""" model = Sequential()
model.add(Dense(10, input_shape=(nFeatures,)))
model.add(Activation('linear'))
model.compile(optimizer='rmsprop', loss='mse', metrics=['mse', 'mae'])

model.fit(trainFeatures, trainLabels, batch_size=4, epochs = 100) """