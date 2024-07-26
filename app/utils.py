from math import ceil
import numpy as np
import cv2


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


def pad_zeros(image, to=(28, 28)):
    y, x = image.shape
    dy, dx = to[0] - y, to[1] - x
    return np.lib.pad(image, ((dy // 2, ceil(dy / 2)), (dx // 2, ceil(dx / 2))))


def center(image):
    # replaced by find_box_contours

    shape = image.shape
    image = crop_zero_edges(image)
    return pad_zeros(image, shape)


def find_box_contours(image):
    contours, h = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    boxes = []
    for n, contour in enumerate(contours):
        if h[0][n][3] == -1:
            boxes.append(cv2.boundingRect(contour))
    
    return boxes
    