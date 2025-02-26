import cv2
import numpy as np
import os

image_paths = [
    'Plaksha_Faculty.jpg',
    'Dr_Shashi_Tharoor.jpg'
]

def load_images(image_paths):
    images = []
    for path in image_paths:
        if not os.path.exists(path):
            print(f"Error: File '{path}' not found.")
            continue
        
        image = cv2.imread(path)
        if image is not None:
            images.append(image)
            print(f"Loaded image: {path} with shape {image.shape}")
        else:
            print(f"Error: Failed to load image '{path}'.")
    return images

images = load_images(image_paths)

for i, img in enumerate(images):
    cv2.imshow(f'Image {i+1}', img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
