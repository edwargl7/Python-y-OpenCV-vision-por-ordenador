import cv2
import numpy as np


def dibujar(evento, x, y, etiquetas, parametros):
    if evento == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x, y), 50, (255, 0, 0), -1)

# Conectar la imagen con la función dibujar
cv2.namedWindow(winname='mi_imagen')
cv2.setMouseCallback('mi_imagen', dibujar)

# Imagen donde se pintará
imagen = np.zeros((500, 500, 3), np.int8)

while True:
    cv2.imshow('mi_imagen', imagen)

    if cv2.waitKey(10) & 0xFF == 27:
        # ESC para salir
        break
cv2.destroyAllWindows()
