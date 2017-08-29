class ReferenceLine():
    """description of class"""

    def __init__(self, redPins):
        self.frame = redPins.frame
        self.centres = redPins.centres

    def calculateScaleFactor(self):
        self._drawReferenceLine()

    def _drawReferenceLine(self):
        import cv2
        if (len(self.centres) > 1):
            cv2.line(self.frame, self.centres[-1], self.centres[-2], (0, 0, 255), thickness = 2, lineType=8, shift=0)
