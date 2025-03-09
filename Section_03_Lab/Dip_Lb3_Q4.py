import cv2

# Read two images
image1 = cv2.imread('image.jpg')
image2 = cv2.imread('amr-sticker.png')

# Ensure both images have the same dimensions
image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Add the two images
added_image = cv2.add(image1, image2_resized)

# Display the original images and the result
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2_resized)
cv2.imshow('Added Image', added_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()