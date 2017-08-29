class FindPins():
    'Finds the push pins of a selected colur'
    #global cv2
    import cv2
    import numpy as np

    pinCount = 0

    def __init__(self, frame, hueLow, hueHigh):
        self.hueLow = hueLow
        self.hueHigh = hueHigh
        self.frame = frame
        self.X = 0
        self.Y = 0
        self.centres = []
        #pinCount += 1

    def findPinCentre(self):
        import cv2
        # Convert to HSV
        hsv = cv2.cvtColor(self.frame,cv2.COLOR_BGR2HSV)
        # Create HSV Mask
        mask = cv2.inRange(hsv, (self.hueLow, 136, 50), (self.hueHigh, 255, 255))
        # Identify Contours In Mask
        contours, _ = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        # Find Largest Area Contour (Our Object of Interest)
        for i in range(len(contours)):

            max_area = 0
            # Check each Contour
            # If we have one
            moments = cv2.moments(contours[i])
                        #if (cv2.contourArea(contours[i]) < 100) # and cv2.contourArea(contours[i] > 10))
            if(moments['m00'] != 0 and (cv2.contourArea(contours[i]) < 500) and (cv2.contourArea(contours[i]) > 50)):
                self.centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
                cv2.circle(self.frame, self.centres[-1], 5, (0, 0, 255), -1)

        



