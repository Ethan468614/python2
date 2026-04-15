import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)

rotated =  cv2.warpAffine(image_rgb, M, (w, h))

plt.imshow(rotated)
plt.title('Rotated Image')
plt.show()

brightness_matrix = np.ones(image_rgb.shape, dtype='uint8') * 50
briter =  cv2.add(image_rgb, brightness_matrix)

briter_rgb = cv2.cvtColor(briter, cv2.COLOR_BGR2RGB)
plt.imshow(briter_rgb)
plt.title('Brightened Image')
plt.show()    