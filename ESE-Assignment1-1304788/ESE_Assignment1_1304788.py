import cv2
import numpy
from FindPins import FindPins
from ReferenceLine import ReferenceLine
cap = cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()

    redPins = FindPins(frame, 0, 15)
    redPins.findPinCentre()

    bluePins = FindPins(frame, 100, 115)
    bluePins.findPinCentre()
    print redPins.centres


    refLine = ReferenceLine(redPins)
    refLine.calculateScaleFactor()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # Wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()