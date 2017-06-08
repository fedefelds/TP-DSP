# esta funcion se encarga que todos los intervalos no silenciosos tengan la
# misma cantidad de muestras. Esto es para que  pre_norm.py pueda crear una
# matriz cuya cada fila tenga uno de los intervalos no silenciosos. Una ventaja
# de forzar a que todos los intervalos no silenciosos tengan tantas muestras
# como el intervalo no silencioso mas grande es que tenemos igual cantidad de
# puntos en la fft, en caso de ser necesaria (es una ventaja medio rebuscada)
# mientras que como desventaja agrega mas calculos no ecesarios.

# todos los intervalos no silenciosos deben tener maximo(m) muestras.
# voy a fijarme fila tras fila, cuantos ceros hay que agregar, y agregarlos.
# para esto uso un ciclo for y np.pad

# for i desde 0 hasta m.shape(0)
#   if len(m[i])<m.shape[0]
#       agrego abs(m.shape[0]-len(m[i])) ceros a m[i]
#   else no toco a m[i]

def padder(m):
for i in range(0,m.shape[0])
    if len(m[i])<m.shape[0]
        m[i]=np.pad[t,abs(m.shape[0]-len(m[i])),'constant']
        m[i]=t2[abs(m.shape[0]-len(m[i])):]
