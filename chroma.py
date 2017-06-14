import librosa

from extraer_silencio import extraer_silencio
from normalizar import normalizar
import matplotlib.pyplot as plt
from cargar_audio import cargar_audio
def chromagram(filename,S=None,norm=None,n_fft=2048,hop_length=50):
    y,sr=cargar_audio(filename,sr=None)
    y,index = extraer_silencio(filename)
    y = normalizar(y)
    chromagrama=librosa.feature.chroma_cqt(y,sr)
    plt.figure(figsize=(10,4))
    librosa.display.specshow(chromagrama,y_axis='chroma',x_axis='time',sr=sr)
    plt.colorbar()
    plt.title('chromagram')
    plt.tight_layout()
    plt.show()

chromagram('/Users/Fede/Documents/Github/TP-DSP/07_Calling_All_My_Lovelies.wav')

