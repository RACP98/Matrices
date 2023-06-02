#debemos importar libreria numpy
import numpy as np

#para trabajar ocn la lib debemos instanciar un arreglo y declararlo como un
#array de numpy(si utiliza alias, recuerde instanciar por el alias)
arreglo = np.array([1, 2, 3, 4, 7])
#para saber la dimension del arreglo
print("arreglo de: ",arreglo.ndim,"dimensión")
#para imprimir el arreglo
print(arreglo)
#para saber el largo del arreglo
# print(len(arreglo))
#para traer el largo del arreglo seguido de una ','
print(arreglo.shape)
#para imprimir  elementos de un array en posiciones seleccionadas.
# print(arreglo[1:3])

#recorrer arreglos
for i in arreglo:
    print(i)
    
#para crear un arreglo de manera automatica debemos utilizar la prop arange(x)
#donde x es el valor excluyente de este arreglo
array = np.arange(15)
print(array)
#para crear un arreglo de manera automatica con inicio y fin declarados debemos utilizar la prop arange(x, y)
#donde 'x' es el valor inicial e 'y' el valor final de este arreglo (recuerde que el valor es excluyente)
array2 = np.arange(5, 15)
print(array2)
#si desea crear un arreglo y que sus elementos tengan un punto (.) debera crearlo con la
#prop arange(x.z) donde x es el largo del array y z es para "decirle a python, aca pon un ."
array3 = np.arange(7.0)
print(array3)

#para imprimir arreglos con un inicio, fin y paso determinado, debemos utilizar la prop arange(x, y, z)
#donde x es el valor inicial; y es el valor final (excluyente); z el paso
array4 = np.arange(2, 7, 2)

