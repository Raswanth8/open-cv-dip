
import cv2
import numpy

img_path = 'D:\Study\opencv\Lab3\imag.png'
image = cv2.imread(img_path)

ret, thresh_image = cv2.threshold(image,100,255,cv2.THRESH_BINARY)

cv2.imwrite("original.jpg", image)
cv2.imwrite("simple_thresh.jpg", thresh_image)
