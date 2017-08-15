import cv2
# Create Video Capture Object (0 is the camera number)
cap = cv2.VideoCapture(0)
while(True):
 # Capture frame-by-frame
 ret, frame = cap.read()
 # Convert the image to gray-scale
 gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
 # Canny Edge Detection
 edges = cv2.Canny(gray,100,200)
 # Display the resulting frame
 cv2.imshow('frame',edges)
 # Wait for user exit (press 'q')
 if cv2.waitKey(1) & 0xFF == ord('q'):
    break
# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()
