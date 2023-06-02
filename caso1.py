# 1).- Se requiere crear un vector de tamaño 100, completar los valores del vector aleatoriamente 
# con números enteros del 0 al 10, para ello deberá investigar la función que permita crear números aleatorios.
# import random
# vector = []
# for i in range(100):
#     numero = random.randint(0, 10)
#     vector.append(numero)
# print(vector)

# 2).- Mostrar por pantalla sólo los valores que se encuentren en los índices pares

# import random
# vector = []
# for i in range(100):
#     numero = random.randint(0, 10)
#     if (numero %2 == 0) :
#         vector.append(numero)
# print(vector)

# 3).- Mostrar el elemento mayor, sólo 1 en caso de repetirse.

# import random
# import numpy as np
# vector = []
# for i in range(100):
#     numero = random.randint(0, 10)
#     vector.append(numero)
# arreglo =np.array(vector)
# print(arreglo.max())

# 4).- Mostrar el índice (posición) del elemento mayor.

# import random
# import numpy as np
# vector = []
# for i in range(100):
#     numero = random.randint(0, 10)
#     vector.append(numero)
# arregloMayor = vector.index(max(vector))
# print(vector)
# print(arregloMayor)

# 5).- Mostrar el elemento menor.

# import random
# import numpy as np
# vector = []
# for i in range(100):
#     numero = random.randint(0, 10)
#     vector.append(numero)
# arreglo =np.array(vector)
# print(arreglo)
# print(arreglo.min())

# 6).- Mostrar el índice del elemento menor.

# import random
# import numpy as np
# vector = []
# for i in range(100):
#     numero = random.randint(0, 10)
#     vector.append(numero)
# arregloMenor = vector.index(min(vector))
# print(vector)
# print(arregloMenor)

# 7).- Crear un Vector de tamaño 10 que almacene nombres de personas.import random

import random
nombres = ["Rodrigo", "Andres", "Javier", "Raul", "Fernando", "Manuel", "Juan", "Alberto", "Luis", "Alejandro"]
vector_nombres = []
for i in range(10):
    nombre = random.choice(nombres)
    vector_nombres.append(nombre)
print(vector_nombres)