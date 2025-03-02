import cv2

# Load the image
image_path = 'amr-sticker.png'
image = cv2.imread(image_path)
new_path = 'amr-stick2.png' 

cv2.imwrite(new_path, image)