import librosa
import numpy as np
import matplotlib.pyplot as plt
from cargar_audio import cargar_audio

def normalizador(path):
    filename=path
    y, sr = cargar_audio(path, None, True, 0, None, np.float32, 'kaiser_best')
    from  separar import separar
    hop = 50
    m = separar(filename, hop_length=hop)
    for i in range(0,m.shape[0]):
        path='fragmento_' + str(i)
        sig=y[m[i,0]:m[i,1]]
        librosa.output.write_wav('/Users/Fede/Desktop/audio dump/'+path, sig, sr, norm=False)