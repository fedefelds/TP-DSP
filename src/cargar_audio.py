# este codigo define la funcion "cargar_audio". La misma se basa en librosa.core.load()
# para mas informacion, ver http://librosa.github.io/librosa/generated/librosa.core.load.html#librosa.core.load

# arg: descripcion..tipo de var..ejemplo..nota <-----

##################################################

# los argumentos de entrada de cargar_audio son los siguientes:

# path: path del audio..string..'/Users/Fede/Box Sync/UNTREF/Ing. De Sonido/DSP/trabajo2/07_Calling_All_My_Lovelies.wav'

# sr: sample rate..[scalar]..44100..si sr=None, usa la sr nativa del archivo

# mono: ..boolean..True..si mono=True, convierte a mono

# offset: empezar a leer despues de offset segundos del archivo..float..offset=0.0

# duration: cargar hasta duration segundos del archivo..float..duration=None..si duration=None, carga todoo el archivo

# dtype: data type de la salida..numeric type..np.float32

# res_type: usar kaiser_best

##################################################

# los argumentos de salida son los siguientes:

# y: señal temporal..np.ndarray

# sr: sample rate..[scalar]

##################################################
# Ejemplo:
# filename='/Users/Fede/Documents/Github/TP-DSP/prueba.wav'
#   y,sr = cargar_audio(filename,None,True,0,None,np.float32,'kaiser_best')
##################################################

import librosa
import numpy as np
import matplotlib.pyplot as plt

def cargar_audio(path, sr, mono, offset, duration,dtype, res_type):

    y,sr = librosa.core.load(path, sr, mono, offset, duration, dtype, res_type)

    return (y,sr)