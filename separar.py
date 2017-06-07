# este codigo define la funcion "separar". La misma se basa en librosa.effects.split

##################################################

# los argumentos de entrada de funcion_nueva son los siguientes:

# arg: descripcion..tipo de var..ejemplo..nota

# y: la señal de audio..np.ndarray, shape=(n,) or (2, n)

# top_db: el umbral (en dB) bajo la referencia que considera como silencio..numero>0

# ref:


##################################################

# los argumentos de salida son los siguientes:

# arg: descripcion..tipo de var..ejemplo..nota



##################################################


#librosa.effects.split(y, top_db=60, ref=<function amax>, frame_length=2048, hop_length=512)


import librosa
import numpy as np
from cargar_audio import cargar_audio  # todo:  si no escribo esto asi, me da 'module object is not callable'
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000

filename='/Users/Fede/Documents/Github/TP-DSP/prueba.wav'

def separar(filename, top_db=60, ref=np.amax, frame_length=1024, hop_length=50):
    y,sr = cargar_audio(filename,None,True,0,None,np.float32,'kaiser_best')
    intervals=librosa.effects.split(y, top_db, ref, frame_length , hop_length)
    return intervals


##################################################
# Ejemplo:
# intervalos=separar(filename,hop_length=50)
# plt.plot()
# print(intervalos[0])
# librosa.output.write_wav('file_trim_5s.wav',intervalo1, sr)
##################################################
