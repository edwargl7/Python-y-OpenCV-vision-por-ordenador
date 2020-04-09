import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Cargar imagen
imagen_perro = Image.open('./images/perro.jpg')
imagen_perro.show()
print(type(imagen_perro))
print("Tamaño imagen: {}".format(imagen_perro.size))

# Convertir imagen en array
array_image = np.asarray(imagen_perro)

# Plotear arreglo
plot_general = plt.subplot(2, 2, 1)
plt.imshow(array_image)
plot_general.set_title('General')
print("Tamaño array: {}".format(array_image.shape))

plot_red = plt.subplot(2, 2, 2)
plt.imshow(array_image[:, :, 0])
plot_red.set_title('Red')

plot_green = plt.subplot(2, 2, 3)
plt.imshow(array_image[:, :, 1])
plot_green.set_title('Green')

plot_blue = plt.subplot(2, 2, 4)
plt.imshow(array_image[:, :, 2])
plot_blue.set_title('Blue')

plt.tight_layout()
plt.show()
