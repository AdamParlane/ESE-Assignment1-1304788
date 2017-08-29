import cv2

cap = cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()

    frame = cv2.medianBlur(frame, 11)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
