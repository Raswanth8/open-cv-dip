import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('D:\Study\opencv\eval3\imag.png')

blur = cv2.boxFilter(img,-1,(6,6))

plt.subplot(121)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(122)
plt.imshow(blur)
plt.title('Blurred')
plt.xticks([])
plt.yticks([])
plt.savefig('plt.png')
cv2.imwrite("Blurred.jpg", blur)