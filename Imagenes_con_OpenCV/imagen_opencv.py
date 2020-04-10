import numpy as np
import matplotlib.pyplot as plt
import cv2

RUTA = './images/perro.jpg'


def cargar_imagen_con_opencv(ruta):
    print("""Cargar Imagen con OpenCV""")
    imagen_perro_BGR = cv2.imread(ruta)
    print(type(imagen_perro_BGR))
    print(imagen_perro_BGR.shape)

    # OpenCV --> BGR (blue green red)
    # Matplotlib --> RGB (red green blue)

    # Transformar de BGR a RGB
    imagen_perro_rgb = cv2.cvtColor(imagen_perro_BGR, cv2.COLOR_BGR2RGB)

    img_sin_proc = plt.subplot(1, 3, 1)
    plt.imshow(imagen_perro_BGR)
    img_sin_proc.set_title('Formato BGR')

    img_sin_proc = plt.subplot(1, 3, 2)
    plt.imshow(imagen_perro_rgb)
    img_sin_proc.set_title('Formato RGB')

    imagen_perro_blanco_negro = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
    img_sin_proc = plt.subplot(1, 3, 3)
    plt.imshow(imagen_perro_blanco_negro, cmap='gray')
    img_sin_proc.set_title("Blanco y Negro")
    plt.show()


def manipulacion_imagen(ruta):
    print("Manipulación de la imagen")
    imagen_perro_normal = cv2.imread(ruta)
    imagen_perro_normal = cv2.cvtColor(imagen_perro_normal, cv2.COLOR_BGR2RGB)
    img_proc = plt.subplot(2, 3, 1)
    plt.imshow(imagen_perro_normal, cmap='gray')
    img_proc.set_title('Normal')

    def cambiar_tamano(alto=200, ancho=100):
        return cv2.resize(imagen_perro_normal, (ancho, alto))

    def cambiar_tamano_porcentaje(ratio_alto=.5, ratio_ancho=.5):
        return cv2.resize(
            imagen_perro_normal, (0, 0),
            imagen_perro_normal, ratio_ancho, ratio_alto)

    def rotar_imagen(flip_op=0):
        """
        0 -> reflejo sobre el eje x, flip vertical
        > 0 -> reflejo sobre el eje y, flip horizontal
        < 0 -> reflejo sobre ambos ejes
        :param flip_op:
        :return:
        """
        return cv2.flip(imagen_perro_normal, flip_op)

    def guardar_imagen(ruta):
        imagen_aux = rotar_imagen()
        imagen_aux = cv2.cvtColor(imagen_aux, cv2.COLOR_RGB2BGR)
        if cv2.imwrite(ruta, imagen_aux):
            print('Imagen guardada en {}'.format(ruta))
        else:
            print("No se pudo guardar la imagen")

    img_proc = plt.subplot(2, 3, 2)
    plt.imshow(cambiar_tamano())
    img_proc.set_title("Resize")

    img_proc = plt.subplot(2, 3, 3)
    plt.imshow(cambiar_tamano_porcentaje())
    img_proc.set_title("Resize porcentaje")

    img_proc = plt.subplot(2, 3, 4)
    plt.imshow(rotar_imagen(0))
    img_proc.set_title("vertical flip")

    img_proc = plt.subplot(2, 3, 5)
    plt.imshow(rotar_imagen(1))
    img_proc.set_title("horizontal flip")

    img_proc = plt.subplot(2, 3, 6)
    plt.imshow(rotar_imagen(-1))
    img_proc.set_title("flip en ambos ejes")

    # Ajuste distancia entre cada subplot
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)
    plt.show()

    guardar_imagen('./images/perro_reflejo.jpg')
cargar_imagen_con_opencv(RUTA)
manipulacion_imagen(RUTA)
