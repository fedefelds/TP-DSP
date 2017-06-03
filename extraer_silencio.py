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
import matplotlib.pyplot as plt

def extraer_silencio(y, top_db, ref, frame_length, hop_length):
    intervals=librosa.effects.split(y, top_db=60, ref= < functionamax >, frame_length = 2048, hop_length = 512)
    return intervals
