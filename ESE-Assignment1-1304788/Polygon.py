class Polygon():

    """Finds and displays the area of the polygon based on the scale factor from referenceLine
    This is done using openCV functions ConvexHull and ContourArea
    A moving average filter ustilising the last 10 values is also used to smooth out the effects of any spurious pin detection"""

    global cv2
    import cv2
    global np
    import numpy as np
    # declare empty list, window size and counter to store moving average values
    window = 50
    prevAreas = [0] * window
    counter = 0

    def __init__(self, polygonPins, refLine):
        # initialise object with required data
        self.frame = polygonPins.frame
        self.centres = polygonPins.centres
        self.BGR = polygonPins.BGR
        self.scale = refLine.scaleFactor
        self.area = 0

    def displayArea(self):
        # find the convex hull
        self.findConvexHull()
        sum = 0
        sumX = 0
        sumY = 0
        if(self.scale):
            # calculate the area using the scale factor and converting to mm^2
            trueArea = self.area * (self.scale**2) /100
            # calculate the centre of the polygon for label positioning
            # if statement to guard against division by 0
            if(len(self.centres) > 3):
                for i in range(len(self.centres)):
                    sumX += self.centres[i][0]
                    sumY += self.centres[i][1]
                centreX = sumX / len(self.centres)
                centreY = sumY / len(self.centres)
            else:
                # default label positions if shape centre not found
                centreX = 100
                centreY = 100
            # save the area value into the previous error list for the moving average filter
            Polygon.prevAreas[Polygon.counter] = trueArea
            # sum the [window] previous error values and average them to find the moving average
            for i in range(Polygon.window):
                sum += Polygon.prevAreas[i]
            average = (sum / Polygon.window)
            # increment the counter to go through each value of the prevArea list
            Polygon.counter += 1
            if(Polygon.counter == Polygon.window):
                Polygon.counter = 0
            #display the text showing the area
            cv2.putText(self.frame, 'Area %.2f cm2' % (average), (centreX - 60, centreY),
                cv2.FONT_HERSHEY_SIMPLEX,0.5, self.BGR, 1)

    def findConvexHull(self):
        # copy the contour centres to a numpy array
        points = np.array(self.centres)
        # if there are contours perform the moving average calculation
        if(len(self.centres) > 3):
            # find the hull using open CV convexHull
            hull = cv2.convexHull(points)
            # draw the lines between each point of the polygon using the hull
            cv2.drawContours(self.frame, [hull], -1, self.BGR, 2)
            # calculate the area using openCV contourArea
            self.area = cv2.contourArea(hull)

