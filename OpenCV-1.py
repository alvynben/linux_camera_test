import cv2
print(cv2.__version__)
cam=cv2.VideoCapture('/dev/video0')

while True:
    _, frame = cam.read()
    cv2.imshow('myCam',frame)
    cv2.moveWindow('myCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()