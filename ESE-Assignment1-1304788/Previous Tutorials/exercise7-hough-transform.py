import cv2
import numpy as np
# Create Video Capture Object (0 is the camera number)
cap = cv2.VideoCapture(1)
while(True):
 # Capture frame-by-frame
 ret, frame = cap.read()
 # Convert To Greyscale
 grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 # Filter Image (See Next Week's Lab)
 grey = cv2.medianBlur(grey,5)
 # Edge Detection
 edges = cv2.Canny(grey,40,80)
 # Line Detection
 lines = cv2.HoughLines(edges,1,np.pi / 180,100)
 # Plot Lines
 if(lines != None):
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
 # Display the resulting frame
 cv2.imshow('frame',frame)
# cv2.imshow('frame2',edges)
 # Wait for user exit (press 'q')
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()
