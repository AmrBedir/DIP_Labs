import cv2
import imutils

# Read the image
image = cv2.imread('image.jpg')

# Rotate the image by 45 degrees without cropping
rotated_image = imutils.rotate_bound(image, 45)

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()