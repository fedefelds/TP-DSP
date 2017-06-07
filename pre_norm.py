##################################################

# los argumentos de entrada de funcion_nueva son los siguientes:

# matriz_de_intervalos: Esta matriz es el resultado de aplicar separar.py a una
# señal:
#
# matriz_de_intervalos[i]==start and end time (in samples) of non-silent interval i.
# Ej:
# matriz_de_intervalos[1]==[59500,80550] <-- hay un intervalo no silencioso cuando 59500<n<80550
##################################################

# esta funcion devuelve los siguientes:

# fragmento: fragmento es un array
# arg: descripcion..tipo de var..ejemplo..nota

##################################################

import librosa
import numpy as np
from cargar_audio import cargar_audio  # todo:  si no escribo esto asi, me da 'module object is not callable'
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000



# matriz_de_intervalos[i]==start and end time (in samples) of non-silent interval i.
# Ej:
# matriz_de_intervalos[1]==[59500,80550]
#
# 1) crear una matriz nula de a filas y b columnas. El numero filas a es igual a
# la cantidad de intervalos no silenciosos,dada por el valor de
# matriz_de_intervalos.shape(0). El valor b es igual al numero de muestras
# del intervalo con mayor cantidad de muestras. Para la brevedad, definimos
# m=matriz_de_intervalos. Entonces, el valor de b esta dado por:
# max ([abs(m[0,0]-m[0,1]),abs(m[1,0]-m[1,1]),...,abs(m[a-1,0]-m[a-1,1]).
# Se puede ver que el valor de b depende del valor de a, mientras que el valor
# de a no depende de b...por eso hay que calcular a primero y b despues.
#
# Para implementar el max([abs(m[0,0]-m[0,1]),abs(m[1,0]-m[1,1]),...,abs(m[a-1,0]-m[a-1,1])
# se puede usar un ciclo for:
#
# maximo= -infinito
# for i desde 0 hasta a-1
#   if abs([abs(m[i,0]-m[i,1]))>maximo
#       maximo=abs([abs(m[i,0]-m[i,1]))
# return maximo
