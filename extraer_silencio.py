# este codigo define la funcion "extraer_silencio". La misma se basa en librosa.effects.split

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
from cargar_audio import cargar_audio # todo:  si no escribo esto asi, me da 'module object is not callable'
import matplotlib.pyplot as plt

def extraer_silencio(y, top_db, ref, frame_length, hop_length):
    y,sr = cargar_audio('/Users/Fede/Documents/Github/TP-DSP/07_Calling_All_My_Lovelies.wav',None,True,0,None,np.float32,'kaiser_best')
    intervals=librosa.effects.split(y, top_db, ref, frame_length , hop_length)

    return intervals

y,sr = cargar_audio('/Users/Fede/Documents/Github/TP-DSP/07_Calling_All_My_Lovelies.wav',None,True,0,None,np.float32,'kaiser_best')
intervals=librosa.effects.split(y)
plt.plot(y[0:1000000])
plt.show()
