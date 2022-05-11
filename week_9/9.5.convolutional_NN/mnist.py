import numpy as np

# pip install tensorflow the first time 
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
with tf.device('/GPU')
# Model / data parameters
num_classes = 10
input_shape = (28, 28, 1)

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Scale images to the [0, 1] range
#### Normalise
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255


# one hot encode

y_train = keras.utils.to_categorical(y_train, num_classes)
print(y_train)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(y_test)
# define the keras model.    the kernel size is the window that checks geometries: can be (3,3), (5,5), (7,7)
model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),   # number of neurons:  must be multiples of 2. good technique to start eith 8 and then we increase in the insede layers.
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation="softmax"),
    ]
)

# model summary table
model.summary()

# define the batch size and number of epochs
batch_size = 128
epochs = 5

# complile and define eval metric
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# fit the model
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1)

# evaluate the model and print the results
score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])
