import cv2

img = cv2.imread('walle.jpg', 1)
imgResize = cv2.resize(img,(256, 256), interpolation = cv2.INTER_CUBIC)
cv2.imshow('Img', img)
cv2.imshow('Img1', imgResize)
cv2.waitKey(0)
cv2.destroyAllWindows()
