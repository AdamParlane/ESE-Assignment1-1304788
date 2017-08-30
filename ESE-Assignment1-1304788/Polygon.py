class Polygon():

    """description of class"""
    global cv2
    import cv2
    global np
    import numpy as np
    #TODO: improve moving average
    sarea = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    a = 0

    def __init__(self, polygonPins, refLine):
        self.frame = polygonPins.frame
        self.centres = polygonPins.centres
        self.BGR = polygonPins.BGR
        self.scale = refLine.scaleFactor
        self.area = 0

    def displayArea(self):
        self.findConvexHull()
        sum = 0
        sumX = 0
        sumY = 0
        if(self.scale):
            trueArea = self.area * (self.scale**2) /100
            for i in range(len(self.centres)):
                sumX += self.centres[i][0]
                sumY += self.centres[i][1]
            centreX = sumX / len(self.centres)
            centreY = sumY / len(self.centres)
            cv2.putText(self.frame, 'Area %.2f cm2' % (trueArea), (centreX - 60, centreY + 100),
                cv2.FONT_HERSHEY_SIMPLEX,0.5, self.BGR, 1)
            Polygon.sarea[Polygon.a] = trueArea
            sum = 0
            for i in range(10):
                sum += Polygon.sarea[i]
            average = (sum / 10)
            Polygon.a += 1
            if(Polygon.a == 10):
                Polygon.a = 0
            print Polygon.sarea
            print average
            cv2.putText(self.frame, 'Area %.2f cm2' % (average), (centreX - 60, centreY),
                cv2.FONT_HERSHEY_SIMPLEX,0.5, self.BGR, 1)

    def findConvexHull(self):
        points = np.array(self.centres)
        hull = cv2.convexHull(points)
        cv2.drawContours(self.frame, [hull], -1, self.BGR, 2)
        self.area = cv2.contourArea(hull)
