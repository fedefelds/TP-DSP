import librosa
import numpy as np
import matplotlib.pyplot as plt
carpeta='/Users/Fede/Desktop/The Turn of a Friendly Card 1979 (GPF)/Canciones del trabajo/'
filename='10'
formato='.mp3'
filename=carpeta+filename+formato
# cargar audio
y, sr = librosa.load(filename)
# extraer silencios al principio y final
y,index=librosa.effects.trim(y, top_db=60, ref=np.amax, frame_length=2048, hop_length=50)
# normalizar
valor_max=np.max(y)
y=y/valor_max
# calculo el valor rms
y_rms=y*y
y_rms=np.sum(y_rms)
y_rms=y_rms/len(y)
y_rms=np.sqrt(y_rms)
# calculo el valor maximo
y_max=np.max(y) # siempre vale 1
# calculo el factor de cresta
factor_de_cresta=((y_max)/(y_rms))
print(factor_de_cresta)

