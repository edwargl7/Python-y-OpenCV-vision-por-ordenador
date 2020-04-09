import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen_perro_BGR = cv2.imread('./images/perro.jpg')
print(type(imagen_perro_BGR))
print(imagen_perro_BGR.shape)

# OpenCV --> BGR (blue green red)
# Matplotlib --> RGB (red green blue)

# Transformar de BGR a RGB
imagen_perro_rgb = cv2.cvtColor(imagen_perro_BGR, cv2.COLOR_BGR2RGB)

img_sin_proc = plt.subplot(1, 2, 1)
plt.imshow(imagen_perro_BGR)
img_sin_proc.set_title('Formato BGR')

img_sin_proc = plt.subplot(1, 2, 2)
plt.imshow(imagen_perro_rgb)
img_sin_proc.set_title('Formato RGB')
plt.show()

imagen_perro_blanco_negro = cv2.imread('./images/perro.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(imagen_perro_blanco_negro, cmap='gray')
plt.show()
