import cv2
import numpy
from FindPins import FindPins
from ReferenceLine import ReferenceLine
from Polygon import Polygon

cap = cv2.VideoCapture(1)

#define pin colours ("color", HSV_Hue_Low, HSV_Hue_High, (BGR tuple))
red = ("red", 0, 30, (0, 0, 255))
blue = ("blue", 90, 125, (255, 0, 0))
green = ("green", 50, 90, (0, 100, 0))
yellow = ("yellow", 15, 30, (60, 240, 240))

sum = 0
a = 0
area = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while(True):
    ret, frame = cap.read()
    frame = cv2.medianBlur(frame, 11)
    redPins = FindPins(frame, red)
    redPins.findPinCentre()

    bluePins = FindPins(frame, blue)
    bluePins.findPinCentre()

    greenPins = FindPins(frame, green)
    greenPins.findPinCentre()

    #yellowPins = FindPins(frame, yellow)
    #yellowPins.findPinCentre()

    refLine = ReferenceLine(redPins)
    refLine.calculateScaleFactor()

    #print scaleFactor




    blueShape = Polygon(bluePins, refLine)
    blueShape.displayArea()
    #if (returnedArea):
    #    area[a] = returnedArea
    #    sum = 0
    #    for i in range(10):
    #        sum += area[i]
    #    average = (sum / 10)
    #    a += 1
    #    if(a == 10):
    #        a = 0
    #print area
    #print average

    #greenShape = Polygon(greenPins, refLine)
    #greenShape.displayArea()

    #yellowShape = Polygon(yellowPins)
    #yellowShape.findConvexHull()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # Wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

# When everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()