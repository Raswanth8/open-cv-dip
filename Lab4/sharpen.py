
import cv2
import numpy as np
img = cv2.imread("D:\Study\opencv\Lab4\imag.png")
filter_matrix = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
dst = cv2.filter2D(img,-1, filter_matrix)
cv2.imwrite("sharpen.jpg", dst)