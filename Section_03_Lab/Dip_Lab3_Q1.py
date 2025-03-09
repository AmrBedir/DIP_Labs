import cv2

# Read the image
image = cv2.imread('amr-sticker.png')

# Crop the image
cropped_image = image[50:300, 100:500]  # Crop from (y1=50, x1=100) to (y2=300, x2=500)

# Flip the cropped image horizontally
flipped_image = cv2.flip(cropped_image, 1)

# Display the original, cropped, and flipped images
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Flipped Image', flipped_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()