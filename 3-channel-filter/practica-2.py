""" Práctica 2 configurar canales y utilizar algoritmo white patch """
import numpy as np
import cv2 

mano='./img/mano.jpg'
manos='./img/manos.jpeg'
ok='./img/ok.jpeg'

img = cv2.imread(mano)#r+g+b/3
(b, g, r) = (img[:,:,0], img[:,:,1], img[:,:,2])


""" Binarizacion de la original """
b=np.where(b>240,0,255*256)
g=np.where(g>230,0,255*256)
r=np.where(r>250,0,255*256)

normal= cv2.merge((b,g,r))

""" Imagen canal azul intenso """
azulintenso=np.copy(img)
(bai, gai, rai) = (azulintenso[:,:,0], azulintenso[:,:,1], azulintenso[:,:,2])

for j in range(len(bai)):
	for k in range(len(bai[j])):
		bai[j][k] *= 1
		gai[j][k] *= .5
		rai[j][k] *= .5

azulintenso=cv2.merge((bai,gai,rai))


""" White patch para con azul """
azulConAlgoritmo=np.copy(img)
(bca, gca, rca) = (azulConAlgoritmo[:,:,0], azulConAlgoritmo[:,:,1], azulConAlgoritmo[:,:,2])

for j in range(len(bca)):
	for k in range(len(bca[j])):
		bca[j][k] *= 1
		gca[j][k] *= .5
		rca[j][k] *= .5

max_b = np.amax(np.amax(azulConAlgoritmo[:,:,0]))
print(max_b)
max_g = np.amax(np.amax(azulConAlgoritmo[:,:,1]))
print(max_g)
max_r = np.amax(np.amax(azulConAlgoritmo[:,:,2]))
print(max_r)

for j in range(len(bca)):
	for k in range(len(bca[j])):
		bca[j][k] = int( (255) * (bca[j][k]) / (max_b))
		gca[j][k] = int( (255) * (gca[j][k]) / (max_g))
		rca[j][k] = int( (255) * (rca[j][k])/ (max_r))

nueva=cv2.merge((bca,gca,rca))

""" Evaluacion sin algoritmo """

""" azulSinAlgoritmo=np.copy(img)
(ba, ga, ra) = (azulSinAlgoritmo[:,:,0], azulSinAlgoritmo[:,:,1], azulSinAlgoritmo[:,:,2])

#ba=ba*1.5
for j in range(len(ba)):
	for k in range(len(ba[j])):
		bca[j][k] *= 1
		gca[j][k] *= .5
		rca[j][k] *= .5

for j in range(len(ba)):
	for k in range(len(ba[j])):
		if ba[j][k] < 240 & ga[j][k] < 230 & ra[j][k] < 250:
			ba[j][k] = 255
			ga[j][k] = 255
			ra[j][k] = 255
		else:
			ba[j][k] = 0
			ga[j][k] = 0
			ra[j][k] = 0

azul=cv2.merge((ba,ga,ra)) """
#ba=np.where(ba>240,0,255*256)
#ga=np.where(ga>230,0,255*256)
#ra=np.where(ra>250,0,255*256)
""" white patch binarizada """

azulwp=np.copy(img)
bwp,gwp,rwp=cv2.split(azulwp)

for j in range(len(bwp)):
	for k in range(len(bwp[j])):
		bwp[j][k] *= 1
		gwp[j][k] *= 1
		rwp[j][k] *= 1

max_bwp = np.amax(np.amax(azulwp[:,:,0]))
print(max_bwp)
max_gwp = np.amax(np.amax(azulwp[:,:,1]))
print(max_gwp)
max_rwp = np.amax(np.amax(azulwp[:,:,2]))
print(max_rwp)

for j in range(len(bwp)):
	for k in range(len(bwp[j])):
		bwp[j][k] = int( (255) * (bwp[j][k]) / (max_bwp))
		gwp[j][k] = int( (255) * (gwp[j][k]) / (max_gwp))
		rwp[j][k] = int( (255) * (rwp[j][k])/ (max_rwp)) 

for j in range(len(bwp)):
	for k in range(len(bwp[j])):
		if bwp[j][k] < 240 & gwp[j][k] < 230 & rwp[j][k] < 250:
			bwp[j][k] = 255
			gwp[j][k] = 255
			rwp[j][k] = 255
		else:
			bwp[j][k] = 0
			gwp[j][k] = 0
			rwp[j][k] = 0

chidodido=cv2.merge((bwp,gwp,rwp))

""" --------------------------------------- """

#cv2.imshow("original",img)
#cv2.imshow("normal binarizada",normal)
#cv2.imshow("escalar azul",azul)
cv2.imshow("azul mas intenso",azulintenso)
cv2.imshow("escalar nueva",nueva)
cv2.imshow("chidodido",chidodido)
#cv2.imshow("sin verde",manosinverde)
#cv2.imshow("sin rojo",manosinrojo)
cv2.waitKey(0)
cv2.destroyAllWindows()