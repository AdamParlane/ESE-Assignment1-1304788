import cv2, time
from datetime import datetime


#create video capture object (0 is camera number)
cap = cv2.VideoCapture(1)
cap.set(3, 1080)
cap.set(4, 1920)
counter = 0

while(True):
    #capture frame by frame
    ret, frame = cap.read()
    counter = counter + 1
    #record current time
    t = time.time()

    g = datetime.now()

    #convert the image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #calcualate dt and display it on the fram
    dt = time.time() - t
    cv2.putText(gray, 'Adam is amazing for %.3f seconds' % (g.month), (30, 20),
                cv2.FONT_HERSHEY_SIMPLEX,0.5, (255,0,0),1)

    #display the resulting frame
    cv2.imshow('frame', gray)

    #wait for user exit (press 'q')
    if cv2.waitKey(1) & 0xFF == ord('q'):
           break;

#when everything done, release the capture (important!)
cap.release()
cv2.destroyAllWindows()
