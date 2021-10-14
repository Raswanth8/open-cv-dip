import cv2


img = cv2.imread("D:\Study\opencv\eval2\imag.png")
scale_percent = 110
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

scaled2 = cv2.resize(img,dim,interpolation=cv2.INTER_CUBIC)


cv2.imwrite("Bicubic.jpg", scaled2)
