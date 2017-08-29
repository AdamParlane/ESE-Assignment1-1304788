class ReferenceLine():
    """description of class"""

    def __init__(self, redPins):
        self.frame = redPins.frame
        self.centres = redPins.centres

    def calculateScaleFactor(self):
        import cv2
        self._drawReferenceLine()
        if (len(self.centres) > 1):
            differenceX = self.centres[-1][-2] - self.centres[-2][-2]
            differenceY = self.centres[-1][-1] - self.centres[-2][-1]
            distance = (differenceX**2 + differenceY**2)**0.5
            print distance

    def _drawReferenceLine(self):
        import cv2
        if (len(self.centres) > 1):
            cv2.line(self.frame, self.centres[-1], self.centres[-2], (0, 0, 255), thickness = 2, lineType=8, shift=0)
