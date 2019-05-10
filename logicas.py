import cv2
import numpy as np

im = cv2.imread("./img/calamardo.JPG",0)
im2 = cv2.imread("./img/patricio.JPG",0)
img = cv2.resize(im, (500, 500))
img2 = cv2.resize(im2, (500, 500))
rows,cols = img.shape

I = cv2.getRotationMatrix2D((cols/2,rows/2),60,1)
dst = cv2.warpAffine(img,I,(500,500))
cv2.imshow('Rotacion',dst)


I = np.float32([[1,0,100],[0,1,90]])
dst = cv2.warpAffine(img,I,(500,500))
cv2.imshow('Traslacion',dst)
cv2.waitKey(0)

resize = cv2.resize(img,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_CUBIC)
cv2.imshow('Tamaño',resize)
cv2.waitKey(0)

cv2.bitwise_and(img, img2, dst)
cv2.imshow('and',dst)
cv2.waitKey(0)

cv2.bitwise_or(img, img2, dst)
cv2.imshow('or',dst)
cv2.waitKey(0)

cv2.bitwise_not(img, dst)
cv2.imshow('not',dst)
cv2.waitKey(0)