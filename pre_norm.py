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
