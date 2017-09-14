# import required modules
import cv2      
import numpy    
from FindPins import FindPins
from ReferenceLine import ReferenceLine
from Polygon import Polygon

# create capture video object from camera 1 (USB Webcam)
cap = cv2.VideoCapture(1)

# define pin colours ("color", HSV_Hue_Low, HSV_Hue_High, (BGR tuple))
red = ("red", 0, 30, (0, 0, 255))       # reference pins
blue = ("blue", 90, 125, (255, 0, 0))   # polygon pins
green = ("green", 50, 90, (0, 100, 0))  # secondary polygon pins

while(True):
    # capture frame-by-frame
    ret, frame = cap.read()
    # add a median filter to smooth contour irregularites
    frame = cv2.medianBlur(frame, 11)
    # find the locations of the red pins (the reference pins)
    

    redPins = FindPins(frame, red)
    redPins.findPinCentre()
    # find the locations of the blue pins (the polygon pins)
    bluePins = FindPins(frame, blue)
    bluePins.findPinCentre()
    # find the locations of the red pins (the secondary polygon pins)
    #greenPins = FindPins(frame, green)
    #greenPins.findPinCentre()

    # draw the reference line and calculate the scale factor
    refLine = ReferenceLine(redPins)
    refLine.calculateScaleFactor()

    # draw the blue convex polygon, calculate and display the area
    blueShape = Polygon(bluePins, refLine)
    blueShape.displayArea()
    # draw the green convex polygon, calculate and display the area
    #greenShape = Polygon(greenPins, refLine)
    #greenShape.displayArea()

    # add a watermark for authenticity
    cv2.putText(frame, 'Adam Parlane 2017, MA(50)', (40, 80),
        cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 0), 1)
    # display the resulting frame
    cv2.imshow('Adam Parlane 2017',frame)

    # wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()