from keras.api.utils import to_categorical
from keras.api.datasets import mnist
from app.utils import threshold


def train(network, save=True):
    (itr, ltr), (ite, lte) = mnist.load_data()

    itr = threshold(itr)
    ite = threshold(ite)

    ltr = to_categorical(ltr, 10)
    lte = to_categorical(lte, 10)

    network.fit(
        itr, ltr, 32, 10, validation_split=0.2, validation_data=(ite, lte)
    )

    if save: network.save('app/example/model.keras')
