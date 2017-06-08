# esta funcion se encarga que todos los intervalos no silenciosos tengan la
# misma cantidad de muestras. Esto es para que  pre_norm.py pueda crear una
# matriz en la que cada fila tenga uno de los intervalos no silenciosos. Una ventaja
# de forzar a que todos los intervalos no silenciosos tengan tantas muestras
# como el intervalo no silencioso mas grande es que tenemos igual cantidad de
# puntos en la fft, en caso de ser necesaria (es una ventaja medio rebuscada)
# mientras que como desventaja agrega mas calculos no necesarios.

# todos los intervalos no silenciosos deben tener maximo(m) muestras.
# voy a fijarme fila tras fila, cuantos ceros hay que agregar, y agregarlos.
# para esto uso un ciclo for y np.pad

# for i desde 0 hasta m.shape(0)
#   if len(m[i])<m.shape[0]
#       agrego abs(m.shape[0]-len(m[i])) ceros a m[i]
#   else no toco a m[i]
#
#
# for i desde 0 hasta la ultima fila de la matriz de intervalos
#   if abs(m[i,0]-m[i,1])<m.shape[0]
#
#
#
#
#
#
#



import numpy as np
from maximo import maximo




def padder(m,y):
    matriz_con_ceros=np.zeros([m.shape[0],maximo(m)])
    for i in range(0,m.shape[0]):
        if (m[i,1]-m[i,0])<matriz_con_ceros.shape[1]:
            array_auxiliar=np.pad(y[int(m[i,0]):m[i,1]],(abs(matriz_con_ceros.shape[1]-(m[i,1]-m[i,0]))),'constant')
            array_auxiliar=array_auxiliar[(abs(matriz_con_ceros.shape[1]-(m[i,1]-m[i,0]))):]
            matriz_con_ceros[i]=array_auxiliar
        else:
            matriz_con_ceros[i] = y[int(m[i,0]):m[i,1]]
    return matriz_con_ceros

m=np.array([[0,5],[10,20],[25,30]])
y=[1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 0, 4, 3, 2, 1]
m2=padder(m,y)
print(m2)
