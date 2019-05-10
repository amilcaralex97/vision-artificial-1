import numpy as np
import cv2
import random

mano='../img/mano.jpg'

img = cv2.imread(mano)

#img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

rows,columns, channels =img.shape
p=0.05
#salt pepper noise
output=np.zeros(img.shape,np.uint8)


for i in range(rows):
    for j in range(columns):
        r=random.random()
        if r<p/2:
            #pepper
            output[i][j]=[0,0,0]
        elif r<p:
            #salt
            output[i][j]=[255,255,255]
        else:
            output[i][j]=img[i][j]


#gaussian noise

gaussian=np.copy(img)
rowsg, columnsg, channelsg= gaussian.shape
mean=0
var=0.1
sigma=var**0.5
gauss=np.random.normal(mean,sigma,(rowsg,columnsg,channelsg))

gauss=gauss.reshape(rowsg,columnsg,channelsg)
noisy=gaussian+gauss

cv2.imwrite('noisesp.jpg',output)
cv2.imshow('Gaussian noise',noisy)
cv2.imshow('salt pepper noise',output)
cv2.waitKey(0)
cv2.destroyAllWindows()