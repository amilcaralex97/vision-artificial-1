import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gaussian=cv2.GaussianBlur(gray,(5,5),0)
    sobelx = cv2.Sobel(gaussian,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(gaussian,cv2.CV_64F,0,1,ksize=5)
    G = np.hypot(sobelx, sobely)
    G = G / G.max() * 255
    theta = np.arctan2(sobely, sobelx)
    ###########################################################
    
# Display the resulting frame
    cv2.imshow('frame',theta)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()