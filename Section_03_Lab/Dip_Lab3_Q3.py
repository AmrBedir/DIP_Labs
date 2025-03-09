import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('amr-sticker.png')

# Flip the image vertically
flipped_image = cv2.flip(image, 0)

# Convert BGR to RGB for matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
flipped_image_rgb = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2RGB)

# Display the images side by side using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(flipped_image_rgb)
plt.title('Vertically Flipped Image')

plt.show()