import cv2

#create video capture object (0 is camera number)
cap = cv2.VideoCapture(0)

while(True):
    #capture frame by frame
    ret, frame = cap.read()

    #display the resulting frame
    cv2.imshow('frame', frame)

    #wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
           break;

#when everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()