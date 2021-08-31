import cv2
import numpy as np

path = 'D:\Study\opencv\eval1\imag.png'
img = cv2.imread(path)

cv2.imshow('original image',img)

print("original image shape:",img.shape)

row,col,plane = img.shape

x, y = 2, 2

plane1 = img[:,:,0]

plane2 = img[:,:,1]

plane3 = img[:,:,2]

resize_plane1 = plane1[1::x,1::x]

resize_plane2 = plane2[1::x,1::x]

resize_plane3 = plane2[1::x,1::x]

resize_img = np.zeros((row//x, col//y, plane),np.uint8)

resize_img[:,:,0] = resize_plane1
resize_img[:,:,1] = resize_plane2
resize_img[:,:,2] = resize_plane3

cv2.imwrite('resize image.jpg',resize_img)

print("resize image shape:",resize_img.shape)
