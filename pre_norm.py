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
from maximo import maximo
mpl.rcParams['agg.path.chunksize'] = 10000

# usar maximo() y padder()
def pre_norm(s):
    m=separar(filename)
    salida_pre_normalizada=padder(m,s)
return salida_pre_normalizada



# matriz_de_intervalos[i]==start and end time (in samples) of non-silent interval i.
# Ej:
# matriz_de_intervalos[1]==[59500,80550]
#
# 1) crear una matriz nula de a filas y b columnas. El numero a es igual a
# la cantidad de intervalos no silenciosos, y esta dada por el valor de
# matriz_de_intervalos.shape(0). El valor b es igual al numero de muestras
# del intervalo con mayor cantidad de muestras. Para la brevedad, definimos
# m=matriz_de_intervalos. Entonces, el valor de b esta dado por:
# max ([abs(m[0,0]-m[0,1]),abs(m[1,0]-m[1,1]),...,abs(m[a-1,0]-m[a-1,1]).
# Se puede ver que el valor de b depende del valor de a, mientras que el valor
# de a no depende de b...por eso hay que calcular a primero y b despues.
#
# Para la implementacion de max([abs(m[0,0]-m[0,1]),abs(m[1,0]-m[1,1]),...,abs(m[a-1,0]-m[a-1,1])
# ver maximo.py (import en linea 25)
#
# 2) Ahora, la idea es asignar a la fila i de la matriz matriz_de_intervalos el intervalo no
# silencioso. Esto se implementa con un loop for:
#
#
#
