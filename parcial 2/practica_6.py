import cv2
import numpy as np

PATH='../img/mano.jpg'

#median filter
img = cv2.imread(PATH,cv2.IMREAD_GRAYSCALE)
img1=cv2.imread(PATH)

img_outmedian = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):
        neighbors = []
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                neighbors.append(a)
        neighbors.sort()
        median = neighbors[24]
        b = median
        img_outmedian.itemset((i,j), b)


#max filter
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):      
        max = 0
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                if a > max:
                    max = a
        b = max
        img_out.itemset((i,j), b)
#minfilter
img_outmin = img.copy()

height = img.shape[0]
width = img.shape[1]

for i in np.arange(3, height-3):
    for j in np.arange(3, width-3):
        min = 255
        for k in np.arange(-3, 4):
            for l in np.arange(-3, 4):
                a = img.item(i+k, j+l)
                if a < min:
                    min = a
        b = min
        img_outmin.itemset((i,j), b)

cv2.imshow("Mediana",img_outmedian)
cv2.imshow("Max",img_out)
cv2.imshow("min",img_outmin)
cv2.waitKey(0)
cv2.destroyAllWindows()
