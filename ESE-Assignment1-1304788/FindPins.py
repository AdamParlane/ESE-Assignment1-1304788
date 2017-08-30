class FindPins():
    'Finds the push pins of a selected colur'
    global cv2
    import cv2

    def __init__(self, frame, color):
        self.color = color[0]
        self.hueLow = color[1]
        self.hueHigh = color[2]
        self.BGR = color[3]
        self.frame = frame
        self.centres = []

    def findPinCentre(self):
        #import cv2
        # Convert to HSV
        hsv = cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
        # Create HSV Mask
        mask = cv2.inRange(hsv, (self.hueLow, 100, 50), (self.hueHigh, 255, 255))
        # Identify Contours In Mask
        contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        for i in range(len(contours)):
            moments = cv2.moments(contours[i])
            if(moments['m00'] != 0 and (cv2.contourArea(contours[i]) < 500) and (cv2.contourArea(contours[i]) > 50)):
                self.centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                cv2.circle(self.frame, self.centres[-1], 5, self.BGR, -1)
        



