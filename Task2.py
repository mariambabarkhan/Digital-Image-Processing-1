import cv2

image = cv2.imread("Capture.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = 120
maxValue = 255
th, dst = cv2.threshold(gray, threshold, maxValue, cv2.THRESH_BINARY)
cv2.imshow("Thresholded Image", dst)
cv2.waitKey(0)

#contours around black objects
contours, hierarchy = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(dst, contours, -1, (0, 0 , 255), 20)
cv2.imshow("Contours", dst)
cv2.waitKey(0)

count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100 and area < 100000:
        count += 1


print("Number of coins: ", count)




