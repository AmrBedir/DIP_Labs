import cv2

# Read the colored image
image = cv2.imread('image.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to convert grayscale to black and white
_, black_white_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the original and black-and-white images
cv2.imshow('Original Image', image)
cv2.imshow('Black and White Image', black_white_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()