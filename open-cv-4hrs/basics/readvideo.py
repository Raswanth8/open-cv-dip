import cv2  as cv

capture = cv.VideoCapture('D:/Study/opencv/open-cv-4hrs/Videos/test1.mp4') # 0 or 1 value will use injected camera

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF == ord('d'): # waitkey to specify time and 0xFF is to specify quit window 
        break

capture.release()
cv.destroyAllWindows()


