class ReferenceLine():
    """description of class"""
    global cv2
    import cv2

    def __init__(self, referencePins):
        self.frame = referencePins.frame
        self.centres = referencePins.centres
        self.scaleFactor = 0

    def calculateScaleFactor(self):
        #import cv2
        self._drawReferenceLine()
        if (len(self.centres) > 1):
            differenceX = self.centres[-1][-2] - self.centres[-2][-2]
            differenceY = self.centres[-1][-1] - self.centres[-2][-1]
            distance = (differenceX**2 + differenceY**2)**0.5
            if (distance > 50):
                self.scaleFactor = 100 / distance

    def _drawReferenceLine(self):
        import cv2
        if (len(self.centres) > 1):
            cv2.line(self.frame, self.centres[-1], self.centres[-2], (0, 0, 255), thickness = 2, lineType=8, shift=0)
