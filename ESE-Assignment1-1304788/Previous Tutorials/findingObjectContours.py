import cv2
# Create Video Capture Object (0 is the camera number)
cap = cv2.VideoCapture(1)


while(True):
     # Capture frame-by-frame
     ret, frame = cap.read()
     # Convert to HSV
     hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
     # Create HSV Mask
     mask = cv2.inRange(hsv, (105,50,50), (125,255,255))
     # Identify Contours In Mask
     contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
     # Find Largest Area Contour (Our Object of Interest)
     if(len(contours) > 0):
         max_area = 0
         ci = None
         # Check each Contour
         for cnt in contours:
             area = cv2.contourArea(cnt)
             if(area > max_area):
                 max_area = area
                 ci = cnt
         # If we have one
         if(ci != None):
             #Draw it
             cv2.drawContours(frame,[ci],0,(255,0,0),2)
     # Display the resulting frame
     cv2.imshow('frame',frame)
     # Wait for user exit (press 'q')
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()

