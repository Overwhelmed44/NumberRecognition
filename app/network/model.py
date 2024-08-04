from keras.api.layers import Dense, Flatten, Input, Conv2D, MaxPooling2D
from keras.api.losses import CategoricalCrossentropy
from keras.api.activations import relu, softmax
from keras.api.optimizers import Adam
from keras import Sequential

model = Sequential([
    Input((28, 28, 1)),

    Conv2D(32, (3, 3), padding='same', activation=relu),
    MaxPooling2D(),
    Conv2D(64, (3, 3), padding='same', activation=relu),
    MaxPooling2D(),

    Flatten(),
    Dense(128, relu),
    Dense(10, softmax)
])

model.compile(Adam(), CategoricalCrossentropy(), metrics=['accuracy'])
