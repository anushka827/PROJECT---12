# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qqG8glgfYPlZIKyhSetHMqRwgsf0K6ZZ
"""

import cv2
from google.colab.patches import cv2_imshow

# Read the color image
image = cv2.imread('pexels-chevanon-1108099.jpg')

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite('pexels-chevanon-1108099_gray.jpg', gray_image)

    # Display the grayscale image safely in Colab
    cv2_imshow(gray_image)