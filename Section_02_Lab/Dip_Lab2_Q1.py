import cv2

# Read the image
image = cv2.imread('image.jpg')

# Convert from BGR to RGB
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the original and RGB-converted images
cv2.imshow('Original Image (BGR)', image)
cv2.imshow('RGB Image', rgb_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()