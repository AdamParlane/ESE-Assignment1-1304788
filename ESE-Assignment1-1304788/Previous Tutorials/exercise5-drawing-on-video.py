import cv2
# Create Video Capture Object (0 is the camera number)
cap = cv2.VideoCapture(0)
while(True):
 # Capture frame-by-frame
 ret, frame = cap.read()
 # Draw a Red Circle Inside a Blue Square
 rad = 50
 cntr = int(cap.get(3)/2.0),int(cap.get(4)/2.0)
 p1 = cntr[0]-rad,cntr[1]-rad
 p2 = cntr[0]+rad,cntr[1]+rad
 cv2.circle(frame,cntr,rad,(0,0,255),2)
 cv2.rectangle(frame,p1,p2,(255,0,0),2)
 # Display the resulting frame
 cv2.imshow('frame',frame)
 # Wait for user exit (press 'q')
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()
