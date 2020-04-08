import numpy as np

# Manejo de arrays con numpy
# Arreglo desde el 5 hasta el 19 con salto de 3
arreglo_uno = np.arange(5, 20, 3)
print("Arreglo general de salto de 3:\n {}\n\n".format(arreglo_uno))

# Matriz de ceros 10x2
matriz_ceros = np.zeros(shape=(10, 2))
print("Arreglo ceros 10x2:\n {}\n\n".format(matriz_ceros))

# Matriz de unos de 5x4
matriz_unos = np.ones(shape=(5, 4))
print("Matriz unos 5x4:\n {}\n\n".format(matriz_unos))

# Números aleatorios, 50 número entre 0 y 99
vector_aleatorios = np.random.randint(0, 100, 50)
print("50 npumeros aleatorios:\n {}\n\n".format(vector_aleatorios))

# Posición del valor máximo del arreglo
print("Posición del valor máximo del arreglo: \n{}\n\n".format(
    vector_aleatorios.argmax()))

# Valor máximo del arreglo
print("Número mayor del arreglo: \n{}\n\n".format(vector_aleatorios.max()))

# Posición del valor mínimo del arreglo
print("Posición del valor mínimo del arreglo: \n{}\n\n".format(
    vector_aleatorios.argmin()))

# Valor mínimo del arreglo
print("Número menor del arreglo: \n{}\n\n".format(vector_aleatorios.min()))

# Forma del arreglo
print("Forma del arreglo: \t{}\n\n".format(vector_aleatorios.shape))

# Transformar forma del arreglo
matriz_aleatorios = vector_aleatorios.reshape(10, 5)
print("Transformación forma del arreglo:\n{}\n\n".format(matriz_aleatorios))

# Acceder a un elemento del arreglo
print("Acceder a un elemento del arreglo:\n{}".format(matriz_aleatorios[0,1]))
print("{}\n\n".format(matriz_aleatorios[0][3]))
