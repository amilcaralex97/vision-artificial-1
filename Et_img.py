import cv2
import numpy as np
import imutils

img = cv2.imread("../img/mano.jpg")
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
			A = np.array([55,55,55,55])

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
			g[j][k] = 0
			r[j][k] = 255
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
		elif E[j][k] == 12:
			b[j][k] = 0
			g[j][k] = 255
			r[j][k] = 255
		elif E[j][k] == 13:
			b[j][k] = 0
			g[j][k] = 0
			r[j][k] = 255
		elif E[j][k] == 14:
			b[j][k] = 50
			g[j][k] = 100
			r[j][k] = 255
		elif E[j][k] == 15:
			b[j][k] = 100
			g[j][k] = 20
			r[j][k] = 75
		elif E[j][k] == 16:
			b[j][k] = 250
			g[j][k] = 150
			r[j][k] = 100
		elif E[j][k] == 17:
			b[j][k] = 125
			g[j][k] = 125
			r[j][k] = 125
		elif E[j][k] == 18:
			b[j][k] = 83
			g[j][k] = 255
			r[j][k] = 25
		elif E[j][k] == 19:
			b[j][k] = 89
			g[j][k] = 145
			r[j][k] = 0
		elif E[j][k] == 20:
			b[j][k] = 255
			g[j][k] = 255
			r[j][k] = 0
		elif E[j][k] == 21:
			b[j][k] = 79
			g[j][k] = 255
			r[j][k] = 90
		elif E[j][k] == 22:
			b[j][k] = 65
			g[j][k] = 65
			r[j][k] = 255
		elif E[j][k] == 23:
			b[j][k] = 152
			g[j][k] = 254
			r[j][k] = 0
		elif E[j][k] == 24:
			b[j][k] = 15
			g[j][k] = 255
			r[j][k] = 150

img[:, :, 0] = r
img[:, :, 1] = g
img[:, :, 2] = b

print (et)

cv2.imwrite("pp.jpeg",img)
img1=cv2.imread("./pp.jpeg")

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
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
cv2.circle(img1, left, 5, (0, 0, 255), -1)
cv2.circle(img1, right, 5, (0, 0, 255), -1)
cv2.circle(img1, (int(centx), int(centy)), 5, (0, 0, 255), -1)
cv2.line(img1, left, right, (255,0,0), 2)
cv2.drawContours(img1, [c], -1, (0,255,0), 2)
cv2.rectangle(img1,(x,y),(x+w,y+h),(0,255,0),2)
cv2.putText(img1,'Distance: '+str(distance),(10,30), font, 1, (0,0,0),2, cv2.LINE_AA)
cv2.imshow('img', img1)

cv2.imshow("Mano", img)

cv2.waitKey()