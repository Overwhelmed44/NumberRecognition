from math import ceil
import numpy as np
import cv2


def threshold(image, th=127):
    return np.where(image > th, 1, 0)


def pad_zeros(image, to):
    y, x = image.shape
    dy, dx = to[0] - y, to[1] - x
    return np.lib.pad(image, ((dy // 2, ceil(dy / 2)), (dx // 2, ceil(dx / 2))))


def center(image, obj_shape=(25, 25), output_shape=(28, 28)):
    y, x = image.shape

    if y > obj_shape[0] or x > obj_shape[1]:
        image = threshold(cv2.resize(image, obj_shape, interpolation=cv2.INTER_CUBIC), 0.5)
    
    return pad_zeros(image, output_shape)


def find_box_contours(image):
    contours, h = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for n, contour in enumerate(contours):
        if h[0][n][3] == -1:
            yield cv2.boundingRect(contour)
    