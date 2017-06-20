import librosa
import numpy as np
carpeta='/Users/Fede/Desktop/The Turn of a Friendly Card 1979 (GPF)/Canciones del trabajo/'
filename='9'
formato='.mp3'
filename=carpeta+filename+formato
# cargar audio
y, sr = librosa.load(filename)
# # extraer silencios al principio y final
# y,index=librosa.effects.trim(y, top_db=60, ref=np.amax,
# frame_length=1024, hop_length=50)
# normalizar
valor_max=np.max(y)
y=y/valor_max
# calcular sr
intervals=librosa.effects.split(y, top_db=60, ref=np.amax,
frame_length=1024, hop_length=50)
M_ns=0
for i in range(0,intervals.shape[0]):
    M_ns = M_ns+intervals[i,1]-intervals[i,0]
N=len(y)
SR=((N-M_ns)/N)
SR=np.array([SR])
print(SR)
# np.savetxt('SR'+'.txt',chromagram,delimiter=',',fmt='%.3f', newline=' & ')