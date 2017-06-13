import librosa
import numpy as np
from cargar_audio import cargar_audio




def extraer_silencio(filename, top_db=60, refe=np.amax, frame_length=1024):
    y, sr = cargar_audio(filename, None, True, 0, None, np.float32, 'kaiser_best')
    cancion,index=librosa.effects.trim(y, top_db=top_db, ref=refe, frame_length=frame_length, hop_length=50)
    return y,index

