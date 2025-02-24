import cv2

def load_images(image_paths):
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        if image is not None:
            images.append(image)
        else:
            print(f"Failed to load image at {path}")
    return images

image_paths = ['Dr_Shashi_Tharoor.jph', 'Plaksha_Faculty.jpg']
images = load_images(image_paths)

print(f'Loaded {len(images)} images with shapes: {[img.shape for img in images]}')
