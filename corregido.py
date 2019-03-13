import numpy as np
import cv2 


mano='./img/mano.jpg'
manos='./img/manos.jpeg'
ok='./img/ok.jpeg'

img = cv2.imread(mano)#r+g+b/3
gaussiana = cv2.GaussianBlur(img, (5,5), 0)
b,g,r=cv2.split(gaussiana)

b=np.array(b)
g=np.array(g)
r=np.array(r)


for j in range(len(b)):
	for k in range(len(b[j])):
		b[j][k] *= 0.5
		g[j][k] *= 0.5
		r[j][k] *= 0.5

for j in range(len(b)):
	for k in range(len(b[j])):
		b[j][k] = int((b[j][k] + 1) / (b[j][k] + g[j][k] + r[j][k] + 1) * 255)
		g[j][k] = int((g[j][k] + 1) / (b[j][k] + g[j][k] + r[j][k] + 1) * 255)
		r[j][k] = int((r[j][k] + 1) / (b[j][k] + g[j][k] + r[j][k] + 1) * 255)

b=np.where(b>200,1*256,255*256)
g=np.where(g>200,1*256,255*256)
r=np.where(r>150,1*256,255*256)

nueva= cv2.merge((b,g,r))



cv2.imshow("imgsinbrillo",nueva)
#cv2.imshow("original",gaussiana)

cv2.waitKey(0)
cv2.destroyAllWindows()