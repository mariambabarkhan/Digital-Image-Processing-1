import cv2

# Load a grayscale image
gray_image = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

# Set a threshold value (you can adjust this value as needed)
threshold_value = 128

# Apply binary thresholding
_, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Display or save the binary image
cv2.imshow('Binary Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

