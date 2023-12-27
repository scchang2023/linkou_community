import cv2
import pyzbar.pyzbar as pyzbar

cap=cv2.VideoCapture(0)
while(True):
    ret,frame=cap.read()
    decodeObjects=pyzbar.decode(frame)
    for obj in decodeObjects:
        print(obj.data)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()