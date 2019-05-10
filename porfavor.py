import cv2
import numpy as np
import imutils

mano="../img/mano.jpg"

img = cv2.imread(mano)
et = 1

b = img[:, :, 2]
g = img[:, :, 1]
r = img[:, :, 0]

E = np.zeros_like(b)

for j in range(len(b)):
	for k in range(len(b[j])):
		if b[j][k] < 180 or g[j][k] < 180 or r[j][k] < 230:
			b[j][k] = 255
			g[j][k] = 255
			r[j][k] = 255
		else:
			b[j][k] = 0
			g[j][k] = 0
			r[j][k] = 0

for j in range(len(r)):
	for k in range(len(r[j])):
		if r[j][k] == 255:
			A = np.array([50,50,50,50])

			if r[j-1][k-1] != 0: A[0] = E[j-1][k-1] 
			if r[j-1][k] != 0: A[1] = E[j-1][k]	
			if r[j-1][k+1] != 0: A[2] = E[j-1][k+1]
			if r[j][k-1] != 0: A[3] = E[j][k-1]

			if r[j-1][k-1] == 255 or r[j-1][k] == 255 or r[j-1][k+1] == 255 or r[j][k-1] == 255:
				E[j][k] = A.min()
				if E[j-1][k-1] 	> E[j][k]: E[j-1][k-1]	= E[j][k]
				if E[j-1][k]	> E[j][k]: E[j-1][k]	= E[j][k]
				if E[j-1][k+1]	> E[j][k]: E[j-1][k+1]	= E[j][k]
				if E[j][k-1] 	> E[j][k]: E[j][k-1]	= E[j][k]
			else:
				E[j][k] = et
				et += 1

for j in range(len(E)):
	for k in range(len(E[j])):
		if E[j][k] == 1:
			b[j][k] = 0
			g[j][k] = 255
			r[j][k] = 0
		elif E[j][k] == 2:
			b[j][k] = 0
			g[j][k] = 255
			r[j][k] = 255
		elif E[j][k] == 3:
			b[j][k] = 25
			g[j][k] = 100
			r[j][k] = 25
		elif E[j][k] == 4:
			b[j][k] = 205
			g[j][k] = 5
			r[j][k] = 5
		elif E[j][k] == 5:
			b[j][k] = 11
			g[j][k] = 13
			r[j][k] = 56
		elif E[j][k] == 6:
			b[j][k] = 123
			g[j][k] = 45
			r[j][k] = 12
		elif E[j][k] == 7:
			b[j][k] = 12
			g[j][k] = 54
			r[j][k] = 15
		elif E[j][k] == 8:
			b[j][k] = 5
			g[j][k] = 0
			r[j][k] = 55
		elif E[j][k] == 9:
			b[j][k] = 55
			g[j][k] = 2
			r[j][k] = 255
		elif E[j][k] == 10:
			b[j][k] = 123
			g[j][k] = 93
			r[j][k] = 3
		elif E[j][k] == 11:
			b[j][k] = 123
			g[j][k] = 12
			r[j][k] = 76

print (et)



lefalta=cv2.merge((b,g,r))

cv2.imwrite("hola.jpeg",lefalta)

chido=cv2.imread("./hola.jpeg")

gray = cv2.cvtColor(chido, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)
cv2.bitwise_not(thresh, thresh)

cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
c = max(cnts, key=cv2.contourArea)

left = tuple(c[c[:, :, 0].argmin()][0])
right = tuple(c[c[:, :, 0].argmax()][0])

distance = np.sqrt( (right[0] - left[0])**2 + (right[1] - left[1])**2 )

x,y,w,h = cv2.boundingRect(c)

centx = np.sqrt( ((right[0] + left[0])**2)/4)
centy = np.sqrt( ((right[1] + left[1])**2)/4 )
print(centx, centy)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.circle(chido, left, 5, (0, 0, 255), -1)
cv2.circle(chido, right, 5, (0, 0, 255), -1)
cv2.circle(chido, (int(centx), int(centy)), 5, (0, 0, 255), -1)
cv2.line(chido, left, right, (255,0,0), 2)
cv2.drawContours(chido, [c], -1, (0,255,0), 2)
cv2.rectangle(chido,(x,y),(x+w,y+h),(0,255,0),2)
cv2.putText(chido,'Distance: '+str(distance),(10,30), font, 1, (0,0,0),2, cv2.LINE_AA)
cv2.imshow('img', chido)

cv2.waitKey(0)
cv2.destroyAllWindows()
