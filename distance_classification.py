import os
import cv2

required_files = [
    'Plaksha_Faculty.jpg',
    'Dr_Shashi_Tharoor.jpg',
    'Lab 5-Spring 2025.ipynb'
]

for file_path in required_files:
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        continue
    
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        img = cv2.imread(file_path)
        if img is not None:
            print(f"Success: Image '{file_path}' loaded correctly.")
        else:
            print(f"Error: Failed to load image '{file_path}'.")
    else:
        print(f"Success: File '{file_path}' exists.")
