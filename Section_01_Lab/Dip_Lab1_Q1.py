import cv2

# Load the image
image_path = 'amr-sticker.png'  
image = cv2.imread(image_path)
cv2.imshow('Wa3di ya Wa3di', image)
cv2.waitKey(0)
cv2.destroyAllWindows()