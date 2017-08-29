import cv2
import numpy
from FindPins import FindPins

cap = cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()
    #cv2.imshow('framde',frame)
    pin1 = FindPins(frame, 100, 125)
    pin1.findPinCentre()
    pin2 = FindPins(frame, 0, 15)
    pin2.findPinCentre()
    #cv2.circle(frame,(pin1.X,pin1.Y),5,(0,0,255),-1)
    cv2.putText(frame, 'X: %.f Y: %.f' %(pin1.X, pin1.Y), (30, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # Wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()