from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time
import numpy as np
import keras

batch_size = 30
num_classes = 35
epochs = 15

NAME = "Braille-CNN"

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)


pickle_in = open("X_test.pickle","rb")
X_test = pickle.load(pickle_in)


pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0
X_test = X_test/255.0


y = keras.utils.to_categorical(y, num_classes)


categories = "abcdefghijklmnopqrstuvwxyz,- ãáéó.+"
categories = list(categories)




model = Sequential()

model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())


model.add(Dense(64))
model.add(Activation('relu'))

model.add(Dense(num_classes, activation='softmax'))


tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

model.compile(loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'],
                )

model.fit(np.array(X), np.array(y),
            batch_size=batch_size,
            epochs=epochs,
            validation_split=0.3,
            callbacks=[tensorboard])



print("Predição em cima dos dados de treino:")
score = model.predict_classes(np.array(X))
print(score)

text = ""
caps = False
for i in range(len(score)):

    if(categories[score[i]]=='+'):
        caps = True
        continue

    if(caps):
        text = text + categories[score[i]].upper()
        caps = False
    else:
        text = text + categories[score[i]]
    
print(text)



print("Predição em cima dos dados de teste:")
score = model.predict_classes(np.array(X_test))
print(score)

text = ""
caps = False
for i in range(len(score)):

    if(categories[score[i]]=='+'):
        caps = True
        continue

    if(caps):
        text = text + categories[score[i]].upper()
        caps = False
    else:
        text = text + categories[score[i]]
    
print(text)
