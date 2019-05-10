import cv2
import numpy as np

im = cv2.imread("Lego.jpg",0)
im2 = cv2.imread("kirby.jpg",0)
img = cv2.resize(im, (500, 500))
img2 = cv2.resize(im2, (500, 500))
rows,cols = img.shape
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(500,500))
cv2.imshow('img',dst)
cv2.waitKey(0)

M = np.float32([[1,0,200],[0,1,80]])
dst = cv2.warpAffine(img,M,(500,500))
cv2.imshow('img',dst)
cv2.waitKey(0)

res = cv2.resize(img,None,fx=.5, fy=.5, interpolation = cv2.INTER_CUBIC)
cv2.imshow('img',res)
cv2.waitKey(0)

cv2.bitwise_not(img, dst)
cv2.imshow('img',dst)
cv2.waitKey(0)

cv2.bitwise_and(img, img2, dst)
cv2.imshow('img',dst)
cv2.waitKey(0)

cv2.bitwise_or(img, img2, dst)
cv2.imshow('img',dst)
cv2.waitKey(0)