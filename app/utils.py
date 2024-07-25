from math import ceil
import numpy as np


def crop_zero_edges(image):
    while not np.sum(image[0]):
        image = image[1:]
    while not np.sum(image[-1]):
        image = image[:-1]
    while not np.sum(image[:,0]):
        image = np.delete(image, 0, 1)
    while not np.sum(image[:,-1]):
        image = np.delete(image, -1, 1)
    return image


def pad_zeros(image, to):
    y, x = image.shape
    dy, dx = to[0] - y, to[1] - x
    return np.lib.pad(image, ((dy // 2, ceil(dy / 2)), (dx // 2, ceil(dx / 2))))


def center(image):
    shape = image.shape
    image = crop_zero_edges(image)
    return pad_zeros(image, shape)
    