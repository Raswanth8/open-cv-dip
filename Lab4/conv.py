
import cv2
import numpy as np

img = cv2.imread("D:\Study\opencv\Lab4\imag.png")
filter_matrix = np.array([[-1,-2,-1], [0,0,0], [1, 2, 1]])
dst = cv2.filter2D(img,-1, filter_matrix)
cv2.imwrite("conv.jpg", dst)