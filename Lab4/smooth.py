
import cv2
import numpy as np

img = cv2.imread("D:\Study\opencv\Lab4\imag.png")
filter_matrix = np.ones((11,11),np.float32)/(11*11)
dst = cv2.filter2D(img,-1, filter_matrix)
cv2.imwrite("smooth.jpg", dst)