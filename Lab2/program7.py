import cv2


path = "D:\Study\opencv\imag.png"

print ('Path:', path)

#Reads image
img = cv2.imread(path)

if img is None:
    print ("image is not valid")

#saving a copy of the image
cv2.imwrite('copy_of_image.jpg', img)

# displays image
cv2.imshow("output",img)




