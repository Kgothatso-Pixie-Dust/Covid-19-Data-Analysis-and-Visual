import os 
from PIL import Image
import matplotlib.pyplot as plt
import cv2
from skimage.filters import threshold_local
import numpy as np
import cv2
import imutils

def load_images_from_directory(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith('png'):
            img_path = os.path.join(directory, filename)
            images.append(img_path)
    return images

def display_images(images):
    for img_path in images:
        img = Image.open(img_path)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
normal_images_dir = 'TB_Chest_Radiography_Database/Normal/'  
tuberculosis_images_dir = 'TB_Chest_Radiography_Database/Tuberculosis/'  
normal_images = load_images_from_directory(normal_images_dir)  
tuberculosis_images = load_images_from_directory(tuberculosis_images_dir)  
