import cv2


#create video capture object (0 is camera number)
cap = cv2.VideoCapture(1)
cap.set(3, 1080)
cap.set(4, 1920)


while(True):
    #capture frame by frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #threshold
    _,thresh = cv2.threshold(gray, 75, 255, cv2.THRESH_BINARY)


    #display the resulting frame
    cv2.imshow('frame', thresh)

    #wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
           break;

#when everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()
