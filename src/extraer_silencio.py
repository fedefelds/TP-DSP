import librosa
import numpy as np
import matplotlib.pyplot as plt
from cargar_audio import cargar_audio
filename='/Users/Fede/Documents/Github/TP-DSP/prueba.wav'
from  separar import separar
hop=50
def extraer_silencio(filename, top_db=60, ref=np.amax, frame_length=1024, hop_length=50):
    y, sr = cargar_audio(filename, None, True, 0, None, np.float32, 'kaiser_best')
    return y
