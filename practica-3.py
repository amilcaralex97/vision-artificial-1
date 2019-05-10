import cv2
import numpy as np


mano="../img/mano.jpg"

img = cv2.imread(mano)
et = 1

b = img[:, :, 2]
g = img[:, :, 1]
r = img[:, :, 0]

E = np.zeros_like(b)

for x in range(len(b)):
	for y in range(len(b[x])):
		if b[x][y] < 180 or g[x][y] < 180 or r[x][y] < 230:
			b[x][y] = 255
			g[x][y] = 255
			r[x][y] = 255
		else:
			b[x][y] = 0
			g[x][y] = 0
			r[x][y] = 0

for x in range(len(r)):
	for y in range(len(r[x])):
		if r[x][y] == 255:
			A = np.array([50,50,50,50])

			if r[x-1][y-1] != 0: A[0] = E[x-1][y-1] 
			if r[x-1][y] != 0: A[1] = E[x-1][y]	
			if r[x-1][y+1] != 0: A[2] = E[x-1][y+1]
			if r[x][y-1] != 0: A[3] = E[x][y-1]

			if r[x-1][y-1] == 255 or r[x-1][y] == 255 or r[x-1][y+1] == 255 or r[x][y-1] == 255:
				E[x][y] = A.min()
				if E[x-1][y-1] 	> E[x][y]: E[x-1][y-1]	= E[x][y]
				if E[x-1][y]	> E[x][y]: E[x-1][y]	= E[x][y]
				if E[x-1][y+1]	> E[x][y]: E[x-1][y+1]	= E[x][y]
				if E[x][y-1] 	> E[x][y]: E[x][y-1]	= E[x][y]
			else:
				E[x][y] = et
				et += 1

for x in range(len(E)):
	for y in range(len(E[x])):
		if E[x][y] == 1:
			b[x][y] = 0
			g[x][y] = 255
			r[x][y] = 0
		elif E[x][y] == 2:
			b[x][y] = 0
			g[x][y] = 255
			r[x][y] = 255
		elif E[x][y] == 3:
			b[x][y] = 25
			g[x][y] = 100
			r[x][y] = 25
		elif E[x][y] == 4:
			b[x][y] = 205
			g[x][y] = 5
			r[x][y] = 5
		elif E[x][y] == 5:
			b[x][y] = 11
			g[x][y] = 13
			r[x][y] = 56
		elif E[x][y] == 6:
			b[x][y] = 123
			g[x][y] = 45
			r[x][y] = 12
		elif E[x][y] == 7:
			b[x][y] = 12
			g[x][y] = 54
			r[x][y] = 15
		elif E[x][y] == 8:
			b[x][y] = 5
			g[x][y] = 0
			r[x][y] = 55
		elif E[x][y] == 9:
			b[x][y] = 55
			g[x][y] = 2
			r[x][y] = 255
		elif E[x][y] == 10:
			b[x][y] = 123
			g[x][y] = 93
			r[x][y] = 3
		elif E[x][y] == 11:
			b[x][y] = 123
			g[x][y] = 12
			r[x][y] = 76

print (et)



lefalta=cv2.merge((b,g,r))

# red color boundaries (R,B and G)
lower = [1, 0, 20]
upper = [60, 40, 200]

# create NumPy arrays from the boundaries
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")


mask = cv2.inRange(lefalta, lower, upper)
output = cv2.bitwise_and(lefalta, lefalta, mask=mask)

ret,thresh = cv2.threshold(mask, 40, 255, 0)
im2,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

if len(contours) != 0:
    # draw in blue the contours that were founded
    cv2.drawContours(output, contours, -1, 255, 3)

    #find the biggest area
    c = max(contours, key = cv2.contourArea)

    x,y,w,h = cv2.boundingRect(c)
    # draw the book contour (in green)
    cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),2)

# show the images
cv2.imshow("Result", np.hstack([lefalta, output]))
cv2.waitKey(0)
cv2.destroyAllWindows()