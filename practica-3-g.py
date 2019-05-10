import numpy as np
import cv2
import imutils
mano="../img/mano.jpg"


img = cv2.imread(mano)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
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
cv2.circle(img, left, 5, (0, 0, 255), -1)
cv2.circle(img, right, 5, (0, 0, 255), -1)
cv2.circle(img, (int(centx), int(centy)), 5, (0, 0, 255), -1)
cv2.line(img, left, right, (255,0,0), 2)
cv2.drawContours(img, [c], -1, (0,255,0), 2)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.putText(img,'Distance: '+str(distance),(10,30), font, 1, (0,0,0),2, cv2.LINE_AA)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()