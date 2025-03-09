import cv2

# Read the image
image = cv2.imread('image.jpg')

# Resize the image by half
resized_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Convert the resized image from BGR to HSV
hsv_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2HSV)

# Save the resized and HSV-converted images
cv2.imwrite('resized_image.jpg', resized_image)
cv2.imwrite('hsv_image.jpg', hsv_image)