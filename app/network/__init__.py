from keras.api.models import load_model
from os.path import exists

PATH = 'app/network/example/model.keras'

if exists(PATH):
    model = load_model(PATH)
else:
    from app.network.model import model
    from app.network.train import train

    train()