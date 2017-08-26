import cv2


#create video capture object (0 is camera number)
cap = cv2.VideoCapture(1)
cap.set(3, 1080)
cap.set(4, 1920)


while(True):
    #capture frame by frame
    ret, frame = cap.read()

    frame = cv2.bilateralFilter(frame, 5, 50, 50)

    #display the resulting frame
    cv2.imshow('frame', frame)

    #wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
           break;

#when everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()
