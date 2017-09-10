class FindPins():

    """Finds the push pins of a selected colur"""

    global cv2
    import cv2

    def __init__(self, frame, color):
        # initialise the object with the required data
        self.hueLow = color[1]
        self.hueHigh = color[2]
        self.BGR = color[3]
        self.frame = frame
        self.centres = []

    def findPinCentre(self):
        # convert to HSV
        hsv = cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
        # create HSV mask with iput hue range, saturation range 100-255, value range 50-255
        mask = cv2.inRange(hsv, (self.hueLow, 100, 50), (self.hueHigh, 255, 255))
        # identify contours in mask
        contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        # find and mark the centre of each pin
        for i in range(len(contours)):
            moments = cv2.moments(contours[i])
            # if there are still moments left and they are in size range (50 - 500 px)
            if(moments['m00'] != 0 and (cv2.contourArea(contours[i]) < 500) and (cv2.contourArea(contours[i]) > 50)):
                # add the new centre to the centres list
                self.centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                # draw dots at the centres of each pin
                cv2.circle(self.frame, self.centres[-1], 5, self.BGR, -1)
        



