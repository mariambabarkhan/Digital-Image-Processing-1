import cv2

# Load an RGB image
image = cv2.imread('cat.jpg')

# Convert the RGB image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display or save the grayscale image
cv2.imshow('Grayscale Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

