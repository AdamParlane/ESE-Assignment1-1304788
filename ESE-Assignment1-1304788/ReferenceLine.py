class ReferenceLine():

    """Finds and draws the reference line, this is used to create a scale factor to convert pixels to mm"""

    global cv2
    import cv2

    def __init__(self, referencePins):
        # initialise the object with the required data
        self.frame = referencePins.frame
        self.centres = referencePins.centres
        self.scaleFactor = 0

    def calculateScaleFactor(self):
        # if there are 2 reference pins, proceed with making a line
        if (len(self.centres) == 2):
            # calculate the difference between x1 & x2
            differenceX = self.centres[-1][-2] - self.centres[-2][-2]
            # calculate the difference between y1 & y2
            differenceY = self.centres[-1][-1] - self.centres[-2][-1]
            # claculate the absolute distance between the 2 points using dx and dy
            distance = (differenceX**2 + differenceY**2)**0.5
            # check that the distance is greater than 50px i.e. it has detected 2 different pins
            if (distance > 50):
                # draw a red line from pin 1 to pin 2 on frame
                cv2.line(self.frame, self.centres[-1], self.centres[-2], (0, 0, 255), thickness = 2, lineType=8, shift=0)
                #calculate the scale factor, this will reduce linear px measurements to mm
                self.scaleFactor = 100 / distance
