import cv2  as cv

img = cv.imread('D:/Study/opencv/open-cv-4hrs/Photos/musk.jpg') # Read image

cv.imshow('Musk',img) #display image


def rescaleFrame(frame,scale =0.75):
    # Works only for live video,image and video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,height):
    # Works only for live video
    capture.set(width,3)
    capture.set(height,4)


resized_img = rescaleFrame(img)
cv.imshow("Resized",resized_img)

capture = cv.VideoCapture('D:/Study/opencv/open-cv-4hrs/Videos/test1.mp4') # 0 or 1 value will use injected camera

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame,scale=0.2)

    cv.imshow('Video',frame)
    cv.imshow('Video',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'): # waitkey to specify time and 0xFF is to specify quit window 
        break

capture.release()
cv.destroyAllWindows()


