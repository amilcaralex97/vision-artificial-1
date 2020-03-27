import numpy as np
import cv2

PATH='../img/mano.jpg'

img = cv2.imread(PATH,cv2.IMREAD_GRAYSCALE)
gaussian= cv2.GaussianBlur(img,(5,5),0)
#average
image=cv2.resize(img,(500,500))

average= np.zeros_like(image)
E=np.zeros((3,3))

for j in range(len(image)-1):
        for k in range(len(image[j])-1):
                E[0][0]=image[j-1][k-1]
                E[0][1]=image[j-1][k-1]
                E[0][2]=image[j-1][k-1]
                E[1][0]=image[j-1][k-1]
                E[1][1]=image[j-1][k-1]
                E[1][2]=image[j-1][k-1]
                E[2][0]=image[j-1][k-1]
                E[2][1]=image[j-1][k-1]
                E[2][2]=image[j-1][k-1]

                average[j][k]=np.mean(E)



#Guassian code
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

gauss = (1.0/57) * np.array(
        [[0, 1, 2, 1, 0],
        [1, 3, 5, 3, 1],
        [2, 5, 9, 5, 2],
        [1, 3, 5, 3, 1],
        [0, 1, 2, 1, 0]])
sum(sum(gauss))

for i in np.arange(2, height-2):
    for j in np.arange(2, width-2):        
        sum = 0
        for k in np.arange(-2, 3):
            for l in np.arange(-2, 3):
                a = img.item(i+k, j+l)
                p = gauss[2+k, 2+l]
                sum = sum + (p * a)
        b = sum
        img_out.itemset((i,j), b)

cv2.imshow('gaussian a pata',img_out)
cv2.imshow("normalona",img)
cv2.imshow("Gaussian",gaussian)
cv2.imshow('promedio',average)
cv2.waitKey(0)
cv2.destroyAllWindows()