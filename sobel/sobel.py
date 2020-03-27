import numpy as np
import cv2
from convolve_np import convolve_np

img = cv2.imread('../img/mano.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

Hx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

Hy = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]])

img_x = convolve_np(img, Hx) / 8.0
img_y = convolve_np(img, Hy) / 8.0

img_out = np.sqrt(np.power(img_x, 2) + np.power(img_y, 2))

img_out = (img_out / np.max(img_out)) * 255

cv2.imshow('sobel',img_out)
cv2.waitKey(0)