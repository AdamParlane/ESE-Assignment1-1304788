import cv2
import cv2.cv as cv
import numpy as np
# Create Video Capture Object (0 is the camera number)
cap = cv2.VideoCapture(1)
while(True):
 # Capture frame-by-frame
 dragon = 0
 ret, frame = cap.read()
 # Convert To Greyscale
 hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 #for red
 hul = 0
 sal = 136
 val = 0
 huh = 15
 sah = 255
 vah = 255
 HSVLOW = np.array([hul, sal, val])
 HSVHIGH = np.array([huh, sah, vah])
 mask = cv2.inRange(hsv,HSVLOW, HSVHIGH)
 res = cv2.bitwise_and(frame,frame, mask =mask)
 grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 # Identify Circles
 circles = cv2.HoughCircles(grey,cv.CV_HOUGH_GRADIENT,1,60,param1=30, param2=30)
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
         dragon = dragon + 1
         #print locations of each centre point (mainly to check its working)
         cv2.putText(frame, 'X: %.f Y: %.f' %((i[0]), (i[1])), (30, (20*dragon) + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)


 cv2.imshow('image', res) 
 cv2.imshow('frame',frame)
 # Wait for user exit (press 'q')
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()

