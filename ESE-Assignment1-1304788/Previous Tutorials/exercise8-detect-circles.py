import cv2
import cv2.cv as cv
import numpy as np
# Create Video Capture Object (0 is the camera number)
cap = cv2.VideoCapture(1)
while(True):
 # Capture frame-by-frame
 ret, frame = cap.read()
 # Convert To Greyscale
 grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 # Identify Circles
 circles = cv2.HoughCircles(grey,cv.CV_HOUGH_GRADIENT,1,20,param1=40, param2=30, minRadius=5, maxRadius=30)
 if(circles != None):
     # Convert to Numpy array
     circles = np.uint16(np.around(circles))
     # For Each Circle, Draw It
     for i in circles[0,:]:
         # draw the outer circle
         cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),2)
         # draw the center of the circle
         cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)
         # Display the resulting frame
 cv2.imshow('frame',frame)
 # Wait for user exit (press 'q')
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()

