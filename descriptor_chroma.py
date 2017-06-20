import librosa
import numpy as np
carpeta='/Users/Fede/Desktop/'
filename='copia de burno mars'
formato='.mp3'
filename=carpeta+filename+formato
# cargar audio
y, sr = librosa.load(filename)
# extraer silencios al principio y final
y,index=librosa.effects.trim(y, top_db=60, ref=np.amax,
frame_length=1024, hop_length=50)
# normalizar
valor_max=np.max(y)
y=y/valor_max
# calculo el chromagram
chromagram=librosa.feature.chroma_cqt(y,sr)
chromagram=np.mean(chromagram,1)
np.savetxt(chroma+'.txt',chromagram,delimiter=',',fmt='%.3f', newline=' & ')
