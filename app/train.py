from keras.api.utils import to_categorical
from keras.api.datasets import mnist
from numpy import where


def train(network, save=True):
    (itr, ltr), (ite, lte) = mnist.load_data()

    itr = where(itr > 127, 1, 0)
    ite = where(ite > 127, 1, 0)

    ltr = to_categorical(ltr, 10)
    lte = to_categorical(lte, 10)

    network.fit(
        itr, ltr, 32, 10, validation_split=0.2, validation_data=(ite, lte)
    )

    if save: network.save('app/example/model.keras')
