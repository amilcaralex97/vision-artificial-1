import numpy as np
import cv2 

mano='./img/mano.jpg'

img = cv2.imread(mano)#r+g+b/3
(bwp, gwp, rwp) = (img[:,:,0], img[:,:,1], img[:,:,2])

for j in range(len(bwp)):
	for k in range(len(bwp[j])):
		bwp[j][k] *= 1
		gwp[j][k] *= .5
		rwp[j][k] *= .5

max_bwp = np.amax(np.amax(img[:,:,0]))
print(max_bwp)
max_gwp = np.amax(np.amax(img[:,:,1]))
print(max_gwp)
max_rwp = np.amax(np.amax(img[:,:,2]))
print(max_rwp)

for j in range(len(bwp)):
	for k in range(len(bwp[j])):
		bwp[j][k] = int( (255) * (bwp[j][k]) / (max_bwp))
		gwp[j][k] = int( (255) * (gwp[j][k]) / (max_gwp))
		rwp[j][k] = int( (255) * (rwp[j][k])/ (max_rwp)) 

bwp=np.where(bwp>250,0,255*256)
gwp=np.where(gwp>250,0,255*256)
rwp=np.where(rwp>250,0,255*256)

chidodido=cv2.merge((bwp,gwp,rwp))

cv2.imshow("azul mas intenso",chidodido)
cv2.waitKey(0)
cv2.destroyAllWindows()