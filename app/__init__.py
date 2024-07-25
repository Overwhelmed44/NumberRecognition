from keras.api.models import load_model
from app.train import train
from os.path import exists

if exists('app/example/model.keras'):
    network = load_model('app/example/model.keras')
else:
    from app.network import network

    network = train(network)

from app.server import app
