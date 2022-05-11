import cv2
from skimage.transform import resize
from os import listdir, walk
from os.path import isfile, join
import matplotlib as plt
import numpy as np
import random
from sklearn.model_selection import train_test_split
from tensorflow import kerasfrom 

def gray_reshape(directory, new_size = (28,28), gray =True):
    """
    give the list of photos with the correct pixel size you want to 
    downsize. If you want Gray then write True.
    """
    items_resized  =[]
    pictures = []
    labels = []
    mapping = {'books' : 1,'coins' : 2,'cups' : 3,'cutlery' : 4,'faces' : 5,'gestures' : 6,'glasses' : 7,'nail_polishes' : 8,'plants' : 9 }
    onlyfolders = [f for f in listdir(directory)]
    for idx, folder in enumerate(onlyfolders[1:]):
        pictures = [f for f in listdir(directory + folder) if isfile(join(directory + folder , f))]
        for idx, picture in enumerate(pictures):
            item = cv2.imread(directory + folder +'/'+ picture )
            labels.append(mapping[folder])
            if gray == True:
                item_gray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
                item_resized_gray = resize(item_gray, new_size)
                items_resized.append(item_resized_gray)
            else:
                item_resized_colored = resize(item, new_size)
                items_resized.append(item_resized_colored)
    return items_resized, labels


X,y = gray_reshape('../output/', new_size = (28,28), gray =True);

#plt.imshow(X[8],cmap='Greys')
# Model / data parameters
num_classes = len(np.unique(y))
input_shape = (28, 28, 1)
# shuffle the data

shuffler = np.random.permutation(len(X))
X = np.array(X)
y = np.array(y)
X = X[shuffler]
y = y[shuffler]

# the data, split between train and test sets

X_train, X_test, y_train, y_test = train_test_split(X, y)
# Scale images to the [0, 1] range
#### Normalise
x_train = X_train.astype("float32") / 255
x_test = X_test.astype("float32") / 255
# Always always check shapes! 
x_train.shape, x_test.shape
# one hot encoder

y_train = keras.utils.to_categorical(y_train, num_classes+1)

y_test = keras.utils.to_categorical(y_test, num_classes+1)

# define the keras model.    the kernel size is the window that checks geometries: can be (3,3), (5,5), (7,7)
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(8, kernel_size=(3, 3), activation="relu"),   # number of neurons:  must be multiples of 2. good technique to start eith 8 and then we increase in the insede layers.
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(16, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.15),
        layers.Dense(num_classes, activation="softmax"),
    ]
)
# model summary table
model.summary()

# define the batch size and number of epochs
batch_size = 5
epochs = 50


# complile and define eval metric
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# fit the model
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)