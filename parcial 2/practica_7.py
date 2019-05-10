import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from convolve_np import convolve_np

img = cv2.imread('../img/mano.jpg',cv2.IMREAD_GRAYSCALE)
#Sovel

height = img.shape[0]
width = img.shape[1]

Hx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

Hy = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 2, 1]])

sobel_x = convolve_np(img, Hx) / 8.0
sobel_y = convolve_np(img, Hy) / 8.0


#prewitt

Px = np.array([[-1, 0, 1],
               [-1, 0, 1],
               [-1, 0, 1]])

Py = np.array([[-1, -1, -1],
               [0, 0, 0],
               [1, 1, 1]])

prewitt_x = convolve_np(img, Px) / 6.0
prewitt_y = convolve_np(img, Py) / 6.0

#robert cross

roberts_cross_v = np.array( [[ 0, 0, 0 ],
                             [ 0, 1, 0 ],
                             [ 0, 0,-1 ]] )

roberts_cross_h = np.array( [[ 0, 0, 0 ],
                             [ 0, 0, 1 ],
                             [ 0,-1, 0 ]] )

robert_x = convolve_np(img, roberts_cross_h) / 2.0
robert_y = convolve_np(img, roberts_cross_v) / 2.0

#-----------------------------------------------------------------------

cv2.imshow('robert_cross',robert_x+robert_y)
cv2.imshow('original',img)
cv2.imshow('chidosobel',sobel_x+sobel_y)
cv2.imshow('prewitt',prewitt_x+prewitt_y)
cv2.waitKey(0)
cv2.destroyAllWindows()